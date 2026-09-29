def palindromo_texto(texto):
    if len(texto) <= 1:
        return True
    if texto[0] != texto[-1]:
        return False
    return palindromo_texto(texto[1:-1])

texto_palindromo = input("Digite uma palavra: ")
texto_limpo = " ".join(texto_palindromo.split()).lower()
print(f"a palavra {texto_limpo} e um palindromo: {palindromo_texto(texto_limpo)}")