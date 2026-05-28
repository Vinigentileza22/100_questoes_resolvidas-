def q_75():
    vetor = [1, 1]
    for i in range(2, 16):
        vetor.append(vetor[-1] + vetor[-2])
    print(vetor)
