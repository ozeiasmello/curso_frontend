#numero = int(input('Digite o número: '))
#if numero > 0:
 #   fatorial = 1
  #  for item in range(1, numero + 1 ):
   #     fatorial = fatorial * item 
    #print(fatorial)


import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input(f'Chute o valor de 1 a 10: '))
    if chute > valor_aleatorio:
        print(f'Chute foi maior que o valor gerado')
    elif chute < valor_aleatorio:
        print(f'Chute foi menor que o calor gerado')
    elif chute == valor_aleatorio:
        acertou = True
        print(f'Você acertou!')    