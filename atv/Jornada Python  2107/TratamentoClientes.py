clientes = {
    'Maria': '041.587.588-89', 
    'Jonas': '235.789.147-56', 
    'Carlos': '048.456.965-46', 
    'Marcos': '456.925.741-63'
    }
    
resultado = {}

for chave, valor in clientes.items():
  resultado[chave] = valor.replace(".", "").replace("-", "")

print(resultado)