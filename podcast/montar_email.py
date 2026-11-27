import html, json
A="#1F3A5F"
def e(s): return html.escape(s, quote=True)
def item(t, destaque=False):
    bg = "#EEF2F7" if destaque else "#FFFFFF"
    bl = f"border-left:4px solid {A};" if destaque else ""
    lab = f'<p style="margin:0 0 6px 0;font-family:Arial,Helvetica,sans-serif;font-size:11px;font-weight:bold;letter-spacing:1px;color:{A};text-transform:uppercase;">Destaque</p>' if destaque else ""
    L=e(t["link"])
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{bg}" style="margin:0 0 14px 0;"><tr><td bgcolor="{bg}" style="background-color:{bg};{bl}padding:16px 18px;">{lab}'
      f'<p style="margin:0 0 6px 0;font-family:Arial,Helvetica,sans-serif;font-size:17px;line-height:1.35;font-weight:bold;color:{A};"><a href="{L}" style="color:{A};text-decoration:none;">{e(t["titulo"])}</a></p>'
      f'<p style="margin:0 0 8px 0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.6;color:#222222;">{e(t["resumo"])}</p>'
      f'<p style="margin:0 0 8px 0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.6;color:#222222;"><b>Por que importa:</b> {e(t["pq"])}</p>'
      f'<p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.5;color:#666666;">{e(t["veiculo"])} · {t["data"]} · <a href="{L}" style="color:{A};">Ler a matéria</a></p></td></tr></table>\n')
def secao(n): return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:10px 0 10px 0;"><tr><td style="border-top:2px solid {A};padding-top:10px;font-family:Arial,Helvetica,sans-serif;font-size:13px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:{A};">{n}</td></tr></table>\n'
d=json.load(open("podcast/noticias.json",encoding="utf-8"))
out=['<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0;padding:0;background-color:#FFFFFF;">\n<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF"><tr><td align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:16px 8px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:640px;"><tr><td>\n']
out.append(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{A}"><tr><td bgcolor="{A}" style="background-color:{A};padding:20px 22px;"><p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:24px;font-weight:bold;color:#FFFFFF;">Digest Diário</p><p style="margin:4px 0 0 0;font-family:Arial,Helvetica,sans-serif;font-size:14px;color:#FFFFFF;">Sexta-feira, 27 de novembro de 2026</p></td></tr></table>\n')
n=1+sum(len(v) for v in d["secoes"].values())
out.append(f'<p style="margin:14px 0 16px 0;font-family:Arial,Helvetica,sans-serif;font-size:13px;color:#555555;">{n} notícias de {d["veiculos"]} veículos · últimas 24 horas (26/11, 09h16, a 27/11, 09h16, horário de Bruxelas)</p>\n')
out.append(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#EEF2F7" style="margin:0 0 14px 0;"><tr><td bgcolor="#EEF2F7" style="background-color:#EEF2F7;padding:14px 18px;"><p style="margin:0 0 10px 0;font-family:Arial,Helvetica,sans-serif;font-size:14px;color:#222222;"><b>Ouvir o resumo desta edição</b> · 3:53 min, com Ana e Leo</p><table role="presentation" cellpadding="0" cellspacing="0" border="0" bgcolor="{A}"><tr><td bgcolor="{A}" style="background-color:{A};padding:10px 18px;"><a href="https://bdiehlc-bit.github.io/digest-podcast/?ep=2026-11-27" style="font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#FFFFFF;text-decoration:none;">Ouvir agora</a></td></tr></table></td></tr></table>\n')
out.append(item(d["destaque"],True))
for s,its in d["secoes"].items():
    if its:
        out.append(secao(s)); out += [item(t) for t in its]
out.append('<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:8px;"><tr><td style="border-top:1px solid #DDDDDD;padding-top:12px;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.5;color:#777777;">Montado automaticamente. Cada notícia foi conferida na fonte ou em segunda fonte. Ouça também no seu app de podcast: https://bdiehlc-bit.github.io/digest-podcast/feed.xml</td></tr></table>\n</td></tr></table></td></tr></table></body></html>')
open("podcast/email.html","w",encoding="utf-8").write("".join(out))
print(n, len("".join(out)))
