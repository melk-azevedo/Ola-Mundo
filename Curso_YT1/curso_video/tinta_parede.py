"""Exercicio de pintar parede"""
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura

tinta = area / 2

print(
    f'''A sua parede tem dimenção de {largura}x{altura}
e sua area é {area:.2f}m.''')
print(f'Para pintar essa parede, voce precisara de {tinta}L de tinta. ')
