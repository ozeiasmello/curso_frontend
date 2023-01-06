import base64

with open("C:\\Users\\Ozeias\\Desktop\\Jornada Python  2107\\logo.png", 'rb') as arquivo:
    arquivo_b6 = base64.b64encode(arquivo.read()) 
    
    print(arquivo_b6)


import json

cadastros =[
    {
         "Nome": "João",
         "idade": 31,
         "Profissões":["Estagiário", "Desenvolvedor Python", "Engenheiro de Software"]


    }
]
# Usando o ENSURE_ASCII=FALSE vai manter os caracteres presente no nome, como, Oz'é'ias. indent=True deixa a lista ajeitada
print(json.dumps(cadastros, ensure_ascii=False, indent=True))