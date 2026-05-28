def q_51():
    c = 1
    maior = 0
    menor = 0
    while c <= 8:
        preco = float(input(f'Preço do {c}º produto: R$'))
        if c == 1:
            maior = preco
            menor = preco
        else:
            if preco > maior: maior = preco
            if preco < menor: menor = preco
        c += 1
    print(f'Maior preço: R${maior:.2f}\nMenor preço: R${menor:.2f}')
