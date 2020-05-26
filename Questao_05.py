def acoes_bolsa(lista):
    p1 = 0
    p2 = 4
    newsoma = sum(lista[p1:p2])
    for c in range(len(lista)-3):
        soma = sum(lista[p1:p2])
        p1 += 1
        p2 += 1
        if soma > newsoma:
            newsoma = soma
    return newsoma
print(acoes_bolsa([-1,-2,-3,-4,-5,-6,-7,-8]))