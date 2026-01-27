
# EJERCICIO 1
class persona():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad 
    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Estudiante(persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado=grado
    def imprimir_grado(self):
        print(f"Grado: {self.grado}")

Pablo=Estudiante("Pablo",20,"Tercer año")
Pablo.imprimir_datos()  

# EJERCICIO 2 

class animal():
    def comer(self):
        print("El animal está comiendo.")

class mamifero(animal):
   def amamantar(self):
        print(f"{self.nombre} está amamantando a sus crías.")   

class Ave(animal):
    def volar(self):
        print(f"{self.nombre} está volando.")   

class Muercielago(mamifero,Ave):
    def __init__(self,nombre):
        mamifero.__init__(self,nombre)
        Ave.__init__(self,nombre)   


