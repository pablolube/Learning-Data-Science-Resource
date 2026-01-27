"""super() en Python se usa para llamar métodos de la clase padre (superclase) desde una clase hija, sin tener que nombrar explícitamente a la clase padre."""
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


class Cuadrado(Rectangulo):
    def __init__(self, alto,ancho):
        # Llama al constructor de Rectangulo
        super().__init__(alto, ancho)

    def area(self):
        return super().area()


class Cubo(Cuadrado):
    def __init__(self, añto,ancho,largo):
        # Llama al constructor de Cuadrado
        super().__init__(alto,ancho)
        self.largo=largo

    def volumen(self):
        return super().area() * self.ancho
