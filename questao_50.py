def q_50():
    import random
    c = 1
    acima_de_5 = 0
    div_3 = 0
    print('Sorteados: ', end='')
    while c <= 20:
        n = random.randint(0, 10)
        print(n, end=' ')
        if n > 5: acima_de_5 += 1
        if n % 3 == 0: div_3 += 1
        c += 1
    print(f'\nAcima de 5: {acima_de_5}\nDivisíveis por 3: {div_3}')
