import re
from collections import Counter

def ache_palavra(texto):
    palavras = re.findall(padrao,texto)
    contagem = Counter(palavras)
    return contagem

texto = input("\nDigite um texto: ")
padrao = input("\nDigite o qual palavra você quer encontrar dentro do texto: ")
repetidas = ache_palavra(texto)

for palavras,contagem in repetidas.items():
    print(f"\nHá {contagem} palavras '{palavras}' no texto\n")
     
