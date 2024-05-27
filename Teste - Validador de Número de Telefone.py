import re

def validar_numero(numero):
    padrao = r"\(\d{2}\) 9\d{4}-\d{4}"
    if re.match(padrao, numero):
        return True
    else:
        return False

digite_numero = input("Digite seu número aqui: ")
numeros = []
numeros.append(digite_numero)

for numero in numeros:
    if validar_numero(numero):
        print(f"{digite_numero} é um número de telefone válido")
    else:
        print(f"{digite_numero} é um número de telefone inválido.")
