def soma_digitos_de_um_numero_inteiro_positivo(numero):
    if numero < 10:
        return numero
    else:
        return numero % 10 + soma_digitos_de_um_numero_inteiro_positivo(numero // 10)

numero_inteiro_positivo = int(input("digite um numero positivo: "))
resultado = soma_digitos_de_um_numero_inteiro_positivo(numero_inteiro_positivo)
print(f"a soma dos digitos  de '{numero_inteiro_positivo}', e o resultado: {resultado}")
