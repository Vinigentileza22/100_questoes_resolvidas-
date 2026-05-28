def q_93():
    def Contador(i, f, inc):
        for x in range(i, f + 1, inc):
            print(x, end=' >> ')
        print('FIM')
    Contador(int(input('Início: ')), int(input('Fim: ')), int(input('Incremento: ')))
