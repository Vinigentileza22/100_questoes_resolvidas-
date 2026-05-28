def q_78():
    vetor = []
    for i in range(15):
        vetor.append(int(input(f'Número {i+1}: ')))
    print('Vetor:', vetor)
    for i, valor in enumerate(vetor):
        if valor % 10 == 0:
            print(f'Múltiplo de 10 na posição {i}')
