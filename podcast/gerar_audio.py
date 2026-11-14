#!/usr/bin/env python3
"""Gera o episódio do podcast a partir de um roteiro JSON.

Uso:      python3 gerar_audio.py roteiro.json saida.mp3
Roteiro:  [{"speaker": "Ana", "text": "..."}, {"speaker": "Leo", "text": "..."}]

Variáveis de ambiente:
  PODCAST_VOZES             '{"Ana":"Kore","Leo":"Puck"}'
  PODCAST_TTS_MODEL         modelo principal (rota /interactions)
  PODCAST_TTS_LEGACY_MODEL  modelo da rota alternativa (generateContent)
  PODCAST_INTERACTIONS_MODE valor de speech_config.mode (padrão: vazio = não enviar)
  PODCAST_MAX_TENTATIVAS    máximo de chamadas por bloco, somando as duas rotas (padrão 4)
  PODCAST_ESPERA_MAX        espera máxima entre tentativas, em segundos (padrão 90)
  PODCAST_MANTER_PARTES=1   não apaga a pasta de blocos após o sucesso
  PODCAST_DRY_RUN=1         só mostra o plano de blocos; nenhuma chamada
  PODCAST_TEST_ONCE=1       teste controlado: UMA chamada, só o modelo principal,
                            sem nova tentativa, sem rota alternativa, texto fixo curto
  PODCAST_MOCK=1            troca a voz por um tom de teste (sem API)
  GEMINI_API_KEY            opcional: sem ela, a chave vem da credencial do ambiente
                            (a chave nunca é impressa nem gravada)

Saída: MP3 mono 48 kbps. Códigos de saída: 0 = MP3 final gerado e completo;
2 = falha na geração (nenhum MP3 final é criado); 1 = erro de uso ou do teste.
Resumo em saida.mp3.status.json: só use o áudio (e só anuncie o episódio) se "ok" for true.
Blocos já gerados ficam em saida.mp3.partes/ e são reaproveitados numa nova execução.
"""
import base64, email.utils, hashlib, json, os, random, re, shutil, ssl, subprocess
import sys, tempfile, time, urllib.error, urllib.request

MODEL = os.environ.get("PODCAST_TTS_MODEL", "gemini-3.8-flash-tts")
LEGACY_MODEL = os.environ.get("PODCAST_TTS_LEGACY_MODEL", "gemini-3.1-flash-tts-preview")
VOICES = json.loads(os.environ.get("PODCAST_VOZES", '{"Ana":"Kore","Leo":"Puck"}'))
STYLE = os.environ.get("PODCAST_ESTILO", "podcast brasileiro de notícias, tom leve, ritmo natural, português do Brasil")
SPEECH_MODE = os.environ.get("PODCAST_INTERACTIONS_MODE", "")
MAX_ATTEMPTS = int(os.environ.get("PODCAST_MAX_TENTATIVAS", "4"))
MAX_WAIT = float(os.environ.get("PODCAST_ESPERA_MAX", "90"))
BASE = "https://generativelanguage.googleapis.com/v1beta"
CHUNK_CHARS = 4000  # blocos menores evitam timeout e cortes
TEST_TURNS = [
    {"speaker": "Ana", "text": "Olá, este é um teste rápido de voz."},
    {"speaker": "Leo", "text": "E aqui é o Leo, confirmando que o áudio funciona."},
]
TRANSIENT = ("transitorio", "limite_temporario", "limite_incerto")


# ---------- log sem segredos ----------
def scrub(text):
    text = str(text)
    key = os.environ.get("GEMINI_API_KEY", "")
    if key:
        text = text.replace(key, "[chave]")
    return re.sub(r"AIza[0-9A-Za-z_\-]{20,}", "[chave]", text)

def log(**fields):
    print(scrub(json.dumps(fields, ensure_ascii=False)), file=sys.stderr, flush=True)


# ---------- HTTP ----------
class ApiError(Exception):
    def __init__(self, code, body="", retry_after=None):
        super().__init__(f"HTTP {code}")
        self.code, self.body, self.retry_after = code, body, retry_after

class BlockFailed(Exception):
    def __init__(self, kind, code):
        super().__init__(f"{kind} (HTTP {code})")
        self.kind, self.code = kind, code

def ctx():
    ca = "/root/.ccr/ca-bundle.crt"
    return ssl.create_default_context(cafile=ca) if os.path.exists(ca) else ssl.create_default_context()

