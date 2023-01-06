numero_eleitores = input('Digite o número de eleitores: ')
total_eletores = int(numero_eleitores)

votos_brancos= input('Digite o número de votos brancos: ')
valor_votos_brancos = int(votos_brancos)

votos_nulos = input('Digite o número de votos nulos: ')
valor_votos_nulos = int(votos_nulos)

votos_validos= input('Digite o número de votos validos: ')
valor_votos_validos = int(votos_validos)

percentual_votos_brancos = (valor_votos_brancos/total_eletores)*100
print(str(percentual_votos_brancos)+ '% Votos Brancos')

percentual_votos_nulos = (valor_votos_nulos/total_eletores)*100
print(str(percentual_votos_nulos)+ '% Votos Nulos')

percentual_votos_validos = (valor_votos_validos/total_eletores)*100
print(str(percentual_votos_validos)+ '% Votos Validos')

#print(total_eletores)
