"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
 """


# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.

#Tuplas
# ============================================================
# TUPLAS EN PYTHON
# ============================================================

print("\n=== 1) CREACIÓN DE TUPLAS ===")

tupla_vacia = ()
tupla_simple = (1, 2, 3)
tupla_sin_parentesis = 4, 5, 6
tupla_un_elemento = (10,)   # importante la coma
tupla_desde_iterable = tuple("abc")

print("Tupla vacía:", tupla_vacia)
print("Tupla simple:", tupla_simple)
print("Tupla sin paréntesis:", tupla_sin_parentesis)
print("Tupla de un elemento:", tupla_un_elemento)
print("Tupla desde iterable:", tupla_desde_iterable)


# ============================================================
# 2) ACCESO A ELEMENTOS
# ============================================================
print("\n=== 2) ACCESO A ELEMENTOS ===")

tupla = (10, 20, 30, 40, 50)

print("Tupla:", tupla)
print("Primer elemento (tupla[0]):", tupla[0])
print("Último elemento (tupla[-1]):", tupla[-1])


# ------------------------------------------------------------
# SLICING (rebanado)
# ------------------------------------------------------------
print("\n--- SLICING ---")

print("tupla[1:4]:", tupla[1:4])
print("tupla[:3]:", tupla[:3])
print("tupla[::2] (saltos de 2):", tupla[::2])
print("tupla[::-1] (invertida):", tupla[::-1])


# ============================================================
# 3) OPERACIONES PERMITIDAS (INMUTABLE)
# ============================================================
print("\n=== 3) INMUTABILIDAD ===")

print("❌ No se puede modificar una tupla")
# tupla[0] = 100  # Error


# ============================================================
# 4) OPERACIONES DE CONSULTA
# ============================================================
print("\n=== 4) CONSULTA Y BÚSQUEDA ===")

tupla = (1, 2, 2, 3, 4)

print("Tupla:", tupla)
print("count(2):", tupla.count(2))
print("index(3):", tupla.index(3))
print("3 in tupla:", 3 in tupla)
print("5 not in tupla:", 5 not in tupla)


# ============================================================
# 5) OPERADORES CON TUPLAS
# ============================================================
print("\n=== 5) OPERADORES CON TUPLAS ===")

t1 = (1, 2)
t2 = (3, 4)

print("Concatenar (+):", t1 + t2)
print("Repetir (*):", t1 * 3)


# ============================================================
# 6) FUNCIONES BUILT-IN CON TUPLAS
# ============================================================
print("\n=== 6) FUNCIONES BUILT-IN ===")

numeros = (3, 7, 1, 9)

print("Tupla:", numeros)
print("len():", len(numeros))
print("max():", max(numeros))
print("min():", min(numeros))
print("sum():", sum(numeros))
print("any():", any(numeros))
print("all():", all(numeros))


# ============================================================
# 7) ITERAR TUPLAS
# ============================================================
print("\n=== 7) ITERAR TUPLAS ===")


numeros = (3, 7, 1, 9)

print("Recorrido simple:")
for n in numeros:
    print(n)

print("Con enumerate():")
for i, v in enumerate(numeros):
    print(f"Índice {i} -> Valor {v}")


# ============================================================
# 8) DESEMPAQUETADO DE TUPLAS
# ============================================================
print("\n=== 8) DESEMPAQUETADO ===")

a, b, c = (10, 20, 30)
print("a, b, c:", a, b, c)

a, *resto = (1, 2, 3, 4)
print("a y resto:", a, resto)

*inicio, ultimo = (1, 2, 3, 4)
print("inicio y último:", inicio, ultimo)


# ============================================================
# 9) CONVERSIÓN ENTRE TIPOS
# ============================================================
print("\n=== 9) CONVERSIÓN ENTRE TIPOS ===")

lista = [1, 2, 3]
tupla_desde_lista = tuple(lista)

print("Lista:", lista)
print("Tupla desde lista:", tupla_desde_lista)

print("Lista desde tupla:", list(tupla_desde_lista))


# ============================================================
# 10) COMPARACIONES
# ============================================================
print("\n=== 10) COMPARACIONES ===")

print("(1, 2) == (1, 2):", (1, 2) == (1, 2))
print("(1, 2) < (1, 3):", (1, 2) < (1, 3))


# ============================================================
# 11) TUPLAS ANIDADAS
# ============================================================
print("\n=== 11) TUPLAS ANIDADAS ===")

tupla_anidada = ((1, 2), (3, 4), (5, 6))
print("Tupla anidada:", tupla_anidada)
print("Elemento [1][0]:", tupla_anidada[1][0])


# ============================================================
# 12) USO COMÚN DE TUPLAS
# ============================================================
print("\n=== 12) USO COMÚN ===")

# Retorno múltiple
def operaciones(a, b):
    return a + b, a - b

suma, resta = operaciones(10, 5)
print("Retorno múltiple:", suma, resta)

# Claves inmutables (ejemplo conceptual)
coordenada = (10, 20)
print("Coordenada:", coordenada)


# ============================================================
# FIN – OPERACIONES CON TUPLAS
# ============================================================
