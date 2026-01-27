class Gato:
    def sonido(self):
        return "Miau"
class Perro:
    def sonido(self):
        return "Guau"   

def hacer_sonido(animal):
    print(animal.sonido())  
gato=Gato()
perro=Perro()



#Polimorfismo de funcion
print(gato.sonido())  # Salida: Miau
print(perro.sonido())  # Salida: Guau

# Uso de la función polimórfica
hacer_sonido(perro)

# En lenguajes con tipado estático, se requeriría que Gato y Perro hereden 
# de una clase base común o implementen una interfaz común para lograr 
# el mismo efecto.hacer_sonido(gato)
# En lenguajes de tipodo dinamico no es necesario.

# Duck Typing
""" Situacion en el que una clase de un objeto 
no importa tanto como los metodos y propiedades que posee.  """
# Ejemplo en Python
class Pato:
    def caminar(self):
        print("El pato camina")
    def hablar(self):
        print("El pato hace cuac")
class Gallina:
    def caminar(self):
        print("La gallina camina")
    def hablar(self):
        print("La gallina hace cocoroco")
class persona:
    def atrapar(self,pato):
        pato.caminar()
        pato.hablar()
        print("Has atrapado al pato")

pato=Pato()
gallina=Gallina()   
persona=persona()   
persona.atrapar(pato)
persona.atrapar(gallina)

"""Solo Funciona  si tienen los mismos metodos y propiedades"""

# Enlaces dinamicos
    # Enlaces Estaticos
# Tipo real

# Tipo declarado
