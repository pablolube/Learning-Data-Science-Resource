# Reduce (funcion,iterable)

import functools
letras=["H","O","L","A"]

palabra=functools.reduce(lambda x,y:x+y,letras)
print(palabra)


# Ejemplo 2 Factorial de 5 

numeros=[1,2,3,4,5]
resultado=functools.reduce(lambda x,y:x*y,numeros)
print(resultado)