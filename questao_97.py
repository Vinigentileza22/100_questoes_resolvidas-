def q_97():
    def Maior(v1, v2, v3):
        return max(v1, v2, v3)
    r = Maior(int(input('V1: ')), int(input('V2: ')), int(input('V3: ')))
    print(f'O maior é {r}')
