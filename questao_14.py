def q_14():
    km = float(input('Quantidade de Km percorridos: '))
    dias = int(input('Quantidade de dias alugados: '))
    print(f'O preço total a pagar é: R${(dias * 90) + (km * 0.20):.2f}')
