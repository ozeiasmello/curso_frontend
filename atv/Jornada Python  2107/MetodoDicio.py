familia = {
    'pai': 'José da Silva',
    'mae': 'Ana Almeida',
    'filho': 'Cleber Almeida da silva',
    'filha': 'Joana ALmeida da Silva'

}

print(f'Família: {familia}')

#COPIA
#Copia um dicionario

copia_familia = familia.copy()

print(f'Copia do dicionario familia: {familia}')

# ITEMS
# Retorna os pares chaves:valor em formato de lista

itens = familia.items()

print(f'Itens: {itens}')
for item in itens :
    print(f'\tChave = {item[0]} e  Valor = {item[1]}')

# KEYS
# Retorna todas as chaves em formato de lista

chaves = familia.keys()

print(f'Chaves: {chaves}')
for chave in chaves:
    print(f'\tChaves: {chave}')

# VALUES
# Retorna todos os valores em formato de lista 

valores = familia.values()

print(f'Valores: {valores}')

for valor in valores:
    print(f'\tValor: {valor}')


# SETDEFAULT
# Insere a chave com o valor passado SE a chave não estiver presente  no dicionário
# Retorna o valor da chave SE a chave já estiver presente no dicionário

familia.setdefault(f'sobrinho', 'Carlos SIlva')

print(familia)

familia.setdefault(f'mae', 'Dona Florinda')
print(familia)

# FROMKYES
# Cria um dicionário a partir de uma lista de chaves e um valor

chaves = ['mae', 'pai', 'filho', 'filha']
valor = 0

jogo = dict.fromkeys(chaves, valor)

print(f'Jogo: {jogo}')