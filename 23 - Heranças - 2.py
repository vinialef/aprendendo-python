class PrintableMixin:
    def print_info(self):
        print(f"\nTipo: {type(self).__name__}")
        for chave, valor in self.__dict__.items():
            print(f"{chave}: {valor}")

class Pessoa(PrintableMixin):
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

class Alien(PrintableMixin):
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

person = Pessoa("Alice", 30)
person.print_info()  

alien = Alien("Blink", 21)
alien.print_info()  