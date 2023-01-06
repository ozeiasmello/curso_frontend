homens = {'João', 'Joaquim', 'Alberto', 'Antonio', 'Leonardo', 'Victor','Kleber', 'Marcelo', 'Alfredo'}
alta_renda = {'Ana', 'Joaquim', 'Joana', 'Antonio', 'Kleber', 'Marcelo', 'Alfredo', 'Carla', 'Adriana'}

print(f'Conjunto de Homens: \t{homens}')
print(f'Conjunto de Alta Renda: {alta_renda}\n{"-" * 150}\n')

# Interceção: Itens que estão em ambos os conjuntos
homens_alta_renda = homens.intersection(alta_renda)
print(f'Usuários com alta renda: {homens_alta_renda}')

# União: Itens de ambos os conjuntos

homens_e_alta_renda = homens.union(alta_renda)
print(f'Homens e Usuários de alta renda: {homens_e_alta_renda}')


# Diferença: Itens que estão apenas em um dos conjuntos

homens_nao_alta_renda = homens.difference(alta_renda)
alta_renda_nao_homens = alta_renda.difference(homens)

print(f'Usuários homens não alta renda: {homens_nao_alta_renda}')
print(f'Usuário Alta renda não homem = {alta_renda_nao_homens}')

# Diferença Simétrica: Itens que estão em um conjunto ou em outro mas não em ambos

homens_nao_alta_renda_e_mulheres = homens.symmetric_difference(alta_renda)
print(f'Usuários homens não Alta renda e Usuárias Mulheres Alta renda: {homens_nao_alta_renda_e_mulheres}')
