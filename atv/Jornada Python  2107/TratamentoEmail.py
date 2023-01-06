emails = [
    ',henRy@gmail.com',
    ' ,juLIa@hotmail.com   ',
    'ivaN@gmail.com ',
    'mar,cos@yahoo.com ',
    '     sanDOVAl@hotmail.com ',
    'IVANA@gmail.com   ',
    'ItaMAr@edu.gov.br'
]
# MAP E FILTER 
#REMOVER OS ESPAÇOS USAR: STRIP
#REMOVER VIRGULA E ESPAÇO: REPLACE
#TRANSFORMAR EM MINUSCULO OU MAIUSCULO: LOWER OU UPPER

emails_tratados = [email.strip().replace(",", "").lower() for email in emails]
emails_tratados_gmail = [email.strip().replace(",", "").upper() for email in emails if "@gmail" in email] 

#FILTRAR A LISTA DE ELEMENTOS: EX: UTILIZAR IF "@GMAIL" IN EMAIL


print(emails_tratados_gmail)
print(emails_tratados)



