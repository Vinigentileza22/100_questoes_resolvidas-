def q_85():
    nomes = []
    sexos = []
    salarios = []
    for _ in range(5):
        nomes.append(input('Nome: '))
        sexos.append(input('Sexo (M/F): ').upper())
        salarios.append(float(input('Salário: R$')))
    print('--- Mulheres que ganham mais de 5 mil ---')
    for i in range(5):
        if sexos[i] == 'F' and salarios[i] > 5000:
            print(f'{nomes[i]} - R${salarios[i]:.2f}')
