#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
#dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias. 

data = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

data2 = int(input("\nDigite a data atual: ")) # Data atual
mes2 = int(input("Digite o mês atual: ")) # Mês atual
ano2 = int(input("Digite o ano atual: ")) # Ano atual
idade_anos = ano2 - ano # Calculando a idade da pessoa


#Abaixo iremos ver se o usuario já completou ano
if mes >= mes2: #se o mes do aniversario for maior que o ano atual 
    if mes == mes2:#se ambos os meses forem iguais
      if data > data2: #checar os dias
         idade_anos - 1 #Se a data de nascimento for maior que a atual, quer dizer que o usuário ainda não completou ano
                            # Por isso decrementamos 1 em idade anos, pois a idade que tinha ali era a idade que ele iria completar
    else:  idade_anos - 1 # Se o mês for maior, o mesmo acontece.
        # A decrementação só ocorre uma vez.
        
dias_passados =  (30 - data) + ((12 - mes)*30) + ((mes2 - 1)*30) + data2 + (idade_anos)*365

print("Voce viveu", dias_passados,"dias.")
