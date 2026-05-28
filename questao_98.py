def q_98():
    def SuperSomador(i, f):
        return sum(range(i, f + 1))
    r = SuperSomador(int(input('Início: ')), int(input('Fim: ')))
    print(f'Soma do intervalo: {r}')
