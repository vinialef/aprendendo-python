saldo = int(input("Digite seu saldo: "))
saque = int(input("Digite seu saque: "))

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")