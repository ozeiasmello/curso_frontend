titulo = 'Monitor Gamer'
polegadas = 27
preco = 1299.99


print(
    f'Nome do produto: {titulo.upper():-^50}\n'
    # o * é o caractere que ira preencher, podendo escolher outro, serve para preencher na frente e atras, um caractere de preencher
    # o ^ serve para o alinhamento, centraliza
    # o 50 indica o numero de caracteres preenchido, tamanho da string
    f'Polegadas: {polegadas}\n'
    f'Preço: R$ {preco}'
)