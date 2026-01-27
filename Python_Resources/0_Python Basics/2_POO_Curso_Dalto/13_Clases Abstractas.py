from abc import ABC, abstractmethod

class  Persona(ABC):
    @abstractmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.actividad=actividad
    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola me llamo:{self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad) 

    def hacer_actividad(self):
        print("Estoy estudiando")

class Trabajador(Persona):
    def __init__(self,nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad) 
    def hacer_actividad(self):
        print(f"Estoy Trabajando en {self.actividad}")

pedrito=Trabajador("Pedrito",24,"no binario","Programacion")
dalto= Estudiante("lucas",21,"Masculino","Programador")

dalto.hacer_actividad()
pedrito.hacer_actividad()

# Con las clases abstractas los estoy obligando a implementarlo.

