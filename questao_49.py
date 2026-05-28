def q_49():
    pares = 0
    impares = 0
    c = 1
    while c <= 6:
        n = int(input(f'Digite o {c}º número: '))
        if n % 2 == 0: pares += 1
        else: impares += 1
        c += 1
    print(f'{pares} pares e {impares} ímpares')
