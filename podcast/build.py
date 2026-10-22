import json, html
D=lambda s:s
items=[
# (secao, titulo, resumo, porque, veiculo, data, link)
("Bélgica","Governo federal encerra reunião sem acordo orçamentário (atualização)",
 "O núcleo do governo De Wever se reuniu na quarta-feira à noite e terminou sem acordo. O objetivo continua sendo achar 10 bilhões de euros. Segundo a VRT NWS, o vice-premiê Vandenbroucke, do Vooruit, rejeitou fechar tudo numa noite e o partido considera as propostas atuais injustas. O prazo final é o fim de dezembro e uma alta geral do IVA saiu da última proposta.",
 "O orçamento define impostos, serviços e pensões que afetam quem vive na Bélgica; o impasse já pesa nos juros do país.",
 "VRT NWS","21/10/2026","https://www.vrt.be/vrtnws/nl/liveblog/kernkabinet-uiteen-zonder-begrotingsakkoord-het-zal-in-de-bles~1790599460224/","Governo sem acordo no orçamento",
 "O núcleo do governo federal se reuniu na quarta à noite e terminou sem acordo. A meta segue sendo encontrar dez bilhões de euros. O vice-premiê Vandenbroucke, do Vooruit, recusou fechar tudo numa noite só. O prazo final é o fim de dezembro, e uma alta geral do IVA saiu da última proposta."),
("Bélgica","Três sindicatos convocam nova manifestação nacional em Bruxelas, em 23 de novembro",
 "CSC, FGTB e Synova anunciaram na quarta-feira o novo protesto, dizendo que o ajuste das contas públicas não deve recair de novo sobre os trabalhadores. A manifestação nacional anterior, em 9 de outubro, teve violência importante.",
 "Protestos grandes em Bruxelas podem afetar transporte e circulação no dia.",
 "RTBF","21/10/2026","https://www.rtbf.be/article/les-trois-syndicats-appellent-a-une-nouvelle-manifestation-nationale-a-bruxelles-le-23-novembre-11803807","Sindicatos marcam protesto de 23 de novembro",
 "Os três sindicatos principais convocaram um novo protesto nacional em Bruxelas, no dia vinte e três de novembro. Eles dizem que o ajuste das contas não pode recair de novo sobre os trabalhadores. O protesto anterior, em nove de outubro, teve muita violência."),
("Bélgica","Comerciantes de Bruxelas temem novos saques no fim de semana",
 "Lojistas da rue Neuve estão protegendo vitrines diante de um possível ato no sábado 24, convocado por chamadas anônimas nas redes. Segundo a La Libre, o gabinete do prefeito diz que não há pedido oficial de manifestação. No fim de semana anterior, lojas Nike e JD Sports foram vandalizadas e saqueadas, com 19 suspeitos presos, 8 deles menores.",
 "Afeta quem circula pelo centro de Bruxelas no sábado.",
 "La Libre","22/10/2026","https://www.lalibre.be/belgique/societe/2026/10/22/ils-veulent-tout-casser-les-commercants-bruxellois-craignent-de-nouveaux-pillages-ce-week-end-VTXXPFZEM5AMVFQDEGJFFYDH7I/","Comerciantes temem novos saques",
 "Lojistas da rue Neuve, em Bruxelas, estão protegendo as vitrines por causa de um possível ato no sábado. Circulam chamadas anônimas nas redes, mas a prefeitura diz que não há pedido oficial. No fim de semana anterior, lojas foram saqueadas e dezenove suspeitos foram presos."),
("Bélgica","Falha no PHP tira do ar sites da polícia federal, do governo flamengo e do SPF Finances",
 "Dois defeitos críticos na linguagem PHP levaram sites a saírem do ar por precaução na quarta-feira. O Centro de Cibersegurança (CCB) disse não ter registrado ataques a sites belgas e recomendou instalar a correção ou desligar o site. A polícia federal lembrou que o 101 segue ativo para urgências.",
 "Serviços públicos online podem ter ficado instáveis; o aviso do CCB vale para quem mantém sites.",
 "RTBF","21/10/2026","https://www.rtbf.be/article/une-faille-informatique-mondiale-un-correctif-visant-a-mettre-fin-a-la-vulnerabilite-dans-php-a-ete-publie-11803667","Falha no PHP derruba sites belgas",
 "Duas falhas graves na linguagem PHP tiraram do ar sites como o da polícia federal e do SPF Finances. O centro belga de cibersegurança diz que não viu ataques no país e pede que todos instalem a correção. Para urgências policiais, o número cento e um continua funcionando."),
("Bélgica","700 mil famílias pagam a mais por luz e gás, diz regulador",
 "Segundo os números da CREG, 700 mil famílias pagam em média 700 euros por ano a mais. A VRT NWS lista quatro passos: conferir a fatura, fazer o scan da CREG, comparar na V-test (ou Brusim, em Bruxelas) e só então trocar, atentando a multas de rescisão. Descontos \"sjoemel\" estão proibidos desde outubro, mas podem valer em contratos antigos.",
 "Com o inverno e a pressão no preço da energia, rever o contrato pode economizar bastante.",
 "VRT NWS","21/10/2026","https://www.vrt.be/vrtnws/nl/2026/10/21/energiecontract-elektriciteit-gas-prijs-v-test-creg-scan/","Famílias pagam a mais por energia",
 "Setecentas mil famílias belgas pagam em média setecentos euros por ano a mais por luz e gás, segundo o regulador. A dica é conferir a fatura, usar o simulador da CREG e comparar ofertas antes de trocar de contrato. Atenção a multas de rescisão."),
("Bélgica","Quase metade das compras da Defesa beneficia a economia belga",
 "De 2021 a meados de 2026, a Defesa gastou 24,2 bilhões de euros em contratações; 11,4 bilhões (47,2%) foram para atores econômicos belgas. Segundo a La Libre, a oposição, exceto o Défi, acusa o ministro Theo Francken de favorecer o mercado americano, o que ele nega.",
 "Mostra quanto do aumento do gasto militar volta para a economia local.",
 "La Libre","21/10/2026","https://www.lalibre.be/belgique/politique-belge/2026/10/21/pres-de-la-moitie-des-investissements-consentis-par-la-defense-profite-a-leconomie-belge-NDOI2ZVFU5DX3NXU2RUMTDPBRM/","Compras da Defesa e economia belga",
 "Desde dois mil e vinte e um, a Defesa belga fez mais de vinte e quatro bilhões de euros em compras. Quase metade foi para empresas belgas. A oposição acusa o ministro Francken de favorecer os Estados Unidos, o que ele nega."),
("Brasil","Campanha de Lula pede ao TSE a cassação da chapa de Flávio Bolsonaro",
 "Na quarta-feira, a campanha de Lula pediu ao TSE a cassação da chapa de Flávio e de Alfredo Gaspar por suposto abuso de poder econômico e uso indevido de meios de comunicação, além de oito anos de inelegibilidade para Flávio. O argumento é que Meta e X favoreceriam Flávio; o pedido cita estudo do Instituto Democracia em Xeque. A relatoria ficou com o ministro Ricardo Villas Bôas Cueva.",
 "A quatro dias do segundo turno, é uma acusação da campanha, ainda sem decisão.",
 "O Antagonista","21/10/2026","https://oantagonista.com.br/brasil/campanha-de-lula-pede-cassacao-da-chapa-de-flavio-por-abuso-de-poder-economico/","Lula pede cassação da chapa de Flávio",
 "A campanha de Lula pediu ao TSE a cassação da chapa de Flávio Bolsonaro, por suposto abuso de poder econômico. O argumento é que redes como Meta e X favoreceriam Flávio. É uma acusação da campanha, ainda sem decisão."),
("Brasil","Lula aceita condições de Flávio para abrir sigilos, mas cobra dados de empresa ligada a Willer Tomaz",
 "Segundo a Exame, a campanha de Lula diz aceitar abrir sigilos bancário, telefônico e fiscal dos candidatos e aliados, desde que Flávio também libere dados da Alcazar Holdings, empresa de Willer Tomaz. A campanha cita documentos da PF que, segundo ela, apontam Flávio como usuário de conta da empresa. Flávio e Tomaz negam sociedade. O prazo dado vai até as 11h de quinta-feira.",
 "O embate sobre sigilos domina a reta final do segundo turno.",
 "Exame","21/10/2026","https://exame.com/brasil/lula-aceita-condicoes-de-flavio-para-abrir-sigilos-mas-cobra-dados-de-empresa-ligada-a-willer-tomaz/","Embate sobre sigilos",
 "A campanha de Lula diz aceitar abrir os sigilos de candidatos e aliados, mas cobra que Flávio libere também dados de uma empresa ligada a Willer Tomaz. Flávio e Tomaz negam qualquer sociedade."),
("Brasil","Quaest: Flávio 45%, Lula 44% no segundo turno, empate técnico",
 "A pesquisa Quaest, feita de 17 a 20 de outubro com 2.154 pessoas e margem de 2 pontos, mostra Flávio com 45% e Lula com 44%. A rejeição a Lula caiu de 53% para 47%; a de Flávio foi de 54% para 52%.",
 "É o retrato mais recente da disputa que decide a Presidência no domingo, 25.",
 "Exame","21/10/2026","https://exame.com/brasil/pesquisa-para-presidente-quaest-flavio-bolsonaro-tem-45-e-lula-44-a-4-dias-do-2o-turno/","Pesquisa Quaest empate técnico",
 "A pesquisa Quaest mostra Flávio com quarenta e cinco por cento e Lula com quarenta e quatro, um empate técnico. A rejeição a Lula caiu para quarenta e sete por cento."),
("Brasil","Lula sanciona lei que perdoa dívidas de MEIs e eleva o teto de faturamento",
 "A lei cancela R$ 15,5 bilhões devidos à União por 3,6 milhões de microempreendedores e eleva o teto anual de R$ 81 mil para R$ 110 mil em 2027 e R$ 140 mil em 2028. Cria também o Pix MEI, com R$ 5 mil de capital inicial entre 2027 e 2030.",
 "Medida de grande alcance entre os pequenos empreendedores brasileiros.",
 "CNN Brasil","21/10/2026","https://www.cnnbrasil.com.br/politica/lula-sanciona-lei-que-perdoa-dividas-e-aumenta-teto-de-faturamento-de-meis/","Lei do MEI sancionada",
 "Lula sancionou a lei que perdoa quinze bilhões e meio de reais em dívidas de microempreendedores e eleva o teto de faturamento anual."),
("Brasil","Lula envia ao Congresso PEC da tarifa zero no transporte nos fins de semana",
 "A PEC reserva no mínimo 26,8% das emendas individuais e de bancada obrigatórias; o governo estima impacto de cerca de R$ 10 bilhões. Ainda precisa passar por comissões e duas votações em cada Casa.",
 "Proposta de peso eleitoral, ainda longe de virar realidade.",
 "CNN Brasil","21/10/2026","https://www.cnnbrasil.com.br/politica/lula-envia-ao-congresso-pec-da-tarifa-zero-no-transporte-em-fins-de-semana/","PEC da tarifa zero nos fins de semana",
 "Lula enviou ao Congresso uma proposta de transporte público gratuito aos fins de semana. O custo estimado é de cerca de dez bilhões de reais, e ela ainda precisa ser votada."),
("Tecnologia e IA","Falhas no PHP achadas por IA: NSA manda tirar do ar sites sem correção",
 "Dois defeitos críticos presentes desde o PHP 5 foram descobertos com ferramentas de IA, pela Calif (iniciativa Patch the Planet, da OpenAI) e pela Wiz. A NSA recomenda desligar sites que não possam ser corrigidos de imediato; a atualização recomendada é o PHP 8.5.12. A OpenAI diz não haver exploração em andamento.",
 "Mostra a IA achando falhas antigas em escala, e explica a queda de sites belgas.",
 "TechCrunch","21/10/2026","https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet/","Falhas no PHP achadas por IA",
 "As duas falhas no PHP foram achadas com ajuda de inteligência artificial. A agência americana NSA recomenda tirar do ar sites que não puderem ser corrigidos já. A OpenAI diz que não há ataques conhecidos."),
("Tecnologia e IA","Meta diz que app de IA Muse passou de 10 milhões de usuários",
 "Na teleconferência de resultados, a Meta afirmou que cerca de um quarto dos cadastrados usa o app diariamente e que compras são uma das principais atividades. Zuckerberg espera que o Muse renda \"centenas de dólares\" por usuário por ano.",
 "Indica como as big techs tentam monetizar assistentes de IA.",
 "TechCrunch","21/10/2026","https://techcrunch.com/2026/10/21/meta-says-muse-has-over-10m-users-with-shopping-a-top-activity/","Meta Muse passa de 10 milhões",
 "A Meta disse que seu aplicativo de IA, o Muse, passou de dez milhões de usuários. Compras são uma das atividades principais."),
("Tecnologia e IA","Trump pede que empresas de data centers paguem \"dividendo\" às comunidades",
 "Em post na Truth Social, Trump disse que acordos financeiros tornam esses projetos populares. Segundo a Euronews, ao menos 47 grandes projetos foram atrasados em 2026 e mais de mil comunidades americanas pediram restrições.",
 "A resistência local a data centers pode afetar o ritmo e o custo da expansão da IA.",
 "Euronews","21/10/2026","https://www.euronews.com/2026/10/21/trump-tells-companies-to-pay-dividend-to-communities-to-make-data-centres-popular","Trump e dividendo de data centers",
 "Trump pediu que empresas de data centers paguem um dividendo às comunidades vizinhas. Muitos projetos têm sido atrasados por oposição local."),
("Economia e mundo","Juro do título francês de 10 anos passa de 5%, primeira vez desde 2002",
 "Segundo a Euronews, o diferencial sobre o título alemão chegou perto de 160 pontos-base. A dívida francesa é de cerca de 120% do PIB, e a Moody's decide sobre a nota do país na sexta-feira, com rebaixamento esperado por a maioria dos economistas.",
 "Tensão na dívida francesa pesa sobre o euro e sobre o crédito na Europa.",
 "Euronews","21/10/2026","https://www.euronews.com/2026/10/21/french-government-10-year-bond-yield-tops-5-for-first-time-since-2002","Juros da França acima de 5%",
 "O juro dos títulos franceses de dez anos passou de cinco por cento, o maior nível desde dois mil e dois. A agência Moody's decide sobre a nota da França na sexta."),
("Economia e mundo","Dívida da zona do euro sobe a 88,8% do PIB",
 "Dados da Eurostat para abril a junho de 2026: Grécia 140,8%, Itália 139,9% e França 119,1%. Os governos da zona do euro devem cerca de 14,4 trilhões de euros.",
 "A Itália está perto de ultrapassar a Grécia como país mais endividado.",
 "Euronews","21/10/2026","https://www.euronews.com/2026/10/21/eurozone-government-debt-climbs-to-888-of-gdp-as-italy-closes-in-on-greece","Dívida da zona do euro",
 "A dívida dos governos da zona do euro subiu para oitenta e oito vírgula oito por cento do PIB. A Itália está quase alcançando a Grécia."),
("Economia e mundo","UE avalia cortes de demanda de energia; ministros se reúnem em 29 de outubro",
 "A proposta é da Irlanda, que preside o Conselho. Segundo a Euronews, o gás subiu 140% desde o ataque de EUA e Israel ao Irã, o Brent está em US$ 110 e os estoques de gás da UE estão em 74%, o menor nível desde 2011.",
 "Pode se traduzir em contas de energia mais altas neste inverno.",
 "Euronews","21/10/2026","https://www.euronews.com/2026/10/21/europe-weighs-energy-saving-measures-as-middle-east-crisis-deepens","UE avalia cortes de energia",
 "Ministros de energia da União Europeia se reúnem em vinte e nove de outubro para discutir cortes de demanda. O gás está muito mais caro e os estoques estão no menor nível desde dois mil e onze."),
("Economia e mundo","Rússia liberta americano preso por lutar pela Ucrânia após pedido de Trump",
 "Segundo a Fox News, Stephen Hubbard, de Michigan, condenado em 2024 a quase sete anos, foi solto depois que Trump tratou do caso com Putin por telefone. Trump diz que os EUA não deram nada em troca.",
 "Sinal sobre a relação EUA–Rússia no debate da paz na Ucrânia.",
 "Fox News","21/10/2026","https://www.foxnews.com/world/stephen-hubbard-russia-american-prisoner-release","Rússia liberta americano",
 "A Rússia libertou o americano Stephen Hubbard, preso por lutar pela Ucrânia, depois de Trump falar com Putin. Trump diz que não houve troca."),
]
B="Arial,Helvetica,sans-serif"
def e(s): return html.escape(s,quote=True)
def card(it,dest=False):
    sec,t,r,p,v,d,l=it[:7]
    lab='<p style="margin:0 0 6px 0;font-family:%s;font-size:11px;font-weight:bold;letter-spacing:1px;color:#1F3A5F;text-transform:uppercase;">Destaque</p>'%B if dest else ''
    inner=f'{lab}<p style="margin:0 0 6px 0;font-family:{B};font-size:17px;line-height:1.35;font-weight:bold;color:#1F3A5F;"><a href="{e(l)}" style="color:#1F3A5F;text-decoration:none;">{e(t)}</a></p><p style="margin:0 0 8px 0;font-family:{B};font-size:14px;line-height:1.6;color:#222222;">{e(r)}</p><p style="margin:0 0 8px 0;font-family:{B};font-size:14px;line-height:1.6;color:#222222;"><b>Por que importa:</b> {e(p)}</p><p style="margin:0;font-family:{B};font-size:12px;line-height:1.5;color:#666666;">{e(v)} · {d} · <a href="{e(l)}" style="color:#1F3A5F;">Ler a matéria</a></p>'
    if dest:
        return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#EEF2F7" style="margin:0 0 14px 0;"><tr><td bgcolor="#EEF2F7" style="background-color:#EEF2F7;border-left:4px solid #1F3A5F;padding:16px 18px;">{inner}</td></tr></table>'
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="margin:0 0 14px 0;"><tr><td bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:16px 18px;">{inner}</td></tr></table>'
def sec(s): return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:10px 0 10px 0;"><tr><td style="border-top:2px solid #1F3A5F;padding-top:10px;font-family:{B};font-size:13px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:#1F3A5F;">{s}</td></tr></table>'
import sys
dur=sys.argv[1] if len(sys.argv)>1 else None
body=card(items[0],True); cur=None
for it in items[1:]:
    if it[0]!=cur: cur=it[0]; body+=sec(cur)
    body+=card(it)
