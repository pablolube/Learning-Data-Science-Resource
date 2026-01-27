class Ave:
    def Volar(self):
        return "Estoy Volando"

class Ave_Voladora:
    def Volar(self):
        return "Estoy Volando"
    
class Ave_nadadora:
    def Volar(self):
        return "Estoy Volando"
            
class Pinguino(Ave):
    def Volar(self):
        return "No puedo volar"
    
def hacer_volar(ave=Ave):
    return ave.volar()

class  AveVoladora(Ave):
    pass
