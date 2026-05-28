def q_28():
    largura = float(input('Largura: '))
    comprimento = float(input('Comprimento: '))
    area = largura * comprimento
    print(f'Área: {area}m²')
    if area < 100:
        print('TERRENO POPULAR')
    elif 100 <= area <= 500:
        print('TERRENO MASTER')
    else:
        print('TERRENO VIP')
