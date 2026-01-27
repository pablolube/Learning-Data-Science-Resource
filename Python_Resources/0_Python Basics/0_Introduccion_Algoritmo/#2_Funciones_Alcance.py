"""_
 EJERCICIO:
 - Crea ejemplos de funciones básicas que representen las diferentes
   posibilidades del lenguaje:
   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 - Comprueba si puedes crear funciones dentro de funciones.
 - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 - Debes hacer print por consola del resultado de todos los ejemplos.
   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

 DIFICULTAD EXTRA (opcional):
 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 
 Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 
"""
# ============================================================
# EJEMPLOS DE FUNCIONES EN PYTHON
# Apunte teórico–práctico
# ============================================================


# ============================================================
# 1) FUNCIONES SIN PARÁMETROS NI RETORNO
# ============================================================
# No reciben datos ni devuelven resultados.
# Solo ejecutan una acción.
def saluda():
    print("Hola, esta es una función sin parámetros ni retorno")

# Llamada a la función
saluda()


# ============================================================
# 2) FUNCIONES CON UNO O VARIOS PARÁMETROS
# ============================================================

nombre = "Pablo"
edad = 15


# ------------------------------------------------------------
# 2.1 Parámetro simple
# Recibe un solo valor y lo utiliza dentro de la función
# ------------------------------------------------------------
def saludo1(nombre):
    print(f"Hola {nombre}")

saludo1(nombre)


# ------------------------------------------------------------
# 2.2 Parámetro con valor por defecto
# Si no se pasa el argumento, se usa el valor asignado
# ------------------------------------------------------------
def saludo2(nombre, edad=18):
    print(f"Hola {nombre}, tengo {edad} años")

saludo2(nombre, edad)   # Se pasa la edad
saludo2(nombre)         # Usa el valor por defecto (18)


# ------------------------------------------------------------
# 2.3 Parámetros variables (*args)
# Permite recibir una cantidad indefinida de argumentos
# Los valores se almacenan en una tupla
# ------------------------------------------------------------
def sumar(*numeros):
    print("La suma es:", sum(numeros))

sumar(1, 2, 3, 4)


#2.4.1
# Funciones con Listas 

def mostrar_numeros(*args):
    print("Argumentos recibidos:", args)

numeros = [1, 2, 3, 4]

# Desempaquetamos la lista
mostrar_numeros(*numeros)




# ------------------------------------------------------------
# 2.4 Parámetros variables con nombre (**kwargs)
# Recibe argumentos en forma clave=valor
# Se almacenan en un diccionario
# ------------------------------------------------------------
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_datos(nombre="Pablo", edad=30, pais="Argentina")



#2.4.2
# Funciones con Diccionarios

def mostrar_datos(**kwargs):
    print("Datos recibidos:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

persona = {
    "nombre": "Pablo",
    "edad": 30,
    "pais": "Argentina"
}

# Desempaquetamos el diccionario
mostrar_datos(**persona) #--> con * desempaqueto el diccionario


# ------------------------------------------------------------
# 2.5 Parámetros solo posicionales (/)
# Obliga a pasar los argumentos solo por posición
# ------------------------------------------------------------
def dividir(a, b, /):
    print("Resultado de la división:", a / b)

dividir(10, 2)
# dividir(a=10, b=2)  # ❌ Error


# ------------------------------------------------------------
# 2.6 Parámetros solo por nombre (*)
# Obliga a usar el nombre del parámetro al llamar la función
# ------------------------------------------------------------
def configurar(*, modo):
    print("Modo:", modo)

configurar(modo="debug")
# configurar("debug")  # ❌ Error


# ============================================================
# 3) FUNCIONES CON RETORNO
# ============================================================
# Devuelven un valor usando la palabra clave return
def suma(a, b):
    if  isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return "Error: ambos valores deben ser números"

a = 10
b = 12
resultado = suma(a, b)
print("Resultado de la suma:", resultado)


# ============================================================
# 4) FUNCIONES DENTRO DE OTRAS FUNCIONES
# ============================================================
# Python permite definir funciones dentro de otras funciones
def funcion_externa():
    print("Estoy en la función externa")

    def funcion_interna():
        print("Estoy en la función interna")

    # Llamada a la función interna
    funcion_interna()

funcion_externa()


# ============================================================
# 5) USO DE FUNCIONES INCORPORADAS EN PYTHON
# ============================================================
numeros = [3, 7, 1, 9]
texto="capitalize"
print("Lista:", numeros)
print("Cantidad de elementos:", len(numeros))
print("Número mayor:", max(numeros))
print("Número menor:", min(numeros))
print("Suma total:", sum(numeros))
print("Tipo:", type(numeros))
print("Upper:", texto.upper)
print("Lower:", texto.lower)
print("Capitalize:", texto.capitalize)


# ============================================================
# 6) VARIABLES LOCALES Y GLOBALES
# ============================================================

#Variables globales

global_var="Python"

print(global_var)
def hello_python():
    local_var="Hola"
    print(f"{local_var},{global_var}!")
print(global_var)
print(local_var) # no se puede acceder desde fuera porque es local a la funcion 

# Variable global (accesible desde todo el programa)
contador = 0

def incrementar():
    global contador  # Permite modificar la variable global
    contador += 1
    print("Contador dentro de la función:", contador)

incrementar()
incrementar()
print("Contador fuera de la función:", contador)


# ------------------------------------------------------------
# Variable local
# Solo existe dentro de la función
# ------------------------------------------------------------
def funcion_local():
    mensaje = "Soy una variable local"
    print(mensaje)

funcion_local()

# EJECICIO  ADICIONAL 

"""Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 
 Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 """


def print_numbers(texto1,texto2)-> int:
    count=0
    for numero in range(1,101):
        if numero %3==0 and numero %5==0:
            print(texto1+texto2)
        elif numero % 3==0:
            print(texto1)
        elif numero % 5 == 0:
            print(texto2)
        else:
            print(numero)
            count+=1
    return print(f"Cantidad de veces que se imprimio el numero fue {count}")

print_numbers("texto1","texto2")