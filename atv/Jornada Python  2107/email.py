emails = [
    ',henRy@gmail.com',
    ' ,juLIa@hotmail.com   ',
    'ivaN@gmail.com ',
    'mar,cos@yahoo.com ',
    '     sanDOVAl@hotmail.com ',
    'IVANA@gmail.com   ',
    'ItaMAr@edu.gov.br'
]

emails_tratados = [email.strip().replace(",", "").lower() for email in emails]

print(emails_tratados)