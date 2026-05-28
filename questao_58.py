def q_58():
    alunos = soma_idade = 0
    while True:
        idade = int(input('Idade do aluno (999 para parar): '))
        if idade == 999:
            break
        alunos += 1
        soma_idade += idade
    print(f'Total de alunos: {alunos}')
    print(f'Média de idade: {soma_idade / alunos if alunos > 0 else 0:.1f}')
