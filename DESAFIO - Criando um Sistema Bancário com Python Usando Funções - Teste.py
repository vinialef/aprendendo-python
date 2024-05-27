def menu():
    menu = """\n
    ================ MENU ================
    [1]Depositar
    [2]Sacar
    [3]Extrato
    [4]Nova conta
    [5]Listar contas
    [6]Novo usuário
    [7]Sair
    => """
    return input(menu)

def depositar (saldo,valor,extrato,/):
     if valor > 0:     
        saldo += valor
        extrato += (f"Depósito: R$ {valor:.2f}\n")
        print("Depósito realizado com sucesso!")
     else:
          print("O Valor digitado é inválido!")
     return saldo,extrato


def sacar (*,valor,saldo,limite_de_saque,extrato,limite,numero_de_saques):

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
            print("Saque concluído!\n")

    return saldo, extrato

def mostrar_extrato (saldo,/,*,extrato):
        print("\n=========EXTRATO==========")
        print("Nenhuma movimentação feita" if not extrato else extrato)
        print("\n==========================")
        print(f"Saldo total:R$ {saldo:.2f}")
        print("\n==========================")   

def criar_usuarios (usuarios):
     cpf = input("Digite seu cpf aqui (somente os 11 números): ")
     usuario = filtrar_usuario(cpf, usuarios)
     
     if usuario:
          print("\nJá existe usuário cadastrado com esse CPF!")
          return
     
     
     nome = input("Digite o nome completo: ")
     data = input("Digite a data de nascimento aqui (DD/MM/AA): ")    
     endereco = input("Digite seu endereço aqui(Rua - Número - Bairro - Cidade/Sigla do Estado): ")

     usuarios.append({"nome": nome, "data": data, "cpf": cpf, "endereco": endereco})

     
     print("\n====Usuário cadastrado com sucesso!====")
     
def filtrar_usuario (cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def principal():
    agencia ="0001"
    limite_de_saque = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas= []
    
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
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)
        
        elif opcao == "6":
             criar_usuarios(usuarios)
        
        elif opcao == "7":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


principal()