def parse_retry_after(value):
    """Retry-After: segundos inteiros ou data HTTP."""
    if not value:
        return None
    value = value.strip()
    if value.isdigit():
        return float(value)
    try:
        return max(0.0, email.utils.parsedate_to_datetime(value).timestamp() - time.time())
    except Exception:
        return None

def body_retry_delay(body):
    m = re.search(r'"retryDelay"\s*:\s*"([\d.]+)s"', body or "")
    return float(m.group(1)) if m else None

def post(url, body, key):
    """Devolve (status, json). Erros viram ApiError (código 0 = falha de rede)."""
    headers = {"Content-Type": "application/json"}
    if key:
        headers["x-goog-api-key"] = key
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx(), timeout=240) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        raw = e.read()[:4000].decode("utf-8", "replace")
        raise ApiError(e.code, raw, parse_retry_after(e.headers.get("Retry-After")))
    except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
        raise ApiError(0, f"rede: {type(e).__name__}")

def classify(e):
    """Tipo do erro: decide se vale repetir."""
    c, low = e.code, (e.body or "").lower()
    if c == 0 or c in (500, 502, 503, 504):
        return "transitorio"
    if c == 429:
        minuto = ("perminute" in low or "per minute" in low
                  or body_retry_delay(e.body) is not None or e.retry_after is not None)
        dia = "perday" in low or "per day" in low or "daily" in low or "limit: 0" in low
        if dia and not minuto:
            return "quota_esgotada"      # não adianta esperar
        if minuto:
            return "limite_temporario"   # limite por minuto: esperar o tempo pedido
        return "limite_incerto"          # mensagem genérica: repete, mas dentro do teto de tentativas
    if c == 401 or "api key not valid" in low or "api_key_invalid" in low:
        return "autenticacao"
    if c == 403:
        return "permissao_ou_faturamento"
    if c == 400 and ("failed_precondition" in low or "billing" in low):
        return "faturamento"
    if c == 404:
        return "modelo_inexistente"
    if c == 400:
        return "requisicao_invalida"
    return "erro_nao_repetivel"

def wait_for(e, n):
    """Espera progressiva com jitter; respeita Retry-After e retryDelay."""
    base = min(MAX_WAIT, 2.0 * 2 ** (n - 1))
    wait = random.uniform(base / 2, base)
    asked = e.retry_after if e.retry_after is not None else body_retry_delay(e.body)
    return max(wait, asked) if asked is not None else wait


# ---------- rotas ----------
def audio_kind(mime, default="wav"):
    mime = (mime or "").lower()
    return "pcm" if ("l16" in mime or "pcm" in mime) else default

def tts_interactions(turns, key):
    speech = {"speakers": [{"speaker": s, "voice": v} for s, v in VOICES.items()]}
    if SPEECH_MODE:
        speech["mode"] = SPEECH_MODE
    body = {
        "model": MODEL,
        "input": [{"type": "user_input", "content": [
            {"type": "text", "text": t["text"],
             "annotations": [{"type": "speech_metadata", "speaker": t["speaker"], "style": STYLE}]}
            for t in turns]}],
        "response_format": {"type": "audio"},
        "generation_config": {"speech_config": speech},
    }
    status, r = post(f"{BASE}/interactions", body, key)
    for step in r.get("steps", []):
        for c in step.get("content", []):
            if c.get("data"):
                return status, base64.b64decode(c["data"]), audio_kind(c.get("mime_type"))
    if r.get("output_audio", {}).get("data"):
        return status, base64.b64decode(r["output_audio"]["data"]), audio_kind(r["output_audio"].get("mime_type"))
    raise ApiError(status, "resposta 200 sem áudio: " + json.dumps(r)[:300])

def tts_legacy(turns, key):
    txt = "\n".join(f'{t["speaker"]}: {t["text"]}' for t in turns)
    body = {
        "contents": [{"parts": [{"text": f"Leia como {STYLE}:\n{txt}"}]}],
        "generationConfig": {"responseModalities": ["AUDIO"], "speechConfig": {"multiSpeakerVoiceConfig": {
            "speakerVoiceConfigs": [{"speaker": s, "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": v}}}
                                    for s, v in VOICES.items()]}}},
    }
    status, r = post(f"{BASE}/models/{LEGACY_MODEL}:generateContent", body, key)
    try:
        part = r["candidates"][0]["content"]["parts"][0]["inlineData"]
    except (KeyError, IndexError, TypeError):
        raise ApiError(status, "resposta 200 sem áudio: " + json.dumps(r)[:300])
    return status, base64.b64decode(part["data"]), audio_kind(part.get("mimeType"), "pcm" if "wav" not in part.get("mimeType", "") else "wav")

