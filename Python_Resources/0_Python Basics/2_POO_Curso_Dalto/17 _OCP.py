class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario=usuario
        self.mensaje=mensaje

    def notificar(self):
        raise NotImplementedError
    
class notificarEmail(Notificador):
    def notificar(self):
        print(f"Enviar mensaje a {self.usuario.email}")

class notificarSMS(Notificador):
    def notificar(self):
        print(f"Enviar sms a {self.usuario.sms}")    
    
class notificarWhatsapp(Notificador):
    def notificar(self):
        print(f"Enviar Whatsapp   a {self.usuario.whatsapp}")    