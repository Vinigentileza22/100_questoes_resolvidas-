def q_32():
    import random
    comp = random.randint(1, 5)
    jog = int(input('Adivinhe o número (1 a 5): '))
    if jog == comp:
        print('Parabéns, você acertou!')
    else:
        print(f'Errou! O número era {comp}')
