import json, html
E = html.escape
D = lambda t, r, p, v, d, l, a=False: dict(t=t, r=r, p=p, v=v, d=d, l=l)
destaque = D("Setca acusa governo de recusar a prépension para os 1.217 demitidos da GSK (atualização)",
 "Segundo a RTBF, o sindicato Setca critica a recusa do governo federal em reintroduzir o regime de prépension (RCC) para os trabalhadores atingidos pelas 1.217 demissões anunciadas pela GSK. O ministro do Emprego, David Clarinval, disse que o Estado não deve pagar a prépension no lugar da empresa; o Setca chamou a posição de inaceitável e lembrou que o Estado concede 481 milhões de euros em ajuda pública ao grupo.",
 "o caso é na sua região, o Brabant wallon, e define que apoio terão os demitidos.",
 "RTBF","19/10/2026","https://www.rtbf.be/article/le-setc-accuse-le-gouvernement-federal-de-priver-les-travailleurs-licencies-d-une-solution-d-accompagnement-11802706","")
secoes = [
("Bélgica", [
D("Francken e Quintin propõem uma “gendarmerie 2.0” e sindicatos se dividem (atualização)",
 "Segundo a RTBF, o ministro da Defesa, Theo Francken (N-VA), e o do Interior, Bernard Quintin (MR), propõem uma força que reuniria formação policial e militar, nos moldes da gendarmeria desmilitarizada em 1991. Os sindicatos SNPS e ACMP-CGMP apoiam; CGSP e SLFP pedem mais pessoal e recursos. PS, Ecolo e PTB são contra, e o PS cita um déficit de 70 milhões de euros na Polícia Federal em 2026.",
 "é uma proposta, não uma decisão, mas abre um debate político sobre segurança pública no país.",
 "RTBF","19/10/2026","https://www.rtbf.be/article/creation-d-une-gendarmerie-2-0-proposee-par-les-ministres-quintin-et-francken-reactions-contrastees-aupres-des-syndicats-11802591",""),
D("Orçamento de saúde de 2027 fica sem acordo no Inami",
 "Segundo a La Libre, na segunda (19/10) os representantes do governo federal se abstiveram no Conselho Geral do Inami, e a proposta de orçamento de saúde de 2027, que previa economia de 141,5 milhões de euros, não foi adotada por falta de unanimidade. O presidente do CIN, Luc Van Gorp, alertou para o risco de graves dificuldades no setor. Sem acordo, o governo terá de decidir sozinho.",
 "afeta o financiamento do sistema de saúde em que você é atendido.",
 "La Libre","19/10/2026","https://www.lalibre.be/belgique/politique-belge/2026/10/19/budget-des-soins-de-sante-2027-le-gouvernement-federal-echoue-a-trouver-un-accord-22VFUZUSIBAO7EAME6LYHDIOBU/",""),
D("Banco Nacional: Bélgica precisa de um quadro orçamentário nacional vinculante",
 "Segundo a RTBF, o Banco Nacional diz que o déficit chegou a 5,2% do PIB em 2025, nível inédito desde o início dos anos 1980, e que o país precisa de regras orçamentárias vinculantes para pôr a dívida em trajetória sustentável. A BNB aponta queda de receitas e alta dos gastos primários, em 7 bilhões de euros no nível federal e 2 bilhões no regional. FGTB e CSC pedem esforço dos “ombros mais largos”.",
 "é o pano de fundo da negociação do orçamento federal, que decide impostos e indexações.",
 "RTBF","19/10/2026","https://www.rtbf.be/article/budget-federal-la-belgique-a-besoin-d-un-cadre-budgetaire-national-contraignant-analyse-la-banque-nationale-bnb-11802557",""),
D("Ahold Delhaize registra queixa na polícia holandesa após ciberataque (atualização)",
 "Segundo a RTBF, o grupo, dono da Delhaize e da Albert Heijn, apresentou queixa depois do incidente de domingo, 11/10; a investigação interna aponta ações maliciosas de terceiros. A empresa diz não ter indício de roubo de dados sensíveis de clientes, funcionários ou parceiros. Mais de uma semana depois, os sistemas ainda não estavam totalmente restabelecidos.",
 "a Delhaize é uma das grandes redes de supermercado do país onde você faz compras.",
 "RTBF","19/10/2026","https://www.rtbf.be/article/cyberattaque-chez-delhaize-ahold-delhaize-porte-plainte-aupres-de-la-police-neerlandaise-apres-l-incident-du-11-octobre-11802748",""),
D("Vinheta rodoviária da Valônia começa em 1º de maio de 2027",
 "Segundo a RTBF, que publicou um explicativo na segunda (19/10), a vinheta vale para veículos de até 3,5 toneladas em autoestradas e vias regionais: 90 euros para elétricos, 100 para Euro 4 ou mais novos e 125 para Euro 0 a 3. A Valônia reduz o imposto de circulação em 70% do valor, e os outros 30% viram um bônus de emprego pago em 2028, de 50 a 500 euros. Quem não trabalha fica de fora do bônus.",
 "toca o bolso de quem dirige no Brabant wallon.",
 "RTBF","19/10/2026","https://www.rtbf.be/article/la-vignette-auto-en-6-questions-11801471",""),
D("Bélgica volta ao horário de inverno na noite de 24 para 25 de outubro",
 "Segundo a RTBF, os relógios recuam uma hora na madrugada de sábado para domingo: às 3h passa a ser 2h. O amanhecer fica uma hora mais cedo e o fim de tarde perde uma hora de luz. Se a UE não decidir o contrário, a próxima mudança é na noite de 27 para 28 de março de 2027.",
 "muda a rotina, e a diferença de horário para Brasília cai de 5 para 4 horas.",
 "RTBF","19/10/2026","https://www.rtbf.be/article/changement-d-heure-2026-la-belgique-basculera-a-l-heure-d-hiver-la-nuit-du-24-au-25-octobre-11801595",""),
]),
("Brasil", [
D("Quatro pesquisas dão vantagem a Flávio Bolsonaro no segundo turno",
 "Segundo a Exame, nos votos válidos, Flávio aparece à frente de Lula em todas: Futura 50,4% a 49,6%, BTG/Nexus 50,3% a 49,7%, AtlasIntel 51,1% a 48,9% e PoderData/Aya 52% a 48%. Em Futura e BTG/Nexus a diferença está dentro da margem de erro. Todas foram divulgadas na segunda (19/10); o segundo turno é domingo, 25/10.",
 "mostra uma disputa apertada a cinco dias da votação que define o presidente do seu país.",
 "Exame","19/10/2026","https://exame.com/brasil/pesquisa-para-presidente-hoje-veja-o-que-mostram-os-ultimos-levantamentos/",""),
D("Campanha de Lula vai pedir ao TSE a cassação da chapa de Flávio por “manipulação” da Meta (atualização)",
 "Segundo a Exame, que cita reportagem da Folha, a campanha de Lula alega que Meta e X usaram IA e ferramentas de recomendação para favorecer Flávio e aliados e reduzir o alcance de perfis pró-Lula. São alegações da campanha; a matéria não traz resposta da Meta nem da campanha de Flávio. O ministro Marco Aurélio Bellizze deu 24 horas para a Meta mostrar que não limita alcance, com multa diária de R$ 1 milhão.",
 "a disputa nas redes pode chegar à Justiça Eleitoral antes da votação.",
 "Exame","19/10/2026","https://exame.com/brasil/campanha-de-lula-vai-pedir-cassacao-da-chapa-de-flavio-devido-a-manipulacao-algoritmica-da-meta/",""),
D("Lula diz que entregará ao TSE seus sigilos bancário e telefônico e os dos filhos",
 "Segundo a Exame, Lula anunciou em Porto Alegre, na segunda (19/10), que formalizará na terça (20) a autorização ao TSE, na expectativa de que Flávio Bolsonaro faça o mesmo. O desafio foi lançado no debate da Band, no domingo, e Flávio não disse se aceita. A quebra oficial de sigilo exige ordem judicial, mas qualquer pessoa pode autorizar o acesso voluntariamente.",
 "o gesto entra na disputa de transparência da reta final.",
 "Exame","19/10/2026","https://exame.com/brasil/lula-vai-autorizar-tse-a-quebrar-seu-sigilo-e-de-seus-filhos/",""),
D("PF abre segundo inquérito sobre Flávio Bolsonaro por suspeita de lavagem de dinheiro",
 "Segundo a Exame, que confirmou reportagem do Estadão, o inquérito foi autorizado pelo STF em 8/10, com relatoria de Alexandre de Moraes. Apura suspeita de lavagem ligada ao advogado Willer Tomaz, amigo do senador e suposto controlador da Rede Loto, empresa de apostas. A campanha de Flávio não comentou; Tomaz diz que “amizade não é crime” e nega que o senador controlasse suas contas. É investigação, não condenação.",
 "um novo caso judicial pesa sobre um dos candidatos a poucos dias do segundo turno.",
 "Exame","19/10/2026","https://exame.com/brasil/pf-abre-2o-inquerito-sobre-flavio-bolsonaro-sobre-suspeita-de-lavagem-de-dinheiro/",""),
D("Senado não terá sessão e PEC da Segurança fica para depois das eleições (atualização)",
 "Segundo a CNN Brasil, o presidente do Senado, Davi Alcolumbre, não marcou sessões deliberativas nesta semana, e a votação da PEC da Segurança Pública foi adiada para depois do segundo turno. O impasse é a redução da maioridade penal: Rogério Marinho (PL) propõe baixar de 18 para 16 anos, e Camilo Santana (PT) propõe 16 anos só para crimes hediondos.",
 "a segurança pública é tema central da campanha e a decisão fica para o próximo governo.",
 "CNN Brasil","19/10/2026","https://www.cnnbrasil.com.br/politica/senado-nao-tera-sessao-nesta-semana-e-votacao-da-pec-da-seguranca-e-adiada/",""),
]),
("Tecnologia e IA", [
D("Microsoft lança “Guardian Agents” para vigiar agentes de IA nas empresas",
 "Segundo o TechCrunch, a Microsoft anunciou na segunda (19/10) novos recursos de segurança. O Defender passa a detectar até 60 tipos de agentes usados por funcionários, entre eles Claude Code e Codex, com controle de acesso e aprovação humana em decisões de risco. A executiva Hayete Gallot disse que modelos de fronteira “não podem ser confiáveis” por serem imprevisíveis, não por malícia. O texto lembra o possível conflito de interesse, pois a Microsoft investiu em OpenAI e Anthropic.",
 "mostra como as grandes empresas tentam controlar agentes de IA dentro das organizações.",
 "TechCrunch","19/10/2026","https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted/",""),
D("Anthropic e Nscale estariam perto de novo acordo de computação de US$ 45 bilhões",
 "Segundo o TechCrunch, que cita o Bloomberg e fontes anônimas, as negociações continuam e os detalhes podem mudar. As empresas anunciaram um acordo do mesmo valor pouco mais de um mês antes. Ambas buscam abrir capital; o Bloomberg diz que a Nscale enfrenta resistência de investidores à avaliação proposta de US$ 30 bilhões.",
 "indica o tamanho dos gastos em infraestrutura de IA, que alguns investidores veem com cautela.",
 "TechCrunch","19/10/2026","https://techcrunch.com/2026/10/19/nscale-and-anthropic-are-reportedly-in-talks-for-yet-another-45-billion-compute-deal/",""),
D("Noruega quer estender a idade mínima de 16 anos para jogos e aplicativos de mensagens",
 "Segundo o Euronews, o governo norueguês finaliza um projeto de lei com idade mínima de 16 anos para redes sociais, que também cobriria jogos e mensageiros considerados de risco, como Roblox, TikTok e Snapchat. As empresas ficariam responsáveis por verificar a idade. O projeto vai ao Parlamento até o fim do ano. A Dinamarca já adotou limites parecidos, e a Comissão Europeia propôs em setembro uma lei sobre o tema.",
 "o debate europeu sobre crianças e telas pode chegar às regras da Bélgica e da UE.",
 "Euronews","19/10/2026","https://www.euronews.com/2026/10/19/norway-to-extend-proposed-under-16-social-media-ban-to-online-games-and-messaging-apps",""),
D("Jensen Huang diz que a Alemanha fica para trás na IA; pacto com Merz é esperado em Berlim",
 "Segundo o Euronews, o presidente da Nvidia afirmou que o progresso europeu é travado por “hesitação e análise demais”. Ele e o chanceler Friedrich Merz devem apresentar um pacto de IA na cúpula Invest in Germany, com centenas de milhões de euros do governo, cerca de dez empresas, como Siemens e Audi, e a startup Black Forest Labs. A maior parte do dinheiro iria para computação na nuvem industrial da Deutsche Telekom.",
 "mostra a corrida europeia por IA própria.",
 "Euronews","19/10/2026","https://www.euronews.com/2026/10/19/nvidia-ceo-jensen-huang-warns-germany-is-falling-behind-in-ai-race",""),
]),
("Economia e mundo", [
D("Danos dos tumultos na França dobram, e bolsas e títulos reagem (atualização)",
 "Segundo o Euronews, ao menos 3.000 lojas foram danificadas no fim de semana, o dobro do número divulgado um dia antes. Na segunda, o CAC 40 caiu 1,1% e o Euro Stoxx 600, 0,9%; o rendimento do título francês de 10 anos subiu a 4,94%. O primeiro-ministro Sébastien Lecornu liberou o desemprego parcial financiado pelo Estado para empresas atingidas.",
 "a instabilidade no vizinho pesa nos mercados europeus e nas contas públicas francesas.",
 "Euronews","20/10/2026","https://www.euronews.com/2026/10/20/frances-riot-damage-doubles-who-will-pay-for-thousands-of-wrecked-shops",""),
D("Roche suspende investimentos na Alemanha após lei que eleva descontos de remédios",
 "Segundo o Euronews, o chefe da Roche Alemanha, Daniel Steiners, disse ao Die Welt que todas as futuras decisões de investimento no país foram suspensas. Desde uma lei aprovada em julho, as farmacêuticas devem dar desconto de 15,5% na maioria dos remédios de marca a partir do próximo ano, contra 7% hoje. O presidente da Siemens, Roland Busch, viu no anúncio um sinal de que empresas podem investir em outro lugar.",
 "a pressão sobre a indústria farmacêutica europeia interessa a uma região com forte presença do setor, como a da GSK.",
 "Euronews","20/10/2026","https://www.euronews.com/2026/10/20/why-pharma-giant-roche-is-putting-german-investments-on-hold",""),
D("Zelensky diz que EUA seguram mísseis antiaéreos; Trump sugere trocar o negociador",
 "Segundo a VRT NWS, Zelensky afirmou numa reunião online com senadores americanos que os mísseis Patriot estão prontos, mas sem aprovação para seguir à Ucrânia. Trump disse a jornalistas que talvez seja hora de Zelensky colocar outra pessoa para negociar, e acusou o ucraniano, numa publicação, de não querer acabar a guerra. As falas vêm de Zelensky e de Trump e não foram confirmadas de forma independente na matéria.",
 "o apoio dos EUA à Ucrânia pesa na segurança da Europa.",
 "VRT NWS","19/10/2026","https://www.vrt.be/vrtnws/nl/liveblog/vs-vertraagt-raketlevering-aan-oekraine-trump-haalt-uit-naar-ze~1789060001669/",""),
D("Dimon, do JPMorgan, lista cinco ameaças “sob a superfície” da economia americana",
 "Segundo a Fox Business, na divulgação do balanço, com lucro abaixo do esperado por analistas, Jamie Dimon citou déficits fiscais grandes, inflação persistente, preços de ativos elevados, juros em alta e condições geopolíticas. Ele disse que as forças “podem ser administráveis”. A matéria lembra a inflação de 3,7% em setembro e a possibilidade de nova alta de juros do Fed antes do fim do ano.",
 "juros e inflação nos EUA mexem com euro, dólar e crédito.",
 "Fox Business","19/10/2026","https://www.foxbusiness.com/economy/jamie-dimon-warns-5-economic-threats-lurking-under-surface",""),
]),
]
total = 1 + sum(len(s[1]) for s in secoes)
veic = {destaque['v']} | {i['v'] for s in secoes for i in s[1]}
print(total, len(veic), sorted(veic))
F = 'font-family:Arial,Helvetica,sans-serif;'
def card(i, bg="#FFFFFF", extra="", label=""):
    bl = f'border-left:4px solid #1F3A5F;' if label else ''
    lab = f'<p style="margin:0 0 6px 0;{F}font-size:11px;font-weight:bold;letter-spacing:1px;color:#1F3A5F;text-transform:uppercase;">Destaque</p>' if label else ''
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{bg}" style="margin:0 0 14px 0;"><tr><td bgcolor="{bg}" style="background-color:{bg};{bl}padding:16px 18px;">{lab}'
     f'<p style="margin:0 0 6px 0;{F}font-size:17px;line-height:1.35;font-weight:bold;color:#1F3A5F;"><a href="{E(i["l"])}" style="color:#1F3A5F;text-decoration:none;">{E(i["t"])}</a></p>'
     f'<p style="margin:0 0 8px 0;{F}font-size:14px;line-height:1.6;color:#222222;">{E(i["r"])}</p>'
     f'<p style="margin:0 0 8px 0;{F}font-size:14px;line-height:1.6;color:#222222;"><b>Por que importa:</b> {E(i["p"])}</p>'
     f'<p style="margin:0;{F}font-size:12px;line-height:1.5;color:#666666;">{E(i["v"])} · {i["d"]} · <a href="{E(i["l"])}" style="color:#1F3A5F;">Ler a matéria</a></p></td></tr></table>')
