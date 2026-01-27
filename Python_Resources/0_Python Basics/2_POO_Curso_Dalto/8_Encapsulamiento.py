class MiClase:
    def __init__(self):
        # Con el _ le digo que es un atributo privado
        self.atributo_publico = "Valor publico"
        self._atributo_privado = "Valor privado"
        self.__atributo_muy_privado = "Valor muy privado"
    def __hablar(self):
        return "Hola desde un metodo privado"   

objeto=MiClase()        
# Acceso al atributo publico
print(objeto.atributo_publico)  # Salida: Valor publico
        
# Acceso al atributo privado (convención, no es realmente privado)
print(objeto._atributo_privado)  # Salida: Valor privado

# Acceso al atributo muy privado (name mangling)
#print(objeto.__atributo_muy_privado)  # Esto causará un error

print(objeto. __hablar)  # Salida: Valor muy privado       

