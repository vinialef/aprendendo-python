frutas = ["maçã","banana","uva"]
#for indice,fruta in enumerate(frutas):
   #print(f"{indice}-> {fruta}")

numeros = [1,5,32,12,3,26,7,2,13]
pares = []
quadrado = []
for numero in numeros:
   if numero % 2 == 0:
     pares.append(numero)

for numero2 in numeros:
  quadrado.append(numero2**2)
     
     
print(pares,"\n",quadrado) 
