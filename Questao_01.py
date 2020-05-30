def qtd_competidores(N, P, lista):
    aceitos = 0
    for item in lista:
        a = (sum(item))
        if a >= P:
            aceitos += 1
    return aceitos

print(qtd_competidores (4, 235, [(100,134),(0,0),(200,200),(150,150)]))

