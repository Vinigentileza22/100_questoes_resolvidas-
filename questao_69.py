def q_69():
    t1 = int(input('Primeiro termo: '))
    r = int(input('Razão: '))
    soma = 0
    for i in range(10):
        termo = t1 + (i * r)
        print(termo, end=' ')
        soma += termo
    print(f'\nA soma é {soma}')
