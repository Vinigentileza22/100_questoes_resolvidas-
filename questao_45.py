def q_45():
    i = int(input('Primeiro Valor: '))
    f = int(input('Último Valor: '))
    inc = int(input('Incremento: '))
    if i < f:
        while i <= f:
            print(i, end=' ')
            i += inc
    else:
        while i >= f:
            print(i, end=' ')
            i -= inc
    print('Acabou!')
