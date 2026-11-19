import html,json
A="#1F3A5F"
def e(s): return html.escape(s,quote=True)
D={"t":"Crise federal: De Wever retoma conversas sobre o orçamento, mas sem o Vooruit (atualização)",
"r":"O primeiro-ministro recebeu separadamente os vice-primeiros-ministros Vincent Van Peteghem (CD&V), Maxime Prévot (Les Engagés) e David Clarinval (MR), mas não Frank Vandenbroucke (Vooruit), que vem criticando em público os parceiros desde o fracasso das negociações no domingo. Segundo a Belga, o clima na coalizão é pessimista e eleições antecipadas já não são descartadas se o governo cair; o rei deu a De Wever mais uma semana, e o Vooruit pede cerca de 750 milhões de euros em impostos extras, sobretudo sobre os mais ricos.",
"p":"Sem orçamento, a coalizão Arizona pode cair; o acordo final define impostos, benefícios e a indexação para quem vive na Bélgica.",
"v":"La Libre (Belga)","d":"18/11/2026","l":"https://www.lalibre.be/belgique/politique-belge/2026/11/18/crise-au-gouvernement-arizona-bart-de-wever-ecarte-vooruit-de-ses-discussions-FYRDB5RCQNB5RBSUWQNQMQTF3M/"}
S=[("Bélgica",[
{"t":"Reforma do desemprego: ministra admite que falta verba para os CPAS em novembro",
"r":"Anneleen Van Bossuyt (N-VA), ministra da Integração Social, reconheceu na Câmara que os recursos para os pagamentos de novembro da renda de integração são insuficientes, mas disse que um eventual atraso seria de alguns dias a duas semanas. O ajuste orçamentário de 2026 acrescenta 210 milhões de euros aos 300 milhões já previstos; a Valônia fica com 53% da compensação.",
"p":"Com o seguro-desemprego limitado no tempo, mais gente recorre aos CPAS, sobretudo na Valônia e em Bruxelas.",
"v":"RTBF","d":"18/11/2026","l":"https://www.rtbf.be/article/reforme-du-chomage-la-ministre-reconnait-des-moyens-insuffisants-pour-les-cpas-mais-se-veut-rassurante-sur-les-paiements-11817387"},
{"t":"Associação de magistrados pede a demissão da ministra da Justiça, Annelies Verlinden (atualização)",
"r":"Verlinden é alvo de investigação por suposto conflito de interesses no projeto i-Police, contrato que assinou com a Sopra Steria em 2021, quando era ministra do Interior. Para a Associação Sindical dos Magistrados, a permanência dela no cargo ficou difícil de conciliar com independência e imparcialidade; a ministra nega irregularidades, é presumida inocente e se recusa a renunciar.",
"p":"Uma ministra da Justiça investigada no cargo é inédita e aumenta a pressão sobre um governo já em crise.",
"v":"La Libre","d":"18/11/2026","l":"https://www.lalibre.be/belgique/judiciaire/2026/11/18/i-police-lassociation-syndicale-des-magistrats-asm-reclame-la-demission-dannelies-verlinden-6RXTYIMXUJEAVCHAFAHVNT3X3Q/"},
{"t":"Defesa registrou mais de 9.300 perdas e roubos de material militar em cinco anos",
"r":"Em resposta parlamentar, o ministro Theo Francken (N-VA) informou 9.029 casos de perda e 351 de roubo entre 2021 e 2025, a maioria de roupa e equipamento pessoal, mas também armas, como um fuzil Barrett .50 perdido em 2025. A Defesa prevê etiquetas eletrônicas RFID para paraquedas e armas leves.",
"p":"Mostra falhas de controle num momento de forte aumento dos gastos militares belgas.",
"v":"La Libre","d":"19/11/2026","l":"https://www.lalibre.be/belgique/politique-belge/2026/11/19/des-armes-des-munitions-de-lequipement-plus-de-9-300-pertes-et-vols-de-materiel-militaire-enregistres-a-la-defense-en-cinq-ans-V5QNAMT2TBGB5KDONHMRO7ILPA/"},
{"t":"Francken e Quintin perto de acordo para criar uma “gendarmaria 2.0”",
"r":"Os gabinetes da Defesa e do Interior quase fecharam o princípio de uma unidade com formação policial e militar, de cerca de cem militares, com até 400 membros da Defesa envolvidos no projeto. Francken lançou a ideia após tumultos em manifestações em Bruxelas e Liège; equipamento e organização ainda estão em discussão.",
"p":"Pode mudar o papel do Exército na segurança interna, de estações de metrô a centrais nucleares.",
"v":"La Libre (Belga)","d":"18/11/2026","l":"https://www.lalibre.be/belgique/politique-belge/2026/11/18/theo-francken-et-bernard-quintin-proches-dun-accord-pour-creer-une-gendarmerie-20-JDMCPOEQGVBUHJ3PN46A4F3RIQ/"},
{"t":"SNCB vai abrir a passageiros trens que hoje circulam vazios",
"r":"A partir de 13 de dezembro, com a nova grade horária, a SNCB acrescenta 24 viagens em dias úteis (13 de manhã e 11 à noite) com trens que hoje saem ou voltam vazios do depósito, permitindo partidas mais cedo e mais tarde em algumas linhas. Até 2029, a oferta deve crescer 3% em relação a 2026.",
"p":"Mais horários no início e no fim do dia para quem depende do trem para trabalhar.",
"v":"RTBF","d":"18/11/2026","l":"https://www.rtbf.be/article/pourquoi-la-sncb-va-desormais-ouvrir-aux-voyageurs-certains-trains-qui-circulaient-a-vide-11817367"}]),
("Brasil",[
{"t":"Senado conclui votação do pacote fiscal e texto vai à Câmara (atualização)",
"r":"O projeto foi aprovado por 69 a 2 em turno suplementar, e os destaques da oposição foram rejeitados. Acordo sobre a Lei Kandir elevou os repasses aos estados de R$ 1 bilhão para R$ 2 bilhões por ano entre 2027 e 2030; segundo o relator Eduardo Braga, o ganho fiscal para 2027 caiu de R$ 56 bilhões para R$ 50 bilhões com as mudanças.",
"p":"É a principal aposta do governo Lula para as contas de 2027 e pesa sobre juros e câmbio.",
"v":"Exame","d":"18/11/2026","l":"https://exame.com/brasil/senado-aprova-pacote-fiscal-apresentado-pelo-governo-lula-texto-vai-a-camara/"},
{"t":"Fachin envia à PGR relatórios da PF que citam ministros do STF no caso Master (atualização)",
"r":"Após reunião com o diretor-geral da PF, Andrei Rodrigues, o presidente do STF disse que a Procuradoria-Geral da República terá 15 dias para se manifestar, e o material segue sob sigilo. Segundo a CNN Brasil, as investigações mencionam ao menos seis ministros do STF e dois do STJ; ser citado não indica, por si só, irregularidade.",
"p":"Abrir investigação contra ministros exigiria votação do plenário do STF, um passo sem precedente recente.",
"v":"CNN Brasil","d":"18/11/2026","l":"https://www.cnnbrasil.com.br/politica/fachin-diz-que-relatorios-da-pf-sobre-ministros-do-stf-serao-enviados-a-pgr/"},
{"t":"PGR denuncia Flávio Bolsonaro por calúnia contra Lula",
"r":"A denúncia, enviada ao ministro Alexandre de Moraes, trata de uma publicação no X de janeiro de 2026 que atribuía a Lula crimes como tráfico e lavagem de dinheiro. Para a subprocuradora Luiza Frischeisen, a imunidade parlamentar não cobre a conduta; a PGR admite oferecer um acordo de não persecução penal.",
"p":"Abre mais uma frente judicial entre o clã Bolsonaro e o governo.",
"v":"Exame","d":"18/11/2026","l":"https://exame.com/brasil/pgr-denuncia-flavio-bolsonaro-por-suposta-calunia-contra-lula-apos-publicacao-nas-redes-sociais/"},
{"t":"Lula assina nesta quinta o decreto que regulamenta o fim da escala 6x1 (atualização)",
"r":"A cerimônia está marcada para 19 de novembro no Planalto; a jornada cai de 44 para 42 horas semanais, com duas folgas e sem corte salarial, a partir de 16 de dezembro, e as 40 horas valem em dezembro de 2027. A CNI estima impacto de R$ 11 bilhões na indústria, e o STF deve levar o tema ao plenário.",
"p":"Muda a rotina de milhões de trabalhadores e os custos das empresas.",
"v":"CNN Brasil","d":"19/11/2026","l":"https://www.cnnbrasil.com.br/politica/governo-assina-hoje-decreto-que-regulamenta-fim-da-escala-de-trabalho-6x1/"},
{"t":"Lula avalia Bruno Moretti para o Ministério da Fazenda",
"r":"Segundo a CNN Brasil, o presidente elogia a atuação do ministro do Planejamento na aprovação do pacote fiscal no Senado; o atual ministro, Dario Durigan, enfrentaria resistências no Planalto. A reportagem não afirma que haverá troca.",
"p":"Uma mudança no comando da Fazenda mexeria com as expectativas do mercado.",
"v":"CNN Brasil","d":"18/11/2026","l":"https://www.cnnbrasil.com.br/politica/com-aprovacao-de-pacote-fiscal-lula-avalia-moretti-para-a-fazenda/"}]),
("Tecnologia e IA",[
{"t":"Anthropic fixa preço da abertura de capital em US$ 83 por ação, acima do previsto",
"r":"O preço ficou acima da faixa de US$ 70 a US$ 78, e a empresa estreia nesta quinta na Nasdaq com o código ANT, avaliada em cerca de US$ 1,5 trilhão, segundo o TechCrunch.",
"p":"É a maior estreia de uma empresa de IA na bolsa e um teste para o apetite dos investidores pelo setor.",
"v":"TechCrunch","d":"18/11/2026","l":"https://techcrunch.com/2026/11/18/anthropic-reportedly-prices-ipo-at-83-a-share-above-projected-range/"},
{"t":"Bancos americanos dizem que cliente responde pelo que agentes de IA fizerem na conta",
"r":"O Citi atualizou seu contrato para dizer que quem der acesso a agentes de IA de terceiros é responsável pelo que eles fizerem, mesmo após vazamento de credenciais; JPMorgan, Bank of America, PNC e Citizens adotaram regras parecidas.",
"p":"Sinaliza como o risco de usar assistentes de IA em finanças pessoais tende a ficar com o usuário.",
"v":"TechCrunch","d":"18/11/2026","l":"https://techcrunch.com/2026/11/18/more-banks-says-customers-using-ai-agents-are-on-their-own-even-if-they-get-hacked/"},
{"t":"Modo IA da busca do Google ganha conversas temporárias",
"r":"As “temporary threads” ficam desvinculadas da conta, não entram no histórico de pesquisa nem influenciam recomendações. O recurso chega a todos os idiomas suportados, no computador e no celular.",
"p":"Opção de privacidade para quem usa a busca com IA, inclusive na Bélgica.",
"v":"TechCrunch","d":"18/11/2026","l":"https://techcrunch.com/2026/11/18/googles-ai-feature-in-search-gets-its-own-incognito-mode/"}]),
("Economia e mundo",[
{"t":"Xi, Trump e Putin fazem reunião trilateral inédita em Shenzhen",
"r":"Os três líderes se reúnem à margem da cúpula da APEC, na China, com desnuclearização e a guerra com o Irã na pauta; segundo a Euronews, a Ucrânia não está entre os temas. Logo depois, os enviados americanos Kushner e Witkoff vão a Berlim para reunião com ucranianos e aliados europeus.",
"p":"Decisões entre as três potências podem redesenhar a segurança europeia sem a Europa à mesa.",
"v":"Euronews","d":"19/11/2026","l":"https://www.euronews.com/2026/11/19/europe-today-xi-trump-and-putin-together-in-a-historic-trilateral-meeting"},
{"t":"Irã ataca base americana no Kuwait após ofensiva dos EUA",
"r":"Segundo a mídia estatal iraniana, citada pela Fox News, o Irã mirou drones e mísseis americanos na base de Ali Al Salem; o Exército do Kuwait disse ter interceptado ataques de drones, e o Bahrein relatou novas interceptações. Foi a resposta ao ataque dos EUA a uma base de mísseis da Guarda Revolucionária na ilha de Qeshm.",
"p":"A escalada no Golfo ameaça o preço do petróleo e da energia na Europa.",
"v":"Fox News","d":"18/11/2026","l":"https://www.foxnews.com/world/iran-targets-us-air-base-kuwait-us-defensive-strikes-criticism-gulf-states"},
{"t":"BCE compara boom da IA à bolha das pontocom",
"r":"No Relatório de Estabilidade Financeira, o Banco Central Europeu alertou que a onda de aberturas de capital pode indicar euforia de fim de ciclo e que o endividamento das big techs deixa os mercados expostos a uma queda brusca, sem chamar a IA de bolha. Ações de tecnologia e IA americanas representam de 16% a 26% dos investimentos em ações de não bancos da zona do euro.",
"p":"Uma correção nas bolsas atingiria fundos e poupanças de europeus.",
"v":"Euronews","d":"18/11/2026","l":"https://www.euronews.com/2026/11/18/ecb-draws-parallels-between-ai-boom-and-dotcom-bubble-as-tech-giants-pile-on-debt"},
{"t":"Inflação britânica sobe para 3,6% com alta dos combustíveis",
"r":"Os preços de combustíveis subiram 33,2% em um ano em outubro, e o diesel bateu recorde; o núcleo da inflação ficou em 2,8%. O Banco da Inglaterra subiu os juros para 4% no início de novembro e prevê inflação perto de 5% em meados de 2027.",
"p":"Mostra o choque de energia que também pressiona o custo de vida na zona do euro.",
"v":"Euronews","d":"18/11/2026","l":"https://www.euronews.com/2026/11/18/uk-inflation-rises-to-36-as-petrol-and-diesel-prices-climb"}])]
P='<p style="margin:0 0 8px 0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.6;color:#222222;">'
def body(n):
    return (f'<p style="margin:0 0 6px 0;font-family:Arial,Helvetica,sans-serif;font-size:17px;line-height:1.35;font-weight:bold;color:{A};"><a href="{e(n["l"])}" style="color:{A};text-decoration:none;">{e(n["t"])}</a></p>'
     f'{P}{e(n["r"])}</p>{P}<b>Por que importa:</b> {e(n["p"])}</p>'
     f'<p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.5;color:#666666;">{e(n["v"])} · {n["d"]} · <a href="{e(n["l"])}" style="color:{A};">Ler a matéria</a></p>')
