def vestibular(N, gabarito, respostas_aluno):
    posicao = 0
    acertos = 0
    for c in range(N):
        if gabarito[posicao] == respostas_aluno[posicao]:
            acertos += 1
        posicao += 1
    return acertos
print(vestibular(7,'AEDBCCE','ADDCCBE') )