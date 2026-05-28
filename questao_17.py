def q_17():
    velocidade = float(input('Qual a velocidade do carro (Km/h)? '))
    if velocidade > 80:
        multa = (velocidade - 80) * 5
        print(f'Você foi multado! O valor da multa é R${multa:.2f}')
