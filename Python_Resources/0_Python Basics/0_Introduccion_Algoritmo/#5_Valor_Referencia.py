"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 
    """
# Valor y referencia
#Tipos de datos por valor
my_int_a=10
print(my_int_a)
#my_int_b=20
my_int_b=my_int_a
my_int_a=30
my_int_b=my_int_a
print(my_int_b)

# Una variable por valor cada vez que se le asigne otra variable se le asigna una copia en ese momento ,por mas que cambie

# Tipos de datos por referencia 
my_list_a=[10,20]
my_list_b=[11,21]
my_list_b=my_list_a
my_list_a.append(2030)
print(my_list_b)

#Los valores por referencia heredan su direccion de memoria

# ============================================================
# ASIGNACIÓN Y PASO DE VARIABLES
# POR VALOR vs POR REFERENCIA EN PYTHON
# ============================================================

print("\n==============================")
print("1) ASIGNACIÓN DE VARIABLES")
print("==============================")

# ------------------------------------------------------------
# 1.1 TIPOS INMUTABLES → COMPORTAMIENTO POR VALOR
# ------------------------------------------------------------
print("\n1.1 ASIGNACIÓN POR VALOR (TIPOS INMUTABLES)")

a = 10
b = a  # se copia el valor (nuevo objeto si se modifica)

b = 20

print("Valor de a (NO cambia):", a)
print("Valor de b (modificado):", b)


# ------------------------------------------------------------
# 1.2 TIPOS MUTABLES → COMPORTAMIENTO POR REFERENCIA
# ------------------------------------------------------------
print("\n1.2 ASIGNACIÓN POR REFERENCIA (TIPOS MUTABLES)")

lista1 = [1, 2, 3]
lista2 = lista1  # ambas variables apuntan al MISMO objeto

lista2.append(4)

print("lista1 (afectada):", lista1)
print("lista2 (afectada):", lista2)


# ============================================================
print("\n==============================")
print("2) FUNCIONES Y PARÁMETROS")
print("==============================")

# ------------------------------------------------------------
# 2.1 FUNCIÓN CON TIPO INMUTABLE (POR VALOR)
# ------------------------------------------------------------
print("\n2.1 FUNCIÓN CON INMUTABLE (int)")

def cambiar_numero(n):
    print("  Dentro de la función (antes):", n)
    n = 100
    print("  Dentro de la función (después):", n)

x = 10
print("Antes de llamar a la función:", x)

cambiar_numero(x)

print("Después de llamar a la función:", x)


# ------------------------------------------------------------
# 2.2 FUNCIÓN CON TIPO MUTABLE (POR REFERENCIA)
# ------------------------------------------------------------
print("\n2.2 FUNCIÓN CON MUTABLE (list)")

def agregar_elemento(lista):
    print("  Dentro de la función (antes):", lista)
    lista.append(99)
    print("  Dentro de la función (después):", lista)

numeros = [1, 2, 3]
print("Antes de llamar a la función:", numeros)

agregar_elemento(numeros)

print("Después de llamar a la función:", numeros)


# ============================================================
print("\n==============================")
print("3) DICCIONARIOS (MUTABLES)")
print("==============================")

def modificar_diccionario(dic):
    print("  Dentro de la función (antes):", dic)
    dic["nuevo"] = "agregado"
    print("  Dentro de la función (después):", dic)

datos = {"nombre": "Pablo"}
print("Antes de la función:", datos)

modificar_diccionario(datos)

print("Después de la función:", datos)


# ============================================================
print("\n==============================")
print("4) EVITAR MODIFICAR EL ORIGINAL (COPIA)")
print("==============================")

def modificar_copia(lista):
    copia = lista.copy()   # copia independiente
    copia.append(100)
    return copia

original = [1, 2, 3]
print("Lista original ANTES:", original)

nueva_lista = modificar_copia(original)

print("Lista original DESPUÉS:", original)
print("Nueva lista modificada:", nueva_lista)


# ============================================================
print("\n==============================")
print("5) RESUMEN FINAL")
print("==============================")

print("""
TIPOS INMUTABLES (por valor):
- int
- float
- str
- bool
- tuple

TIPOS MUTABLES (por referencia):
- list
- dict
- set

REGLA CLAVE:
Si el objeto es MUTABLE → puede modificarse fuera de la función
Si el objeto es INMUTABLE → NO se modifica fuera de la función
""")


#DIFICULTAD EXTRA (opcional):
"""
Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 """

a=1
b=2
def funciona(a,b):
    temp=a
    a=b
    b=temp
    return a,b

c,d=funciona(a,b)

print(f"Valores Originales a:{a} y b:{b}")
print(f"Valores Cambiados c:{c} y d:{d}")

# Funcion por referencia
a=[1,2]
b=[2,1]

def funcionb(a,b):
    temp=a
    a=b
    b=temp
    return a,b

c,d=funcionb(a,b)

print(f"Valores Originales a:{a} y b:{b}")
print(f"Valores Cambiados c:{c} y d:{d}")
