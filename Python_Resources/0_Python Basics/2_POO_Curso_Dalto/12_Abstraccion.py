class Auto():
    def __init__(self):
        self._estado="Apagado"

    def encender(self):
        self._estado="encendido"
        print("El autoo esta encendido")

    def conducir(self):
        if self._estado=="apagado":
            self.encender()
        print("Conduciendo el auto")

mi_auto=Auto()
mi_auto.conducir()
