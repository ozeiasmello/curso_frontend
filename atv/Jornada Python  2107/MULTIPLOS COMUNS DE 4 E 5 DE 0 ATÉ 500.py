#MULTIPLOS COMUNS DE 4 E 5 DE 0 ATÉ 500
#Filtrar numeros
#estruturas condicionais 

resultado = [numero for numero in range(0, 501) if numero % 4 == 0 if numero % 5 == 0]

print(resultado)
