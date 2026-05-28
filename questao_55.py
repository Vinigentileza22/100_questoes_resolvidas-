def q_55():
    import random
    comp = random.randint(1, 10)
    tentativas = 4
    acertou = False
    while tentativas > 0 and not acertou:
        jog = int(input(f'Adivinhe o número (1 a 10) - {tentativas} tentativas: '))
        if jog == comp:
            print('Parabéns, você acertou!')
            acertou = True
        else:
            print('Errou!')
            tentativas -= 1
    if not acertou: print(f'O número era {comp}')
