def q_10():
    largura = float(input('Largura da parede (m): '))
    altura = float(input('Altura da parede (m): '))
    area = largura * altura
    print(f'Área a ser pintada: {area:.2f}m²')
    print(f'Quantidade de tinta necessária: {area / 2:.2f} litros')
