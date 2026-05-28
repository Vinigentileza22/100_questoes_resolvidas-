def q_57():
    total_m = total_f = 0
    while True:
        salario = float(input('Salário: R$'))
        sexo = input('Sexo (M/F): ').upper()
        if sexo == 'M': total_m += salario
        elif sexo == 'F': total_f += salario
        resp = input('Quer continuar? (S/N): ').upper()
        if resp == 'N':
            break
    print(f'Total salários Homens: R${total_m:.2f}')
    print(f'Total salários Mulheres: R${total_f:.2f}')
