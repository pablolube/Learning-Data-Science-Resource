"""Funciones que :
1) Aceptan una funcion como argumento
2) Devuelven una funcion como resultado""" 

def hablarAlto(texto):
    return texto.upper()

def hablarBajo(texto):
    return texto.lower()


# FUNCION COMO ARGUMENTO
def hola(func):
    texto=func("Hola")
    print(texto)

hola(hablarAlto)
hola(hablarBajo)

# Devuelven una funcion como resultado

def divisor(x):
    def dividendo(y):
        return y/x
    return dividendo

divide=divisor(2)
print(divide(10))
