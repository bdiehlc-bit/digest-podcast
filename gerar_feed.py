#!/usr/bin/env python3
"""Gera feed.xml (RSS de podcast) a partir de episodes.json.
Uso: python3 gerar_feed.py [pasta]   (padrão: pasta deste script)
PODCAST_BASE_URL define o endereço público do site (termina com /).
Amostras (arquivo com "amostra" no nome) ficam fora do feed.
"""
import email.utils, json, os, sys, datetime
from xml.sax.saxutils import escape

BASE = os.environ.get("PODCAST_BASE_URL", "https://bdiehlc-bit.github.io/digest-podcast/")
TITLE = "Digest Diário em Áudio"
DESC = "A conversa de cada manhã sobre as notícias do Digest Diário: Bélgica, Brasil, tecnologia e o mundo, com Ana e Leo."
AUTHOR = "Digest Diário"

def main():
    pasta = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    eps = json.load(open(os.path.join(pasta, "episodes.json")))
    items = []
    for e in eps:
        arq = e["arquivo"]
        if "amostra" in arq:
            continue
        slug = os.path.splitext(os.path.basename(arq))[0]
        y, m, d = map(int, e["data"].split("-"))
        pub = email.utils.format_datetime(datetime.datetime(y, m, d, 6, 0, tzinfo=datetime.timezone.utc))
        size = os.path.getsize(os.path.join(pasta, arq))
        caps = e.get("capitulos") or []
        resumo = "Neste episódio: " + ", ".join(caps) + "." if caps else e.get("titulo", "")
        items.append(f"""    <item>
      <title>{escape(e.get("titulo", slug))}</title>
      <description>{escape(resumo)}</description>
      <link>{BASE}?ep={slug}</link>
      <guid isPermaLink="false">{escape(slug)}</guid>
      <pubDate>{pub}</pubDate>
      <enclosure url="{BASE}{arq}" length="{size}" type="audio/mpeg"/>
      <itunes:duration>{e.get("duracao", "")}</itunes:duration>
      <itunes:explicit>false</itunes:explicit>
    </item>""")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{TITLE}</title>
    <link>{BASE}</link>
    <atom:link href="{BASE}feed.xml" rel="self" type="application/rss+xml"/>
    <description>{escape(DESC)}</description>
    <language>pt-br</language>
    <itunes:author>{AUTHOR}</itunes:author>
    <itunes:image href="{BASE}capa.jpg"/>
    <itunes:category text="News"/>
    <itunes:explicit>false</itunes:explicit>
    <itunes:type>episodic</itunes:type>
{chr(10).join(items)}
  </channel>
</rss>
"""
    open(os.path.join(pasta, "feed.xml"), "w").write(xml)
    print(f"feed.xml: {len(items)} episódio(s)")

if __name__ == "__main__":
    main()
