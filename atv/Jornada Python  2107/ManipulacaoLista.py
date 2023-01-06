from numpy import true_divide


sacola = ['Arroz', 'Feijão', 'Carne', 'Farinha']
print(f'A lista inicial é: {sacola}')

#METODO: APPEND(objeto)
#Adiciona um item no fim da lista

sacola.append('Macarrão')
print(f'Lista após a chamda do método APPEND(): {sacola}')

#MÉTODO: EXTEND(Estrutura)
#Adiciona todos os itens de outra estrutura ao fim da lista

sacola.extend(['Maionese', 'Ketchup'])
print(f'Lista após a chamada do método EXTEND(): {sacola}')

#Método: INSERT (indice, objeto)
#Insere um item na posição desejada

sacola.insert(0, 'Milho')
print(f'Lista após a chamda do método INSERT(): {sacola}')

#Método REMOVE (Objeto)
#Remove o primeiro elemento igual ao valor passado

sacola.remove('Macarrão')
print(f'Lista após a chamada do elemento REMOVE(): {sacola}')

#Método POP (Indice)
#Remove o item da posição desejada da Lista e o retorna
#Caso o intem não for especificado, retorna o ultimo elemento
#Cada POP remove um alimento 
# usar elemento = sacola.pop(3) adiciona o elemento novamente ps: no final da lista

sacola.pop(3)
print(f'Lista após a chamada do método POP(): {sacola}')

#Método CLEAR()
#Remove todos os elementos da lista

sacola.clear()
print(f'Lista após a chamada do elemento CLEAR(): {sacola}')

#Método INDEX (valor[, comeco, fim])
#Retorna o indice do primeiro elemento do valor especificado na lista
#Podemos ainda passar outros dois parâmetros que dizem onde pesquisar na lista (comeco e fim)
# (sacola.indec('Milho', 0, 5))

#print(sacola.index())
#print(f'Lista após a chamada do método INDEX(): {sacola}')

#Método: COUNT(valor)
#Conta o número de ocorrências do valor especificado na lista
#Conta em números a quantidade de elemento que consta na lista

print(sacola.count('Arroz'))
print(f'Lista após a chamada do Método COUNT(): {sacola}')

#Método: SORT([chave, reverso])
#Ordena os itens da lista . Parêmetro adicionais podem ser utilizados para customizar a ordenação

sacola.sort(reverse=True)
print(f'Lista após a chamada do método SORT(): {sacola}')

#Método: REVERSE()
#Reverte os elementos na lista

sacola.reverse()
print(f'Lista após a chamada do método REVERSE(): {sacola}') 

#Método: COPY()
#Retorna uma lista com a cópia dos elementos da lista de origem

copia_sacola = sacola.copy()
print(f'Lista após a chamado do método COPY(): {copia_sacola}')