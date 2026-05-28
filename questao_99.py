def q_99():
    def Potencia(b, e):
        return b ** e
    r = Potencia(float(input('Base: ')), float(input('Expoente: ')))
    print(f'Resultado: {r}')
