def q_94():
    def Fibonacci(n):
        a, b = 1, 1
        for _ in range(n):
            print(a, end=' >> ')
            a, b = b, a + b
        print('FIM')
    Fibonacci(int(input('Quantos termos? ')))
