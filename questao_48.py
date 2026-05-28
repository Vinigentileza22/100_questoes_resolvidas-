def q_48():
    soma = 0
    c = 1
    while c <= 7:
        n = int(input(f'Digite o {c}º número: '))
        soma += n
        c += 1
    print(f'O somatório é {soma}')
