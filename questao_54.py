def q_54():
    soma_alt = mais_90 = menos_50_menos_160 = mais_190_mais_100 = 0
    c = 1
    while c <= 7:
        peso = float(input(f'Peso da {c}ª pessoa: '))
        alt = float(input(f'Altura da {c}ª pessoa: '))
        soma_alt += alt
        if peso > 90: mais_90 += 1
        if peso < 50 and alt < 1.60: menos_50_menos_160 += 1
        if alt > 1.90 and peso > 100: mais_190_mais_100 += 1
        c += 1
    print(f'Média altura: {soma_alt/7:.2f}m')
    print(f'Mais de 90Kg: {mais_90}')
    print(f'<50Kg e <1.60m: {menos_50_menos_160}')
    print(f'>1.90m e >100Kg: {mais_190_mais_100}')
