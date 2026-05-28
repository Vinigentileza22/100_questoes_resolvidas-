def q_29():
    nome = input('Nome: ')
    salario = float(input('Salário: R$'))
    anos = int(input('Anos na empresa: '))
    if anos <= 3:
        novo = salario * 1.03
    elif anos < 10:
        novo = salario * 1.125
    else:
        novo = salario * 1.20
    print(f'{nome} terá um novo salário de R${novo:.2f}')