n=1+sum(len(x) for _,x in S)
h=['<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0;padding:0;background-color:#FFFFFF;">',
'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF"><tr><td align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:16px 8px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:640px;"><tr><td>',
f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{A}"><tr><td bgcolor="{A}" style="background-color:{A};padding:20px 22px;"><p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:24px;font-weight:bold;color:#FFFFFF;">Digest Diário</p><p style="margin:4px 0 0 0;font-family:Arial,Helvetica,sans-serif;font-size:14px;color:#FFFFFF;">Quinta-feira, 19 de novembro de 2026</p></td></tr></table>',
f'<p style="margin:14px 0 16px 0;font-family:Arial,Helvetica,sans-serif;font-size:13px;color:#555555;">{n} notícias de 7 veículos · últimas 24 horas (18/11 09h16 a 19/11 09h16, horário de Bruxelas)</p>',
f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#EEF2F7" style="margin:0 0 14px 0;"><tr><td bgcolor="#EEF2F7" style="background-color:#EEF2F7;padding:14px 18px;"><p style="margin:0 0 10px 0;font-family:Arial,Helvetica,sans-serif;font-size:14px;color:#222222;"><b>Ouvir o resumo desta edição</b> · 5:05 min, com Ana e Leo</p><table role="presentation" cellpadding="0" cellspacing="0" border="0" bgcolor="{A}"><tr><td bgcolor="{A}" style="background-color:{A};padding:10px 18px;"><a href="https://bdiehlc-bit.github.io/digest-podcast/?ep=2026-11-19" style="font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#FFFFFF;text-decoration:none;">Ouvir agora</a></td></tr></table></td></tr></table>',
f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#EEF2F7" style="margin:0 0 14px 0;"><tr><td bgcolor="#EEF2F7" style="background-color:#EEF2F7;border-left:4px solid {A};padding:16px 18px;"><p style="margin:0 0 6px 0;font-family:Arial,Helvetica,sans-serif;font-size:11px;font-weight:bold;letter-spacing:1px;color:{A};text-transform:uppercase;">Destaque</p>{body(D)}</td></tr></table>']
for name,items in S:
    h.append(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:10px 0 10px 0;"><tr><td style="border-top:2px solid {A};padding-top:10px;font-family:Arial,Helvetica,sans-serif;font-size:13px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:{A};">{name}</td></tr></table>')
    for it in items:
        h.append(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="margin:0 0 14px 0;"><tr><td bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:16px 18px;">{body(it)}</td></tr></table>')
h.append('<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:8px;"><tr><td style="border-top:1px solid #DDDDDD;padding-top:12px;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.5;color:#777777;">Montado automaticamente. Cada notícia foi conferida na fonte ou em segunda fonte. Ouça também no seu app de podcast: https://bdiehlc-bit.github.io/digest-podcast/feed.xml</td></tr></table>')
h.append('</td></tr></table></td></tr></table></body></html>')
open('/home/user/digest-podcast/podcast/email.html','w',encoding='utf-8').write('\n'.join(h))
print(n, len('\n'.join(h)))
