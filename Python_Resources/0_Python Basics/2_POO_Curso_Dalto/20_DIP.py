#Dependency Inversion Principle (DIP)

# class Diccionario:
#     def verificar_palabras(self,palabra):
#          #logica para verificar palabras
#         pass
# class CorretorOrtografico:
#     def __init__(self):
#           self.diccionario=Diccionario()
#     def corregir_texto(self,texto):
#         pass

from abc import ABC,abstractmethod

class VerificadorOrtografico(self,palabra):
    #Logica para verificar palabras si esta en el diccionario
    pass
class CorrectorOrtorgrafico
    def __init__(self,verificador):

    def corrregir_text(self,text):
        #usamor el verificador para corregir el texto 