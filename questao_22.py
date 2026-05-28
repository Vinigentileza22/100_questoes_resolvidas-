def q_22():
    ano_nasc = int(input('Ano de nascimento: '))
    idade = 2026 - ano_nasc
    if idade < 18:
        print(f'Faltam {18 - idade} anos para o alistamento.')
    elif idade > 18:
        print(f'Já se passaram {idade - 18} anos do alistamento.')
    else:
        print('Você deve se alistar este ano!')
