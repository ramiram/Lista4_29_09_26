def quantosAnagramaTem(palavra):

    if len(palavra) <= 1:
        return [palavra]

    palavras = [ ]

    for indice in range(len(palavra)):

        contagem__de_caracteres = palavra[indice]


        resto_do_texto = palavra[:indice] + palavra[indice+1:]


        for anagrama in quantosAnagramaTem (resto_do_texto):
            palavras.append(contagem__de_caracteres + anagrama)

    lista_anagramas = list(dict.fromkeys(palavras))
    
    return lista_anagramas


palavra = input("digite uma palavra: ")
resultado = quantosAnagramaTem(palavra)
print(f"a palavra {palavra} contem o total de anagramas: {len(resultado)}")
print(resultado)