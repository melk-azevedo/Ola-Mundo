def get_tipo_dia(dia):
    dias = {
        1: 'Final de Semana',
        2: 'Dia de Semana',
        3: 'Dia de Semana',
        4: 'Dia de Semana',
        5: 'Dia de Semana',
        6: 'Dia de Semana',
        7: 'Final de Semana',
    }
    return dias.get(dia, '**DIA INVÁLIDO**')


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia}: {get_tipo_dia(dia)}')
