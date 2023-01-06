from random import randint


#for aluno in alunos:
# print(f'O nome do aluno é: {aluno}')
# nota = randint(3, 10)
# print(f'A nota do Aluno {aluno} foi de {nota}')

#for aluno in alunos:
#   nota_1 = randint(5, 10)
 #   nota_2 = randint(4, 9)
  #  nota_3 = randint(3, 7)
#
 #   nota_final = nota_1 * 0.2 + nota_2 * 0.3 + nota_3 * 0.5

  #  print(f' A nota do final do aluno {aluno} foi de: {nota_final}')

alunos = ['João', 'Ana', 'Paula', 'Matheus', 'Bento']
notas = [randint(5, 10), randint(5, 10), randint(5, 10), randint(5, 10), randint(5, 10)]

for aluno, nota in zip(alunos, notas):
    print(f'A nota do aluno {aluno} foi de {nota}')
