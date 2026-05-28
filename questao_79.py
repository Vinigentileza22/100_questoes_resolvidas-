def q_79():
    vetor = []
    for i in range(10):
        vetor.append(int(input(f'Número {i+1}: ')))
    for i, valor in enumerate(vetor):
        if valor % 2 == 0:
            print(f'Par {valor} na posição {i}')
