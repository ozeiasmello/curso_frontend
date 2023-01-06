cadastro = {
    'id': 1,
    'nome': 'Ozeias Mello',
    'filhos': ['Joana', 'Sarah'],
    'compras': [
        {
            'id': 4785,
            'produto':  'Notebook Gamer',
            'preco': 2597.99
        } 
    ]

}
filhos = cadastro.get('filhos')
print(filhos)

#notebook_gamer = cadastro["compras"][0]

#print(f'O usuário {cadastro["nome"]} realizou a seguinte compra : {notebook_gamer["produto"]}')