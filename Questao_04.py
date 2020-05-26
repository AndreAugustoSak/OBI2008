def auto_estrada(C, P):
    qtd_paineis = 0
    posicao = 0
    for c in range(C):
        letra = P[posicao]
        if letra == 'P' or letra == 'C':
            qtd_paineis += 2
        elif letra == 'A':
            qtd_paineis += 1
        else:
            qtd_paineis += 0
        posicao += 1
    return qtd_paineis
print(auto_estrada (5, 'DAPCD'))