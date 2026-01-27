# HERENCIA SIMPLE

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre} y soy de nacionalidad {self.nacionalidad}")

class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        # CON LA FUNCION SUPER() LLAMAMOS AL CONSTRUCTOR DE LA CLASE PADRE - LE PONGO QUE QUIERO QUE HEREDE
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo=trabajo
        self.salario=salario    

roberto= Empleado("Roberto",30,"Mexicana","Programador",50000)
print(roberto.nombre)

# HERENCIA JERARQUICA

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre} y soy de nacionalidad {self.nacionalidad}")

class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        # CON LA FUNCION SUPER() LLAMAMOS AL CONSTRUCTOR DE LA CLASE PADRE - LE PONGO QUE QUIERO QUE HEREDE
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo=trabajo
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,grado,materia):
        super().__init__(nombre,edad,nacionalidad)
        self.grado=grado
        self.materia=materia
