class Celular():
    #Contructor
    def __init__(self,marca,modelo,camara):
        self.marca=marca
        self.modelo=modelo
        self.camara=camara 
    def llamar(self):
        print(f"Llamando desde el celular {self.modelo} de la marca {self.marca}")
    def cortar(self):
        print("Llamada finalizada")

celular1=Celular("Xiaomi","Redmi Note 11",50)
celular2=Celular("Samsung","Galaxy A32",64)     
print(f"El celular {celular1.modelo} de la marca {celular1.marca} tiene una camara de {celular1.camara} MP")

celular1.llamar()
celular1.cortar()