def tts_mock(turns, key):
    secs = max(1.0, sum(len(t["text"]) for t in turns) / 15.0)
    out = subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", f"sine=frequency=440:duration={secs:.1f}",
                          "-ar", "24000", "-ac", "1", "-f", "wav", "-"], capture_output=True, check=True)
    return 200, out.stdout, "wav"

ROUTES = [("interactions", lambda: MODEL, tts_interactions),
          ("generateContent", lambda: LEGACY_MODEL, tts_legacy)]


# ---------- um bloco, com tentativas limitadas ----------
def synth_block(turns, key, idx, stats):
    """Devolve (dados, tipo). Total de chamadas por bloco <= MAX_ATTEMPTS (somando as rotas)."""
    if os.environ.get("PODCAST_MOCK") == "1":
        _, data, kind = tts_mock(turns, key)
        return data, kind
    attempts = 0
    for r_idx, (route, model_fn, fn) in enumerate(ROUTES):
        failures_here = 0
        while True:
            if attempts >= MAX_ATTEMPTS:
                raise BlockFailed("limite_de_tentativas", stats["ultimo_http"])
            attempts += 1
            stats["chamadas"] += 1
            entry = {"bloco": idx, "tentativa": attempts, "rota": route, "modelo": model_fn()}
            try:
                status, data, kind = fn(turns, key)
                stats["modelos"].add(model_fn())
                stats["ultimo_http"] = status
                log(**entry, http=status, resultado="ok")
                return data, kind
            except ApiError as e:
                failures_here += 1
                stats["ultimo_http"] = e.code
                tipo = classify(e)
                stats["erros"].append({**entry, "http": e.code, "tipo": tipo})
                log(**entry, http=e.code, resultado="erro", tipo=tipo, mensagem=(e.body or "")[:200])
                if tipo in TRANSIENT:
                    wait = wait_for(e, failures_here)
                    if wait > MAX_WAIT:
                        raise BlockFailed("espera_pedida_acima_do_limite", e.code)
                    if attempts >= MAX_ATTEMPTS:
                        raise BlockFailed(tipo, e.code)
                    log(**entry, espera_s=round(wait, 1))
                    time.sleep(wait)
                    continue
                # erro que NÃO se repete: só cai para a rota alternativa quando o problema
                # é o formato/modelo da rota nova (outra requisição, não repetição da mesma)
                if (tipo in ("requisicao_invalida", "modelo_inexistente")
                        and r_idx == 0 and len(ROUTES) > 1):
                    log(**entry, aviso="rota alternativa")
                    break
                raise BlockFailed(tipo, e.code)
    raise BlockFailed("sem_rota", stats["ultimo_http"])


# ---------- blocos e áudio ----------
def chunks(turns):
    """Blocos de até CHUNK_CHARS; cada bloco fecha só depois de ter as duas vozes."""
    cur, size = [], 0
    for t in turns:
        if cur and size + len(t["text"]) > CHUNK_CHARS and len({x["speaker"] for x in cur}) >= 2:
            yield cur
            cur, size = [], 0
        cur.append(t)
        size += len(t["text"])
    if cur:
        yield cur

def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                          "default=nw=1:nk=1", path], capture_output=True, text=True).stdout.strip()
    return float(out) if out else 0.0

def fmt(sec):
    return f"{int(sec // 60)}:{int(sec % 60):02d}"

def to_wav(data, kind, dest, tmpdir):
    raw = os.path.join(tmpdir, "raw." + kind)
    open(raw, "wb").write(data)
    src = ["-f", "s16le", "-ar", "24000", "-ac", "1", "-i", raw] if kind == "pcm" else ["-i", raw]
    subprocess.run(["ffmpeg", "-v", "error", "-y", *src, "-ar", "24000", "-ac", "1", dest], check=True)

def block_id(turns):
    h = hashlib.sha256(json.dumps([turns, VOICES, STYLE, MODEL], ensure_ascii=False, sort_keys=True).encode())
    return h.hexdigest()[:12]

def write_status(path, **fields):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(fields, f, ensure_ascii=False, indent=1)


