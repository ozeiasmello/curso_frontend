# Levando em consideração a velocidade maxima permitida de 80km em uma determinada rua. Crie
#um programa que recebe do usuario um valor que representa a velocidade e com base nessa velocidade , diga se 
#ele tomou uma multa leve, grave ou gravissima. Levando em consideração que se a pessoa estiver abaixo da 
# velocidade maxima, seu programa deve exibir "Não houve multa" , caso esteja a 10km acima , deve exibir "Levou multa leve", 
# caso esteja entre 11 e 20km acima da velocidade maxima, exibir "Levou multa grave"
# e caso esteja acima de 20km da velocidade maxima exiba : "Levou multa gravíssima"

velocidade = int(input('Digite a velocidade: '))
velocidade_maxima = 80

if velocidade <= velocidade_maxima:
    print(f'Não houve multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print(f'Levou multa leve ')
elif velocidade > velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print(f'Levou multa gravissima')