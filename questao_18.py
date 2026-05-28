def q_18():
    ano_nascimento = int(input('Ano de nascimento: '))
    idade = 2026 - ano_nascimento
    print(f'Sua idade é {idade} anos.')
    if idade >= 16:
        print('Você já tem idade para votar.')
    else:
        print('Você ainda não tem idade para votar.')