# ---------- teste controlado ----------
def run_test(key):
    """UMA chamada, só o modelo principal, sem nova tentativa, sem rota alternativa."""
    result = {"modo": "teste", "modelo": MODEL, "rota": "interactions", "chamadas": 1}
    tmp = tempfile.mkdtemp()
    try:
        status, data, kind = tts_mock(TEST_TURNS, key) if os.environ.get("PODCAST_MOCK") == "1" \
            else tts_interactions(TEST_TURNS, key)
        wav = os.path.join(tmp, "t.wav")
        to_wav(data, kind, wav, tmp)
        sec = duration(wav)
        result.update(http=status, resultado="ok", duracao=fmt(sec), segundos=round(sec, 1), bytes=len(data))
        code = 0
    except ApiError as e:
        result.update(http=e.code, resultado="erro", tipo=classify(e), mensagem=scrub((e.body or "")[:300]))
        code = 1
    except Exception as e:
        result.update(http=None, resultado="erro", mensagem=scrub(f"{type(e).__name__}: {e}")[:300])
        code = 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(json.dumps(result, ensure_ascii=False))
    return code


# ---------- principal ----------
def main():
    key = os.environ.get("GEMINI_API_KEY", "")
    if os.environ.get("PODCAST_TEST_ONCE") == "1":
        return run_test(key)
    if len(sys.argv) < 3:
        print(__doc__, file=sys.stderr)
        return 1
    roteiro, saida = sys.argv[1], sys.argv[2]
    turns = [t for t in json.load(open(roteiro, encoding="utf-8")) if t.get("text", "").strip()]
    first = next(iter(VOICES))
    for t in turns:
        if t.get("speaker") not in VOICES:
            t["speaker"] = first
    blocks = list(chunks(turns))
    if os.environ.get("PODCAST_DRY_RUN") == "1":
        print(json.dumps({"blocos": len(blocks), "chamadas_minimas": len(blocks),
                          "caracteres_por_bloco": [sum(len(t["text"]) for t in b) for b in blocks],
                          "modelo": MODEL}, ensure_ascii=False))
        return 0

    out_abs = os.path.abspath(saida)
    os.makedirs(os.path.dirname(out_abs), exist_ok=True)
    parts_dir, status_path = out_abs + ".partes", out_abs + ".status.json"
    os.makedirs(parts_dir, exist_ok=True)
    stats = {"chamadas": 0, "erros": [], "modelos": set(), "ultimo_http": None}
    tmp = tempfile.mkdtemp()
    wavs, reused = [], 0
    try:
        for i, grp in enumerate(blocks):
            wav = os.path.join(parts_dir, f"bloco-{i:03d}-{block_id(grp)}.wav")
            if os.path.exists(wav) and duration(wav) > 0:
                reused += 1
                log(bloco=i, resultado="reaproveitado")
            else:
                data, kind = synth_block(grp, key, i, stats)
                part = wav + ".tmp.wav"
                to_wav(data, kind, part, tmp)
                os.replace(part, wav)
            wavs.append(wav)
        lst = os.path.join(tmp, "lista.txt")
        open(lst, "w").write("".join(f"file '{p}'\n" for p in wavs))
        final_tmp = out_abs + ".tmp.mp3"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                        "-af", "loudnorm=I=-16:TP=-1.5", "-ar", "24000", "-c:a", "libmp3lame", "-b:a", "48k",
                        "-ac", "1", "-f", "mp3", final_tmp], check=True)
        sec = duration(final_tmp)
        if sec <= 0:
            raise BlockFailed("mp3_invalido", stats["ultimo_http"])
        os.replace(final_tmp, out_abs)  # só aqui o MP3 final passa a existir
    except BlockFailed as e:
        summary = {"ok": False, "motivo": str(e), "blocos": len(blocks), "reaproveitados": reused,
                   "chamadas": stats["chamadas"], "erros": stats["erros"],
                   "modelos": sorted(stats["modelos"]), "partes": parts_dir}
        write_status(status_path, **summary)
        print(json.dumps(summary, ensure_ascii=False))
        return 2
    except subprocess.CalledProcessError as e:
        summary = {"ok": False, "motivo": f"ffmpeg falhou ({e.returncode})", "blocos": len(blocks),
                   "chamadas": stats["chamadas"], "erros": stats["erros"], "partes": parts_dir}
        write_status(status_path, **summary)
        print(json.dumps(summary, ensure_ascii=False))
        return 2
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        if os.path.exists(out_abs + ".tmp.mp3"):
            os.remove(out_abs + ".tmp.mp3")

    if os.environ.get("PODCAST_MANTER_PARTES") != "1":
        shutil.rmtree(parts_dir, ignore_errors=True)
    summary = {"ok": True, "arquivo": saida, "duracao": fmt(sec), "segundos": int(sec),
               "bytes": os.path.getsize(out_abs), "blocos": len(blocks), "reaproveitados": reused,
               "chamadas": stats["chamadas"], "erros": stats["erros"], "modelos": sorted(stats["modelos"])}
    write_status(status_path, **summary)
    print(json.dumps(summary, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
