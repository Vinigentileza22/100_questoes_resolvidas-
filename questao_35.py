def q_35():
    tipo = input('Carro popular ou luxo? ').lower()
    dias = int(input('Dias de aluguel: '))
    km = float(input('Km percorridos: '))
    if tipo == 'popular':
        preco = dias * 90 + (km * 0.20 if km <= 100 else km * 0.10)
    else:
        preco = dias * 150 + (km * 0.30 if km <= 200 else km * 0.25)
    print(f'Total a pagar: R${preco:.2f}')
