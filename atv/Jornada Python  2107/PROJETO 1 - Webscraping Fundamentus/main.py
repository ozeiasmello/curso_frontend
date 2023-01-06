import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.fundamentus.com.br/fii_resultado.php')
soup = BeautifulSoup(response.text, 'html.parser')

print(response) 

pass