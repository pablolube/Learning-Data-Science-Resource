class estudiante():
    def __init__(self,Nombre,edad,grado):
        self.Nombre=Nombre
        self.edad=edad
        self.grado=grado
    def estudiar(self):
        print(f"{self.Nombre} esta estudiando")

nombre=input("Ingrese el nombre del estudiante: ")
edad=input("Ingrese la edad del estudiante: ")  
grado=input("Ingrese el grado del estudiante: ")    

estudiante=estudiante(nombre,edad,grado)

print(f"El estudiante {estudiante.Nombre} tiene {estudiante.edad} años y esta en {estudiante.grado} grado")

while True:
    print("¿Desea que el estudiante estudie? (si/no)")  
    estudiar=input()
    if (estudiar.lower()=="si"):
        estudiante.estudiar()
        break



