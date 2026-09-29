def ache_o_anagrama(texto):

    if len(texto) <= 1:
        return [texto]

    textos = [ ]

    for anagrama in range(len(texto)):

        atualiza_caracteres = texto[anagrama]


        resto_do_texto = texto[:anagrama] + texto[anagrama+1:]


        for sub_anagrama in ache_o_anagrama(resto_do_texto):
            textos.append(atualiza_caracteres + sub_anagrama)


    return list(dict.fromkeys(textos))


palavra = input("digite uma palavra: ")
resultado = ache_o_anagrama(palavra)
print(f"a palavra {palavra} contem o total de anagramas: {len(resultado)}")
print(resultado)