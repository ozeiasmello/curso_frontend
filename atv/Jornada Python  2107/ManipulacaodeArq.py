#texto = "Jornada Python - Manipulação de Arquivos"
# Descritor de arquivo
#arquivo = open("C:\\Users\\Ozeias\\Desktop\\Jornada Python  2107\\dados.txt", 'w' )
# Escrita do dado, dar um nome a String , colocando a variável texto
#arquivo.write(texto)

# Leitura do dado
#arquivo = open("C:\\Users\\Ozeias\\Desktop\\Jornada Python  2107\\dados.txt", 'r' )
#não colocar variavel
#retorno = arquivo.read()
#Colocar o nome da variável
#print(retorno)

texto = "\n\nVenha DOMINAR Python!"

arquivo = open("C:\\Users\\Ozeias\\Desktop\\Jornada Python  2107\\dados.txt", 'a' )

arquivo.write(texto)

# IMPORTANTE, SEMPRE FECHAR O ARQUIVO
arquivo.close()
