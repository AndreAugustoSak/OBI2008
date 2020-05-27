def mini_calculadora(N, dividendo, divisor):
    melhor_solução = ()
    if N >= dividendo and N >= divisor:
        melhor_solução = (dividendo,divisor)
    if N < dividendo or N < divisor:
        x = 1
        while dividendo > N:
            if dividendo % 2 == 0 and divisor % 2 == 0:
                dividendo = dividendo / 2
                divisor = divisor / 2
            elif dividendo % 3 == 0 and divisor % 3 == 0:
                dividendo = dividendo / 3
                divisor = divisor / 3
            elif dividendo % 5 == 0 and divisor % 5 == 0:
                dividendo = dividendo / 5
                divisor = divisor / 5
            elif dividendo % 7 == 0 and divisor % 7 == 0:
                dividendo = dividendo / 7
                divisor = divisor / 7
            else:
                break
        melhor_solução = (dividendo,divisor)
        if dividendo > N:
            melhor_solução = 'IMPOSSIVEL'
    return melhor_solução
print(mini_calculadora(30,200,90))