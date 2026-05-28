def q_82():
    notas = []
    for _ in range(10):
        notas.append(float(input('Nota: ')))
    media = sum(notas) / 10
    acima_media = sum(1 for n in notas if n > media)
    maior = max(notas)
    pos_maior = [i for i, v in enumerate(notas) if v == maior]
    print(f'Média turma: {media:.1f}\nAlunos acima da média: {acima_media}')
    print(f'Maior nota: {maior}\nPosições maior nota: {pos_maior}')
