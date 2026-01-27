""" encadenamiento de métodos (method chaining) es una técnica de programación que permite llamar varios métodos seguidos en una sola línea, porque cada método devuelve el objeto sobre el que se está trabajando."""
class Coche:
        def encender(self):
            print("has arrancado el motor")
            return self
        def conducir(self):
            print("Estas conduciendo")
            return self
        def frenar(self):
            print("Frenaste!!")
            return self
        def apagar(self):
            print(" Apagaste el choche")
            return self
coche=Coche()

coche.encender().conducir()
