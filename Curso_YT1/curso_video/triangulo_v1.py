r1 = int(input('Digite o primeiro número: '))
r2 = int(input('Digite o segundo número: '))
r3 = int(input('Digite o terceiro número: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('forma um trângulo')
else:
    print('Não forma um triângulo')
