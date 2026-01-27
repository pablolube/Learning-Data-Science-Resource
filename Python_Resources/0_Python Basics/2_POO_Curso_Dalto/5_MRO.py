class A:
    def hablar(self):
        print("Hola, soy la clase A")

class F(D):
    def hablar(self):
        print("Hola, soy la clase F")

class B(A):
    def hablar(self):
        print("Hola, soy la clase B")

class C(F):
    def hablar(self):
        print("Hola, soy la clase C")

class D(B,C):
    pass

d=D()
d.hablar()

print(D.mro())  # muestra el orden de resolucion de metodos
print(D.__mro__)  # muestra el orden de resolucion de metodos