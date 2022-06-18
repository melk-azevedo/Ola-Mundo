idade = int(input('Digite a sua idade: '))
resposta = ''
if idade < 16:
    print('Você não pode votar.')
    resposta = 'não'
elif 16 <= idade < 18 or idade > 65:
    print('Voto Opcional. \nDeseja votar nessa eleição ?')
    resposta = input('Digite (sim) para prosseguir ou (nao) para encerrar: \n')
    if resposta == 'sim':
        print('Vamos votar!')
    else:
        print('Até a proxima eleição.')


else:
    print('Voto Obrigatório.')
    resposta = 'sim'

if resposta == 'sim':

    voto = idade

    voto_nulo = 0
    Bolsonaro = 22
    votoBolsonaro = 0
    Lula = 44
    votoLula = 0

    while voto:
        voto = int(input(
            'Digite o numero do seu candidato, 1 para nulo e qualquer outra'
            ' coisa para sair: '))
        if voto == 22:
            print('Você votou em Bolsonaro')
            votoBolsonaro += 1
        elif voto == 44:
            print('Você votou em Lula')
            votoLula += 1
        elif voto == 1:
            print('Voto Nulo')
            voto_nulo += 1
        else:
            voto = False
            print("saindo")

    print('Obrigado por vir!')

    print("Votos bolsonaro: ", votoBolsonaro, " / Votos Lula:",
          votoLula, " / Votos Nulos ", voto_nulo)
