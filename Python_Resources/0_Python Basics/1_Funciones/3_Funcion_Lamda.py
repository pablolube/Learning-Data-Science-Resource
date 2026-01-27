#lamda parametros: expresion

def doble(x):
    return x*2
print(doble(5))

#Con lambda

doble2=lambda x:x*2
print(doble2(5))



#Con lambda con 2 parametros 
multiplicar=lambda x,y:x*y
print(multiplicar(2,4))

#lamda con 3 parametros 
sumar=lambda x,y,z:x+y+z
print(sumar(1,2,3))

#lamda con strings
concatenar=lambda nombre,apellido:nombre+" "+apellido
print(concatenar("pablo","luberriaga"))

#Check edad
check_edad= lambda edad:True if edad>=18 else False
print(check_edad(21))
print(check_edad(1))
