

escolha = int(input("Informe sua conta: \n[1] Conta Normal \n[2] Conta Universitária \n[3] Conta Especial \nDigite Aqui: "))
if escolha == 1:
    print ("Sua conta é normal")
elif escolha == 2:
    print ("Sua conta é universitária")
elif escolha == 3:
    print ("\nSua conta é especial \nVocê tem 5 vezes mais cheque especial que uma conta normal\n")      
saldo = int(input("Quanto Você possui de saldo: "))
saque = int(input("Quanto Você quer sacar: "))
cheque_especial = int(input("Quanto Você possui de Cheque Especial: "))

if escolha == 1:
    print ("Sua")   
if escolha == 1:   
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Saldo insuficiente")

elif escolha == 2:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif escolha == 3:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + (5*cheque_especial)):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Saldo insuficiente")

else:
    print("Opção inválida")