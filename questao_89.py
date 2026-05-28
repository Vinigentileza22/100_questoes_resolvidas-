def q_89():
    def Gerador(msg, n, b):
        bordas = ['+-------+', '~~~~~~~~:::::::~~~~~~~', '<<<<<<<<------->>>>>>>']
        print(bordas[b-1])
        for _ in range(n):
            print(msg)
        print(bordas[b-1])
    Gerador('Portugol Studio', 3, 2)
