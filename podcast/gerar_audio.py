#!/usr/bin/env python3
"""Gera o episódio do podcast a partir de um roteiro JSON.
Uso: python3 gerar_audio.py roteiro.json saida.mp3
roteiro.json = [{"speaker": "Ana", "text": "..."}, ...]
PODCAST_VOZES='{"Ana":"Kore","Leo":"Puck"}' define apresentadores e vozes.
GEMINI_API_KEY é opcional: sem ela, a chave vem da credencial guardada no ambiente.
PODCAST_MOCK=1 troca a voz por um tom de teste (valida a cadeia sem usar a API).
Saída: MP3 mono 48 kbps (cerca de 0,35 MB por minuto).
"""
import base64, json, os, ssl, subprocess, sys, tempfile, time, urllib.error, urllib.request

MODEL = os.environ.get("PODCAST_TTS_MODEL", "gemini-3.8-flash-tts")
LEGACY_MODEL = os.environ.get("PODCAST_TTS_LEGACY_MODEL", "gemini-3.1-flash-tts-preview")
VOICES = json.loads(os.environ.get("PODCAST_VOZES", '{"Ana":"Kore","Leo":"Puck"}'))
STYLE = os.environ.get("PODCAST_ESTILO", "podcast brasileiro de notícias, tom leve, ritmo natural, português do Brasil")
BASE = "https://generativelanguage.googleapis.com/v1beta"
CHUNK_CHARS = 1800  # blocos menores evitam timeout e cortes

def ctx():
    ca = "/root/.ccr/ca-bundle.crt"
    return ssl.create_default_context(cafile=ca) if os.path.exists(ca) else ssl.create_default_context()

def post(url, body, key):
    headers = {"Content-Type": "application/json"}
    if key:
        headers["x-goog-api-key"] = key
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers)
    with urllib.request.urlopen(req, context=ctx(), timeout=240) as r:
        return json.load(r)

def tts_interactions(turns, key):
    body = {
        "model": MODEL,
        "input": [{"type": "user_input", "content": [
            {"type": "text", "text": t["text"],
             "annotations": [{"type": "speech_metadata", "speaker": t["speaker"], "style": STYLE}]}
            for t in turns]}],
        "response_format": {"type": "audio"},
        "generation_config": {"speech_config": {"mode": "conversational",
            "speakers": [{"speaker": s, "voice": v} for s, v in VOICES.items()]}},
    }
    r = post(f"{BASE}/interactions", body, key)
    for step in r.get("steps", []):
        for c in step.get("content", []):
            if c.get("data"):
                return base64.b64decode(c["data"]), "wav"
    if r.get("output_audio", {}).get("data"):
        return base64.b64decode(r["output_audio"]["data"]), "wav"
    raise RuntimeError("interactions sem áudio: " + json.dumps(r)[:400])

def tts_legacy(turns, key):
    txt = "\n".join(f'{t["speaker"]}: {t["text"]}' for t in turns)
    body = {
        "contents": [{"parts": [{"text": f"Leia como {STYLE}:\n{txt}"}]}],
        "generationConfig": {"responseModalities": ["AUDIO"], "speechConfig": {"multiSpeakerVoiceConfig": {
            "speakerVoiceConfigs": [{"speaker": s, "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": v}}}
                                    for s, v in VOICES.items()]}}},
    }
    r = post(f"{BASE}/models/{LEGACY_MODEL}:generateContent", body, key)
    part = r["candidates"][0]["content"]["parts"][0]["inlineData"]
    return base64.b64decode(part["data"]), ("wav" if "wav" in part.get("mimeType", "") else "pcm")

def tts_mock(turns, key):
    secs = max(1.0, sum(len(t["text"]) for t in turns) / 15.0)
    out = subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", f"sine=frequency=440:duration={secs:.1f}",
                          "-ar", "24000", "-ac", "1", "-f", "wav", "-"], capture_output=True, check=True)
    return out.stdout, "wav"

def chunks(turns):
    cur, size = [], 0
    for t in turns:
        if cur and size + len(t["text"]) > CHUNK_CHARS:
            yield cur; cur, size = [], 0
        cur.append(t); size += len(t["text"])
    if cur: yield cur

def synth(turns, key):
    if os.environ.get("PODCAST_MOCK") == "1":
        return tts_mock(turns, key)
    last = None
    for fn in (tts_interactions, tts_legacy):
        for attempt in range(2):
            try:
                return fn(turns, key)
            except urllib.error.HTTPError as e:
                last = f"{fn.__name__} HTTP {e.code}: {e.read()[:300]!r}"
                if e.code in (400, 404): break  # formato ou modelo: tenta a outra rota
            except Exception as e:
                last = f"{fn.__name__}: {e}"
            time.sleep(3)
    raise RuntimeError(last)

def main():
    roteiro, saida = sys.argv[1], sys.argv[2]
    key = os.environ.get("GEMINI_API_KEY", "")
    turns = [t for t in json.load(open(roteiro)) if t.get("text", "").strip()]
    primeiro = next(iter(VOICES))
    for t in turns:
        if t.get("speaker") not in VOICES: t["speaker"] = primeiro
    os.makedirs(os.path.dirname(os.path.abspath(saida)), exist_ok=True)
    tmp = tempfile.mkdtemp()
    parts = []
    for i, grp in enumerate(chunks(turns)):
        data, kind = synth(grp, key)
        raw = os.path.join(tmp, f"p{i}.{kind}")
        open(raw, "wb").write(data)
        wav = os.path.join(tmp, f"n{i}.wav")
        src = ["-f", "s16le", "-ar", "24000", "-ac", "1", "-i", raw] if kind == "pcm" else ["-i", raw]
        subprocess.run(["ffmpeg", "-v", "error", "-y", *src, "-ar", "24000", "-ac", "1", wav], check=True)
        parts.append(wav)
    lst = os.path.join(tmp, "lista.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                    "-af", "loudnorm=I=-16:TP=-1.5", "-ar", "24000", "-c:a", "libmp3lame", "-b:a", "48k", "-ac", "1",
                    saida], check=True)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                                "default=nw=1:nk=1", saida], capture_output=True, text=True).stdout.strip())
    print(json.dumps({"arquivo": saida, "duracao": f"{int(dur // 60)}:{int(dur % 60):02d}",
                      "segundos": int(dur), "bytes": os.path.getsize(saida), "blocos": len(parts)}))

if __name__ == "__main__":
    main()
