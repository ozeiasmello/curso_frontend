from datetime import date

from openpyxl import Workbook

# acao = input("Qual o codigo da ação que você quer processar?").upper()
acao = "BIDI4"
with open(f'./dados/{acao}.txt', 'r') as arquivo_cotacao:
    linhas = arquivo_cotacao.readline()
    linhas = [linha .replace("\n","").split(";") for linha in linhas]

workbook = Workbook()
planilha_ativa = workbook.active
planilha_ativa.title = "Dados"
planilha_ativa.append(["DATA", "COTAÇÃO", "BANDA INFERIOR", "BANDA SUPERIOR"])
for linha in linhas:

    # Data
    # linha[0] = 22-01-06
    # linha[1] = 8.8
    ano_mes_dia = linha[0].split(" ")[0]
    data = date(
       year=int(ano_mes_dia.split("-")[0]),
       month=int(ano_mes_dia.split("-")[1]),
       day=int(ano_mes_dia.split("-")[2])
    )
    # Cotação

    cotacao = float(linha[1])

    # Banda inferior
    # MÉDIA MÓVEL (20P) - 2X DESVIO_PADRÃO(20p)

    # Banda Superior
    planilha_ativa[f'A{indice}'] = data
    planilha_ativa[f'B{indice}'] = cotacao

    indice += 1

workbook.save("./saida/Planilha.xlsx")
