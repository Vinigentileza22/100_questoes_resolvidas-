def q_63():
    soma = menor = total = pares = 0
    while True:
        n = int(input('Digite um número: '))
        soma += n
        total += 1
        if n % 2 == 0:
            pares += 1
        if total == 1 or n < menor:
            menor = n
        if input('Continuar? (S/N): ').upper() == 'N':
            break
    print(f'Somatório: {soma}\nMenor valor: {menor}')
    print(f'Média: {soma / total:.1f}\nValores pares: {pares}')
