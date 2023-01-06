import requests

headers= {'User-Agente': 'Mozilla/5.0'}
res = requests.get('https://www.fundamentus.com.br/fii_resultado.php', headers=headers)
if res:
    print('Response OK')
else:
    print('Response Failed')

print(res)