def q_31():
    import random
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    comp = random.choice(opcoes)
    jog = input('Escolha Pedra, Papel ou Tesoura: ').capitalize()
    print(f'Computador escolheu: {comp}')
    if jog == comp:
        print('Empate!')
    elif (jog == 'Pedra' and comp == 'Tesoura') or (jog == 'Papel' and comp == 'Pedra') or (jog == 'Tesoura' and comp == 'Papel'):
        print('Você venceu!')
    else:
        print('Você perdeu!')
