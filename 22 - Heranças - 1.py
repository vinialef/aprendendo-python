class A:
    def method(self):
        print("Método de A")

class B:
    def method(self):
        print("Método de B")

class C(A, B):
    pass

print(C.__mro__)