pod=''
if dur:
    pod=f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#EEF2F7" style="margin:0 0 14px 0;"><tr><td bgcolor="#EEF2F7" style="background-color:#EEF2F7;padding:14px 18px;"><p style="margin:0 0 10px 0;font-family:{B};font-size:14px;color:#222222;"><b>Ouvir o resumo desta edição</b> · {dur} min, com Ana e Leo</p><table role="presentation" cellpadding="0" cellspacing="0" border="0" bgcolor="#1F3A5F"><tr><td bgcolor="#1F3A5F" style="background-color:#1F3A5F;padding:10px 18px;"><a href="https://bdiehlc-bit.github.io/digest-podcast/?ep=2026-10-22" style="font-family:{B};font-size:14px;font-weight:bold;color:#FFFFFF;text-decoration:none;">Ouvir agora</a></td></tr></table></td></tr></table>'
veic=len({i[4] for i in items})
out=f'''<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0;padding:0;background-color:#FFFFFF;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF"><tr><td align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:16px 8px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:640px;"><tr><td>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#1F3A5F"><tr><td bgcolor="#1F3A5F" style="background-color:#1F3A5F;padding:20px 22px;"><p style="margin:0;font-family:{B};font-size:24px;font-weight:bold;color:#FFFFFF;">Digest Diário</p><p style="margin:4px 0 0 0;font-family:{B};font-size:14px;color:#FFFFFF;">Quinta-feira, 22 de outubro de 2026</p></td></tr></table>
<p style="margin:14px 0 16px 0;font-family:{B};font-size:13px;color:#555555;">{len(items)} notícias de {veic} veículos · últimas 24 horas (21/10 06h49 a 22/10 06h49, horário de Bruxelas)</p>
{pod}{body}
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:8px;"><tr><td style="border-top:1px solid #DDDDDD;padding-top:12px;font-family:{B};font-size:12px;line-height:1.5;color:#777777;">Montado automaticamente. Cada notícia foi conferida na fonte ou em segunda fonte. Ouça também no seu app de podcast: https://bdiehlc-bit.github.io/digest-podcast/feed.xml</td></tr></table>
</td></tr></table></td></tr></table></body></html>'''
open('email.html','w').write(out)
# roteiro
L=[]
L.append(("Ana","Bom dia! Aqui é a Ana, e este é o Digest Diário de quinta-feira, vinte e dois de outubro."))
L.append(("Leo","E eu sou o Leo. Hoje são dezoito notícias. Vamos começar pelo orçamento belga."))
L.append(("Ana",items[0][8]))
L.append(("Leo","É um assunto que mexe com impostos e serviços. Dá para acompanhar de perto nas próximas semanas."))
for it in items[1:]:
    L.append(("Ana" if len(L)%2==0 else "Leo", it[8]))
L.append(("Ana","E é isso por hoje. As matérias completas estão no e-mail."))
L.append(("Leo","Até amanhã!"))
# alternate strictly
for i,x in enumerate(L): L[i]={"speaker":"Ana" if i%2==0 else "Leo","text":x[1]}
json.dump(L,open('roteiro.json','w'),ensure_ascii=False)
print(len(items),veic,sum(len(x['text'].split()) for x in L))
json.dump({"titulo":items[0][1],"caps":[i[7] for i in items]},open('meta.json','w'),ensure_ascii=False)
