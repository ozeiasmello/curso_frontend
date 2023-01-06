

clientes = {
    'Maria': '041.587.588-89', 
    'Jonas': '235.789.147-56', 
    'Carlos': '048.456.965-46', 
    'Marcos': '456.925.741-63'
    }

#{chave: valor for intem in sequencia}
resultado = {chave.upper():valor.replace(".", "").replace("-", "") for chave, valor in clientes.items()}

print(resultado)


#Filtrar estruturas condicionais 