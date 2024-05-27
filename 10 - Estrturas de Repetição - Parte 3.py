opcao = int

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair\n"))

    if opcao == 1:
        print("Efetuando Saque")
    elif opcao == 2:
        print("Exibindo extrando...")
else:
    print("Obrigado por usar nosso sistema bancário,até logo!")