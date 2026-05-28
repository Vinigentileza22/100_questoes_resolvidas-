def q_60():
    maior_idade = 0
    nome_velha = ''
    mulher_jovem = 0
    nome_mjovem = ''
    soma_idade = homens_30 = mulheres_18 = total = 0
    while True:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        sexo = input('Sexo (M/F): ').upper()
        total += 1
        soma_idade += idade
        if total == 1 or idade > maior_idade:
            maior_idade = idade
            nome_velha = nome
        if sexo == 'M' and idade > 30:
            homens_30 += 1
        elif sexo == 'F':
            if idade < 18: mulheres_18 += 1
            if mulher_jovem == 0 or idade < mulher_jovem:
                mulher_jovem = idade
                nome_mjovem = nome
        if input('Continuar? (S/N): ').upper() == 'N':
            break
    print(f'Pessoa mais velha: {nome_velha}\nMulher mais jovem: {nome_mjovem}')
    print(f'Média grupo: {soma_idade / total:.1f}')
    print(f'Homens > 30: {homens_30}\nMulheres < 18: {mulheres_18}')
