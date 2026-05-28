def q_23():
    nome = input('Nome: ')
    sexo = input('Sexo (M/F): ').upper()
    valor = float(input('Valor das compras: R$'))
    if sexo == 'F':
        desconto = valor * 0.13
    else:
        desconto = valor * 0.05
    print(f'Olá {nome}, o valor com desconto é R${valor - desconto:.2f}')
