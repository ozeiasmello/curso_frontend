# Filtrar estruturas condicionais 

cadastro = {
    'Maria' : 4500,
    'Marcos' : 7800,
    'Gabriel' : 3750,
    'João' : 150000
}

salaroa_maior_15000 = {chave: valor for chave, valor in cadastro.items() if valor > 5000}

print(salaroa_maior_15000)