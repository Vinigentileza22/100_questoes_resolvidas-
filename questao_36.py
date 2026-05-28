def q_36():
    horas = int(input('Horas de atividade no mês: '))
    if horas <= 10: pontos = horas * 2
    elif horas <= 20: pontos = horas * 5
    else: pontos = horas * 10
    print(f'Você fez {pontos} pontos e ganhou R${pontos * 0.05:.2f}')
