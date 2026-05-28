def q_44():
    i = int(input('Primeiro Valor: '))
    f = int(input('Último Valor: '))
    inc = int(input('Incremento: '))
    while i <= f:
        print(i, end=' ')
        i += inc
    print('Acabou!')
