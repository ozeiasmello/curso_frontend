#          0    1    2    3    4    5 
from operator import le


letras = ['a', 'b', 'c', 'd', 'e', 'f']
#          -6   -5   -4   -3   2   -1
#print(letras[0:3:1])
#print(letras[3:6:1])
#print(letras[::-1])
print(letras[-6:-3:1])
print(letras[-3::1])

# print(letras[::2]) pula de 2 em 2 mudando o PASSO

#print(letras[::2] + letras [1::2]) as duas listas ficam na mesma linha