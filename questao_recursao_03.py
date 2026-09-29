def inverter_strings(texto):
    if len(texto) <= 1:
        return texto
    return texto[-1] + inverter_strings(texto[:-1])

frase = input("digite uma palavra: ")
print(f"a palavra {frase} invertido e: {inverter_strings(frase)}") 
