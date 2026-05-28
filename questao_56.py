def q_56():
    soma = 0
    while True:
        n = int(input('Digite um valor (1111 para parar): '))
        if n == 1111:
            break
        soma += n
    print(f'O somatório é {soma}')
