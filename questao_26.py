def q_26():
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    if n1 > n2:
        print('O primeiro valor é o maior.')
    elif n2 > n1:
        print('O segundo valor é o maior.')
    else:
        print('Não existe valor maior, os dois são iguais.')
