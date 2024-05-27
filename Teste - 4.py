def menu():
    menu = """\n
    ================ MENU ================
    [1]Depositar
    [2]Sacar
    [3]Extrato
    [4]Sair
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
          print("O Valor digitado é inválido!")
     
    return saldo,extrato


def sacar(*,valor,saldo,limite_de_saque,extrato,limite,numero_de_saques):
    maior_que_saldo = valor > saldo
    maior_que_limite = valor > limite
    excedeu_saques = numero_de_saques >= limite_de_saque

    if maior_que_saldo:
           print("Falha na operação! Sem saldo\n") 
    
    elif  maior_que_limite:
           print("Falha na operação! Limite de crédito excedido\n")

    elif excedeu_saques:
           print("Falha na operação! Limite de Saques excedido\n")
    
    elif valor > 0:
            saldo -= valor
            extrato += (f"Saque: R$ {valor:.2f}\n")
            numero_de_saques += 1
            print("Saque concluído\n")
    else:
         print("O valor informado é inválido")

    return saldo, extrato


def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================") 

def principal():
    limite_de_saque = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                valor=valor,
                saldo=saldo,
                limite_de_saque=limite_de_saque,
                extrato=extrato,
                limite=limite,
                numero_de_saques=numero_de_saques,                
           )

        elif opcao == "3":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


principal()