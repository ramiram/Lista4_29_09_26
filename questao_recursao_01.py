def maximo_divisor_comum(a,b):
    if b == 0:
        return a
    return maximo_divisor_comum(b, a % b)

primeiro_divisor = float(input("Entre com o primeiro divisor comum: "))
segundo_divisor = float(input("Entre com segundo divisor comum: "))

print(f"o maximo divisor comum de {primeiro_divisor} e {segundo_divisor} e resultado: {maximo_divisor_comum(primeiro_divisor, segundo_divisor)}")
