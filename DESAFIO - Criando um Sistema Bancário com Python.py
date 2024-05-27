menu = "=========== \n[1]Saque \n[2]Deposito \n[3]Extrato \n[4]Sair \n=========== \n=> "

extrato =""
limite_de_saque = 0
saldo = 0

while True:
    escolha = int(input(menu))

    if escolha == 1:
        valor = float(input("\nDigite o valor a ser sacado: "))
        if valor < 0: 
            print("Valor inválido\n")
        elif saldo <= 0:
            print("Falha na operação! Sem saldo\n")
        elif limite_de_saque >= 3:
            print("Falha na operação! Limite de Saques excedido\n")
        elif valor > 500:
            print("Falha na operação! Valor excede o limite máximo\n")
        elif valor >= 0:
            print("Saque concluído\n")
            extrato += f"Saque: R$ {valor:.2f}\n"
            saldo -= valor
            limite_de_saque += 1

    if escolha == 2:
        deposito = float((input("Digite o valor a ser Depositado: ")))
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
    
    if escolha == 3:
        print("\n=====EXTRATO=====")
        print("Nenhuma movimentação feita" if not extrato else extrato)
        print("\n=================")
        print(f"Saldo total:R$ {saldo:.2f}")
        print("\n=================")
    
    if escolha == 4:
        break
