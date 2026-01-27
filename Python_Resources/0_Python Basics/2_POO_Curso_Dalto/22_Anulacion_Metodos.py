
"""En POO (Programación Orientada a Objetos), la anulación de métodos (también llamada sobrescritura de métodos o method overriding) ocurre cuando una clase hija redefine un método que ya existe en su clase padre, manteniendo el mismo nombre y la misma firma, pero con un comportamiento distinto.
"""

class  Animal:
    def comer(self):
        print ('Este animal esta comiendo')

class Conejo(Animal):
    def comer(self):
        print ('Este animal esta comiendo una zanahoria')


conejo=Conejo()

conejo.comer()