from abc import ABC, abstractmethod

# Principio de Segregación de Interfaces (ISP)

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass


class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass


class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass


class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        print("El humano está comiendo")

    def dormir(self):
        print("El humano está durmiendo")

    def trabajar(self):
        print("El humano está trabajando")


class Robot(Trabajador):
    def trabajar(self):
        print("El robot está trabajando")
