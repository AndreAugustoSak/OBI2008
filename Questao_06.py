def mini_calculadora(N, dividendo, divisor):
    bits = 2 ** N
    if bits >= dividendo:
        a = dividendo
        b = divisor
        # MDC = Menor divisor comum
        while b != 0:
            resto = a % b
            a = b
            b = resto
        mdc = a
        print(mdc)
        x = int(dividendo / mdc)
        y = int(divisor / mdc)
        t = (x, y)
        return t
    else:
        return 'IMPOSSÍVEL'

print(mini_calculadora(30,200,90))