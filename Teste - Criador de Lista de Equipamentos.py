itens = []

while True:
    if len(itens) <= 2:
       item = input()
       itens.append(item)     
    else:
        break

print("Lista de Equipamentos:")  
for item in itens:    
    print(f"- {item}")