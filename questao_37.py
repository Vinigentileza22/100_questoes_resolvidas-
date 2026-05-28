def q_37():
    salario = float(input('Salário: R$'))
    gen = input('Gênero (M/F): ').upper()
    anos = int(input('Anos na empresa: '))
    if gen == 'F':
        if anos < 15: aumento = 0.05
        elif anos <= 20: aumento = 0.12
        else: aumento = 0.23
    else:
        if anos < 20: aumento = 0.03
        elif anos <= 30: aumento = 0.13
        else: aumento = 0.25
    print(f'Novo salário: R${salario * (1 + aumento):.2f}')
