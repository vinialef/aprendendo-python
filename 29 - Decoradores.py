def pai(operação):
    def somar(a,b):
        return a+b
    def subtrair(a,b): 
        return a-b
    def multiplicar(a,b):
        return a*b
    def dividir(a,b):
        return a/b
    
    while True:
        if operação == "1":
           return somar    
        elif operação == "2":
           return subtrair
        elif operação == "3":
           return multiplicar
        elif operação == "4":
           return dividir
        elif operação == "5":
            break
        else:
            print("Opção Inválida")
        
    


menu=" \n[1] Somar \n[2] Subtrair \n[3] Multiplicar \n[4] Dividir \n[5] Parar "
print(menu)
resultado = pai(input("=> "))(float(input("\nDigite um valor: ")),float(input("Digite outro valor:  ")))
print(f"\nO resultado é {resultado}\n")

#Implementar usando classes
    