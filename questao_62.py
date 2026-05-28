def q_62():
    total = soma = mais_21 = 0
    while True:
        idade = int(input('Idade: '))
        total += 1
        soma += idade
        if idade >= 21:
            mais_21 += 1
        if input('Continuar? (S/N): ').upper() == 'N':
            break
    print(f'Idades digitadas: {total}\nMédia: {soma / total:.1f}')
    print(f'Pessoas com 21 ou mais: {mais_21}')
