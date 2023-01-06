idade = input('Digite sua Idade: ')
sexo = input('Digite seu sexo "M" para Maculino e "F" para feminino: ')

if sexo.upper() == 'M': 
    # codigo para o sexo masculino
    if int(idade) >= 65:
        print('Parabéns! Já era pra ter se aposentado, mumia véia')
    else:
        print(f'Sua vez ainda não chegou Vagabunda! Espera mais {65 - int(idade)} anos.')
elif sexo.upper() == 'F':
    # codigo para o sexo Feminino
 if int(idade) >= 60:
        print('Parabéns! Já era pra ter se aposentado, mumia véia')
else:
        print(f'Sua vez ainda não chegou Vagabunda! Espera mais {60 - int(idade)} anos.')