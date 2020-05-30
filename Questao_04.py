def auto_estrada(C, P):
    total = 0
    for letra in P:
        if letra == 'P' or letra == 'C':
            qtd_paineis = 2
        elif letra == 'A':
            qtd_paineis = 1
        else:
            qtd_paineis = 0
        total += qtd_paineis
    return total
print(auto_estrada (14, 'ADCCPPPPPAADCP'))