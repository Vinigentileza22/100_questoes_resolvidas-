def q_68():
    mulheres = homens_100 = soma_peso_m = maior_peso_h = 0
    for i in range(1, 9):
        sexo = input('Sexo (M/F): ').upper()
        peso = float(input('Peso: '))
        if sexo == 'F':
            mulheres += 1
            soma_peso_m += peso
        elif sexo == 'M':
            if peso > 100: homens_100 += 1
            if peso > maior_peso_h: maior_peso_h = peso
    print(f'Mulheres: {mulheres}\nHomens > 100Kg: {homens_100}')
    print(f'Média peso mulheres: {soma_peso_m / mulheres if mulheres > 0 else 0:.1f}Kg')
    print(f'Maior peso entre homens: {maior_peso_h}Kg')
