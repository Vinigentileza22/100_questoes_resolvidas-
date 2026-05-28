def q_100():
    def Media(n1, n2):
        return (n1 + n2) / 2
    def Situacao(m):
        if m < 5.0: return 'REPROVADO'
        elif m < 7.0: return 'RECUPERAÇÃO'
        else: return 'APROVADO'
    med = Media(float(input('N1: ')), float(input('N2: ')))
    sit = Situacao(med)
    print(f'Média: {med:.1f} - Situação: {sit}')
