def q_70():
    a, b = 1, 1
    for i in range(10):
        print(a, end=' ')
        a, b = b, a + b
