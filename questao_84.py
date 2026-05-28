def q_84():
    nomes = []
    idades = []
    for _ in range(9):
        nomes.append(input('Nome: '))
        idades.append(int(input('Idade: ')))
    print('--- Menores de Idade ---')
    for i in range(9):
        if idades[i] < 18:
            print(f'{nomes[i]} - {idades[i]} anos')
