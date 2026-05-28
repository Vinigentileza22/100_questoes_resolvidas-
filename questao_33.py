def q_33():
    valor_casa = float(input('Valor da casa: R$'))
    salario = float(input('Salário: R$'))
    anos = int(input('Anos a pagar: '))
    prestacao = valor_casa / (anos * 12)
    if prestacao > salario * 0.30:
        print('Empréstimo NEGADO.')
    else:
        print(f'Empréstimo APROVADO! Prestação: R${prestacao:.2f}')
