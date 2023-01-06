#CRIANDO SETS

carteira = {'PETR4', 'CASH3', 'MGLU3', 'BBAS3', 'WEGE3'}
print(f'Carteira Inicial: {carteira}')

# Adicionar elementos com ADD

carteira.add('ITSA4')
print(f'Carteira pós ADD(): {carteira}')

# Atualizando elementos com UPDATE
carteira.update({'PETR4', 'AVEB3', 'RAIZ4'})
print(f'Carteira após upedate(): {carteira}')

# Removendo elementos com DISCARD
carteira.discard('PETR4')
print(f'Carteira após discard(): {carteira}')

# Removendo elementos com REMOVE
carteira.remove('ABEV3')
print(f'Carteira após remove(): {carteira}')

# Retirando elementos com POP (aleatório, pois nao sabe qual é o ultimo elemento)
item = carteira.pop()
print(f'item removido: {item}')
print(f'Carteira após o pop:{carteira}')