def sec(n): return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:10px 0 10px 0;"><tr><td style="border-top:2px solid #1F3A5F;padding-top:10px;{F}font-size:13px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:#1F3A5F;">{n}</td></tr></table>'
import sys
dur = sys.argv[1] if len(sys.argv) > 1 else ""
podcast = ""
if dur:
    podcast = (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#EEF2F7" style="margin:0 0 14px 0;"><tr><td bgcolor="#EEF2F7" style="background-color:#EEF2F7;padding:14px 18px;"><p style="margin:0 0 10px 0;{F}font-size:14px;color:#222222;"><b>Ouvir o resumo desta edição</b> · {dur} min, com Ana e Leo</p><table role="presentation" cellpadding="0" cellspacing="0" border="0" bgcolor="#1F3A5F"><tr><td bgcolor="#1F3A5F" style="background-color:#1F3A5F;padding:10px 18px;"><a href="https://bdiehlc-bit.github.io/digest-podcast/?ep=2026-10-20" style="{F}font-size:14px;font-weight:bold;color:#FFFFFF;text-decoration:none;">Ouvir agora</a></td></tr></table></td></tr></table>')
body = ('<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0;padding:0;background-color:#FFFFFF;">'
 '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF"><tr><td align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:16px 8px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:640px;"><tr><td>'
 f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#1F3A5F"><tr><td bgcolor="#1F3A5F" style="background-color:#1F3A5F;padding:20px 22px;"><p style="margin:0;{F}font-size:24px;font-weight:bold;color:#FFFFFF;">Digest Diário</p><p style="margin:4px 0 0 0;{F}font-size:14px;color:#FFFFFF;">Terça-feira, 20 de outubro de 2026</p></td></tr></table>'
 f'<p style="margin:14px 0 16px 0;{F}font-size:13px;color:#555555;">{total} notícias de {len(veic)} veículos · últimas 24 horas (19/10 06h47 a 20/10 06h47, horário de Bruxelas)</p>'
 + podcast + card(destaque, "#EEF2F7", label=True))
for n, its in secoes:
    body += sec(n) + "".join(card(i) for i in its)
body += (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:8px;"><tr><td style="border-top:1px solid #DDDDDD;padding-top:12px;{F}font-size:12px;line-height:1.5;color:#777777;">Montado automaticamente. Cada notícia foi conferida na fonte ou em segunda fonte. Ouça também no seu app de podcast: https://bdiehlc-bit.github.io/digest-podcast/feed.xml</td></tr></table></td></tr></table></td></tr></table></body></html>')
open("/home/user/digest-podcast/podcast/email.html", "w", encoding="utf-8").write(body)
print(len(body))
