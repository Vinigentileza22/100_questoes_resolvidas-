def q_83():
    import random
    vetor = [random.randint(0, 99) for _ in range(20)]
    print(f'Originais: {vetor}')
    vetor.sort()
    print(f'Ordenados: {vetor}')
