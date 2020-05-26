def qtd_competidores(N, P, lista):
    aceitos = 0
    for c in range(N):
        competidor = lista[c]
        fase1 = competidor[0]
        fase2 = competidor[1]
        total = fase1 + fase2
        if total >= P:
            aceitos += 1
    return aceitos

print(qtd_competidores(3, 100, [(50,50),(100,0),(49,50)]))

