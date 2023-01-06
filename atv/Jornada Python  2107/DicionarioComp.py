computador = {
    'cpu': 'Core i7',
    'ram': 'DDR 16GB',
    'ssd':  'Samsung Evo 840 256Gb',
    'gpu': 'RTX 2080 Ti'
}

print(f'Computador v1:{computador}')

computador['ram'] = 'DDR4 32Gb'

print(f'Computador v2: {computador}')
# Os [] adicionam propriedades, caracteristicas
computador ['fonte'] = 'Fonte 600w Corsair'

print(f'Computador V3: {computador}')

# O upgrade adiciona varias chaves, propriedades, valores...
computador.update({'Fonte': 'Corsain 850w Corsain', 'ssd':'Samsung Evo 840 1Tb' })