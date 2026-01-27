class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre} y soy de nacionalidad {self.nacionalidad}")

class Artista:
    def __init__(self,habilidad):
        self.habilidad=habilidad

    def mostrar_habilidad(self):
        print(f"Mi habilidad artistica es: {self.habilidad}")   

class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas=notas
        self.universidad=universidad

class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,trabajo,habilidad,salario):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.trabajo=trabajo
        self.salario=salario

    def mostrar_habilidad(self):
        print("no tengo habilidades artisticas")
    
    def presentarse(self):
        return f'{super().mostrar_habilidad()}'
    

Ana=EmpleadoArtista("Ana",28,"Argentina","Diseñadora Grafica","Pintura Digital",60000)
Ana.presentarse()

# como se si here de Persona o de Artista?
herencia=issubclass(EmpleadoArtista,Persona)
instancia= isinstance(Ana,Artista) 
print(herencia)
print(instancia)
