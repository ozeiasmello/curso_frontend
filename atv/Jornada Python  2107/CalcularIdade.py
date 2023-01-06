#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
#dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias. 

data = int(input("Digite a data do seu nascimento: ")) # Data do nascimento
mes = int(input("Digite o mês do seu nascimento: ")) # Mês do nascimento
ano = int(input("Digite o ano do seu nascimento: ")) # Ano do nascimento

data2 = int(input("\nDigite a data atual: ")) # Data atual
mes2 = int(input("Digite o mês atual: ")) # Mês atual
ano2 = int(input("Digite o ano atual: ")) # Ano atual
idade_anos = ano2 - ano # Calculando a idade da pessoa

# Aqui abaixo iremos checar se o usuário já completou ano
if mes >= mes2: # Se o mês do aniversário for maior que o mês atual
    if mes == mes2: # Se o ambos os meses forem iguais
        if data > data2: # Checamos os dias
            idade_anos - 1 # Se a data de nascimento for maior que a atual, quer dizer que o usuário ainda não completou ano
                            # Por isso decrementamos 1 em idade anos, pois a idade que tinha ali era a idade que ele iria completar
    else:
        idade_anos - 1 # Se o mês for maior, o mesmo acontece.
        # A decrementação só ocorre uma vez.

dias_passados =  (30 - data) + ((12 - mes)*30) + ((mes2 - 1)*30) + data2 + (idade_anos)*365
"""
Explicando o cálculo:

(30 - data) - Pegamos a data do usuário e subtraímos por 30, exemplo: 30 - 27 = 3, ou seja, se passaram 3 dias após seu nascimento
((12 - mes)*30) - Subtraímos o mês do usuário por 12 e depois multiplicando por 30, transformando em dias, exemplo: ((12-11)*30), se passaram 30 dias após seu nascimento
((mes2 - 1)*30) - Aqui é basicamente a mesma coisa, a diferença é que aqui calculamos quantos dias se passaram desde o início do ano atual
data2 - Somando os dias passados com o dia atual
(idade_anos)*365 - Transformando a idade do usuário em dias

Somando tudo irá dar o resultado.
"""

print("Você viveu",dias_passados,"dias.")