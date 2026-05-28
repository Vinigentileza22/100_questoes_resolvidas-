def q_43():
    c = 30
    while c >= 1:
        if c % 4 == 0:
            print(f'[{c}]', end=' ')
        else:
            print(c, end=' ')
        c -= 1
