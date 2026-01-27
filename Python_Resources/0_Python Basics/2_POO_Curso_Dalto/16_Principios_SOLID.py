#SRP 
class TanqueDeCombustilbe():
    def __init__(self):
        self.combustible=100
        
    def agregar_combustible(self,cantidad):
        self.combustible+=cantidad

    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self,cantidad):
        self.combustible-=cantidad

class Auto():
    def __init__(self,tanque):        
        self.posicion=0
        self.tanque=tanque

    def mover(self,distancia):
        if self.tanque.obtener_combustible()>= distancia/2:
            self.posicion+=distancia
            self.tanque.usar_combustible(distancia/2)
            print("Has movido el auto exitosamente")
        else:
            print("El auto tiene poco combustible")
    def obtener_posicion(self):
        return self.posicion

    
tanque=TanqueDeCombustilbe()
autito=Auto(tanque)
print(autito.mover)

print(autito.obtener_posicion())
autito.mover(10)

print(autito.obtener_posicion())
autito.mover(20)

print(autito.obtener_posicion())
autito.mover(40)

print(autito.obtener_posicion())
