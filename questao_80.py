def q_80():
    import random
    vetor = [random.randint(1, 15) for _ in range(30)]
    chave = int(input('Digite a chave a procurar: '))
    posicoes = [i for i, v in enumerate(vetor) if v == chave]
    print(f'Sorteados: {vetor}')
    print(f'A chave {chave} foi encontrada nas posições {posicoes}')
    print(f'Total de vezes sorteada: {len(posicoes)}')
