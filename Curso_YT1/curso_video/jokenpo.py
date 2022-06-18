from random import randint
from time import sleep

print('-=--' * 5)
print('Vamos jogar jokenpô')
print('-=--' * 5)

print('')

computador = randint(1, 3)
if computador == 1:
    computador = 'PEDRA'
elif computador == 2:
    computador = 'PAPEL'
elif computador == 3:
    computador = 'TESOURA'

jogador = str(input('''Faça a sua escolha:
[PEDRA]
[PAPEL]
[TESOURA]\n''')).strip().upper()

print(f'Minha escolha foi {computador} e a sua foi {jogador}.')
print(f'{computador} X {jogador} \nVAMOS AO RESULTADO...')

sleep(5)

if computador == jogador:
    print('Poxa deu empate, que tal outra vez ?')
elif computador == 'PEDRA' and jogador == 'TESOURA':
    print('Eu ganhei..')
elif computador == 'PAPEL' and jogador == 'PEDRA':
    print('Eu ganhei..')
elif computador == 'TESOURA' and jogador == 'PAPEL':
    print('EU ganhei..')
else:
    print('Parabéns você ganhou')
