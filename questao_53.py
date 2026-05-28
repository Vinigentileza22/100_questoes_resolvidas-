def q_53():
    homens = mulheres = soma_idade = soma_homens = mulheres_mais_20 = 0
    c = 1
    while c <= 5:
        idade = int(input(f'Idade da {c}ª pessoa: '))
        sexo = input('Sexo (M/F): ').upper()
        soma_idade += idade
        if sexo == 'M':
            homens += 1
            soma_homens += idade
        elif sexo == 'F':
            mulheres += 1
            if idade > 20: mulheres_mais_20 += 1
        c += 1
    print(f'Homens: {homens}, Mulheres: {mulheres}, Média grupo: {soma_idade/5:.1f}')
    print(f'Média homens: {soma_homens/homens if homens > 0 else 0:.1f}')
    print(f'Mulheres +20 anos: {mulheres_mais_20}')
