def acoes_bolsa(lista):
    p1 = 0
    p2 = 4
    soma = []
    for c in range(len(lista)-3):
        soma.append(sum(lista[p1:p2]))
        p1 += 1
        p2 += 1
    lucro = max(soma)
    return lucro
print(acoes_bolsa([-2,1,-2,1,0,-3]))