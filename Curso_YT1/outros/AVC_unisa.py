from time import sleep


print('''Bem vindo! \nVoce deverá responder apenas com (sim) ou (nao)
as questões a seguir.''')

sleep(1)
print('Vamos ao questionário.\n')
sleep(3)

cont = 0

print('1– Pergunta: Se o farol está vermelho, você pode avançar com o carro?')

print('')
sleep(3)

resposta = input('Responda com (sim) ou (nao): ')
if resposta != 'sim':
    print('Acertou! Vamos para a próxima pergunta.')
    cont = cont+1
else:
    print('Errou, pesquise o assunto!')
    cont == cont

print('')

print('''2– Pergunta: Se o farol está amarelo, você deve acelerar
o carro para passar?''')

print('')
sleep(3)

resposta = input('Responda com (sim) ou (nao): ')

if resposta != 'sim':
    print('Acertou! Vamos para a próxima pergunta.')
    cont = cont+1
else:
    print('Errou, pesquise o assunto!')
    cont == cont

print('')

print('''3– Pergunta: Se o farol está verde e não há nenhum pedestre
atravessando, você pode avançar?''')

print('')
sleep(3)

resposta = input('Responda com (sim) ou (nao): ')

if resposta != 'nao':
    print('Acertou! Vamos para a próxima pergunta.')
    cont = cont+1
else:
    print('Errou, pesquise o assunto!')
    cont == cont

print('')

print('''4– Pergunta: Se o farol está verde e há pedestre atravessando,
você pode avançar?''')

print('')
sleep(3)

resposta = input('Responda com (sim) ou (nao): ')
if resposta != 'sim':
    print('Acertou! Vamos para a próxima pergunta.')
    cont = cont+1
else:
    print('Errou, pesquise o assunto!')
    cont == cont

print('')

print('5– Pergunta: Se o farol está vermelho, você deve parar o carro?')

print('')
sleep(3)

resposta = input('Responda com (sim) ou (nao): ')
if resposta != 'nao':
    cont = cont+1
else:
    print('Errou, pesquise o assunto!')
    cont == cont

print('\n Calculando o resultado aguarde.\n')
sleep(5)

if cont >= 3:
    print('Voce acertou:', cont,
          'de 5 \n Parabéns! Você conhece as leis de trânsito!')
else:
    print('Voce acertou', cont, 'de 5 \nVoce reprovou!')
