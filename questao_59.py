def q_59():
    maior_idade = homens = mulher_jovem = soma_h = 0
    c = 1
    while True:
        idade = int(input('Idade: '))
        sexo = input('Sexo (M/F): ').upper()
        if c == 1 or idade > maior_idade:
            maior_idade = idade
        if sexo == 'M':
            homens += 1
            soma_h += idade
        elif sexo == 'F':
            if mulher_jovem == 0 or idade < mulher_jovem:
                mulher_jovem = idade
        c += 1
        if input('Continuar? (S/N): ').upper() == 'N':
            break
    print(f'Maior idade: {maior_idade}\nHomens cadastrados: {homens}')
    print(f'Mulher mais jovem: {mulher_jovem}')
    print(f'Média idade homens: {soma_h / homens if homens > 0 else 0:.1f}')
