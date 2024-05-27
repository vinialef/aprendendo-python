class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    def __del__(self):
        print("Removendo Objeto...")


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
print(b1.cor, b1.modelo, b1.ano, b1.valor)
b1.buzinar()
b1.correr()
b1.parar()
del b1


#b2 = Bicicleta("verde", "monark", 2000, 189)
#b2.correr()
#print(b2.cor)
