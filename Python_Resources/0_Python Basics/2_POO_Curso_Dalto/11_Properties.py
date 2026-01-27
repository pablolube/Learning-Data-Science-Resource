class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.__nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    @property
    def nombre(self):
       return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre=nuevo_nombre
    
    @nombre.deleter
    def nombre(self):
       del self.__nombre
       print("Se elimino el nombre")

#Ejecuto el Get
dalto=Persona("Dalto",34,"Argentina")
nombre=dalto.nombre


print(nombre)

nombre=dalto.nombre="Pepito"

del dalto.nombre
print(dalto.nombre)
# #Ejecuto el Set
# dalto.set_nombre("Pepito")
# print(dalto.nombre)
