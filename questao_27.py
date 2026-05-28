def q_27():
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    if media <= 4.9:
        print('REPROVADO')
    elif 5.0 <= media <= 6.9:
        print('RECUPERAÇÃO')
    else:
        print('APROVADO')
