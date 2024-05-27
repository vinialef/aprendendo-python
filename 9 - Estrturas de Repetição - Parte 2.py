texto = input("Digite uma palavra: ")
vogais = "aeiou"


for letras in texto:
    if letras in vogais:
        print(letras.upper(), end=" ")
      
