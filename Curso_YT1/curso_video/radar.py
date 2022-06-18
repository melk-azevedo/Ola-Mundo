from time import sleep
from random import randint

print('Radar a frente \033[31m. \nReduza a velocidade..\033[m')
sleep(3)

print('')

print('Você passou no radar. \nAguarde...')
sleep(3)

print('')

velocidade = randint(30, 200)
vel_maxima = 130
vel_minima = 40
multa = 7

print(f'Você está a {velocidade}km/h')

if velocidade > vel_maxima:
    multa = (velocidade - vel_maxima) * multa
    print(f'''Você está acima da velocidade permitida,
e será multado no valor de \033[31mR$ {multa:.2f}\033[m''')
else:
    print('Continue respeitando os limites de velocidade.')
