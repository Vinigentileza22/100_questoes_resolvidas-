def q_91():
    def Maior(v1, v2):
        if v1 > v2: print(f'Maior: {v1}')
        elif v2 > v1: print(f'Maior: {v2}')
        else: print('Os valores são iguais')
    Maior(int(input('V1: ')), int(input('V2: ')))
