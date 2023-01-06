import psutil


bateria = psutil.sensors_battery() 
percentual_bateria = str(bateria.percent)
restam = int(percentual_bateria) - int(100)


print(f'Este notebook está com {percentual_bateria}% de bateria e restam {restam}% para a carga completa!')

plugado = bateria.power_plugged

if plugado:
    print('O notebook está conectado na tomada!')
else:
    print('O notebook está desconectado da tomada!')