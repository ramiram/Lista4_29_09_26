def potencia_de_numero(a,b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / potencia_de_numero(a,-b)
    return a * potencia_de_numero(a, b - 1)

base = int(input("digite o valor base: "))
expoente = int(input("digite o valor expoente: "))
potencia = potencia_de_numero(base,expoente)

print(f"a potencia de {base} e {expoente} e resultado: {potencia}")