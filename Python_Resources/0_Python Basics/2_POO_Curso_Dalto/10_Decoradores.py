def decorador(funcion):
    def funcion_modficada():
        print("Antes de la funcion")
        funcion()
        print("Despues de la funcion")  
    return funcion_modficada

# def saludo():
#     print("Hola a todos")

# saludo_modificada=decorador(saludo)
# saludo_modificada()

@decorador
def saludo():
    print("Hola a todos")  
     
saludo()