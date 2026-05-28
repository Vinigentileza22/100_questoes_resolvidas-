def q_16():
    cigarros_por_dia = int(input('Quantidade de cigarros fumados por dia: '))
    anos_fumando = int(input('Quantos anos já fumou: '))
    total_cigarros = cigarros_por_dia * (anos_fumando * 365)
    minutos_perdidos = total_cigarros * 10
    dias_perdidos = minutos_perdidos / (24 * 60)
    print(f'Você perdeu aproximadamente {dias_perdidos:.1f} dias de vida.')
