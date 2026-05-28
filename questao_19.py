def q_19():
    nome = input('Nome do aluno: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    print(f'A média do aluno {nome} foi {media:.1f}')
    if media >= 7.0:
        print('O aluno teve um BOM APROVEITAMENTO.')
    else:
        print('O aluno NÃO teve um bom aproveitamento.')
