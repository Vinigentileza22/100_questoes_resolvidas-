def q_30():
    l1 = float(input('Lado 1: '))
    l2 = float(input('Lado 2: '))
    l3 = float(input('Lado 3: '))
    if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
        if l1 == l2 == l3:
            print('Triângulo EQUILÁTERO')
        elif l1 != l2 and l2 != l3 and l1 != l3:
            print('Triângulo ESCALENO')
        else:
            print('Triângulo ISÓSCELES')
    else:
        print('NÃO forma um triângulo.')
