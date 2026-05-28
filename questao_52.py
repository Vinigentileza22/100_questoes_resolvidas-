def q_52():
    soma_idade = 0
    mais_18 = 0
    menos_5 = 0
    maior_idade = 0
    c = 1
    while c <= 10:
        idade = int(input(f'Idade da {c}ª pessoa: '))
        soma_idade += idade
        if idade > 18: mais_18 += 1
        if idade < 5: menos_5 += 1
        if c == 1 or idade > maior_idade: maior_idade = idade
        c += 1
    print(f'Média: {soma_idade/10:.1f}')
    print(f'Mais de 18: {mais_18}\nMenos de 5: {menos_5}\nMaior idade: {maior_idade}')
