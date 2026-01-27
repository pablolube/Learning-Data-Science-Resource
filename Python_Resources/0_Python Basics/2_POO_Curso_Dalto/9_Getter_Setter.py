# HERENCIA SIMPLE

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self._nombre=nombre
        self._edad=edad
    def get_nombre(self):
       return self._nombre
    def set_nombre(self,new_nombre):
       self._nombre=new_nombre
klhklhklhklhl
#Ejecuto el Get
dalto=Persona("Dalto",34,"Argentina")
print(dalto.get_nombre())

#Ejecuto el Set
dalto.set_nombre("Pepito")
print(dalto.get_nombre())

