class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def __str__(self):
        return f'Persona(nombre {self.nombre},edad{self.edad})'
    def __repr__(self):
        return f'Persona(nombre{self.nombre},edad{self.edad})'

    #SOBRECARGA DE OPERADORES
    def __add__(self,otro):
        nuevo_valor=self.edad+ otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)

dalto=Persona("Dalto",21)
pedro=Persona("Pedro",22)
juan=Persona("Pedro",22)
resultado=dalto+pedro+juan
print(resultado)