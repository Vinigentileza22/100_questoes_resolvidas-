def q_81():
    idades = []
    for _ in range(8):
        idades.append(int(input('Idade: ')))
    media = sum(idades) / 8
    pos_25 = [i for i, v in enumerate(idades) if v > 25]
    maior = max(idades)
    pos_maior = [i for i, v in enumerate(idades) if v == maior]
    print(f'Média: {media:.1f}\nPosições > 25 anos: {pos_25}')
    print(f'Maior idade: {maior}\nPosições maior idade: {pos_maior}')
