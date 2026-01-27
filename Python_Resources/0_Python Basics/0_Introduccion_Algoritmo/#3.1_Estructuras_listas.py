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

# ============================================================
# LISTAS EN PYTHON
# ============================================================

print("\n=== 1) CREACIÓN DE LISTAS ===")

# Forma literal con []
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = ["Francia", "Alemania", "España", "Reino Unido"]

# Crear lista desde iterable
lista3 = list("abc")

print("lista1:", lista1)
print("lista2:", lista2)
print("lista3:", lista3)


# ============================================================
# 2) ACCESO A ELEMENTOS
# ============================================================
print("\n=== 2) ACCESO A ELEMENTOS ===")

lista = [0, 1, 2, 3, 4]

print("Lista:", lista)
print("Primer elemento (lista[0]):", lista[0])
print("Último elemento (lista[-1]):", lista[-1])


# ------------------------------------------------------------
# SLICING (rebanado)
# ------------------------------------------------------------
print("\n--- SLICING ---")
print("lista[1:3]:", lista[1:3])
print("lista[:2]:", lista[:2])
print("lista[::2] (saltos de 2):", lista[::2])
print("lista[::-1] (invertida):", lista[::-1])


# ============================================================
# 3) AGREGAR ELEMENTOS
# ============================================================
print("\n=== 3) AGREGAR ELEMENTOS ===")

lista.append(5)
print("append(5):", lista)

lista.insert(1, 200)
print("insert(1, 200):", lista)

lista.extend([6, 7, 8])
print("extend([6, 7, 8]):", lista)


# ============================================================
# 4) ELIMINAR ELEMENTOS
# ============================================================
print("\n=== 4) ELIMINAR ELEMENTOS ===")

lista.remove(200)
print("remove(200):", lista)

ultimo = lista.pop()
print("pop() -> último eliminado:", ultimo)
print("Lista actual:", lista)

primero = lista.pop(0)
print("pop(0) -> primero eliminado:", primero)
print("Lista actual:", lista)

del lista[2]
print("del lista[2]:", lista)

lista.clear()
print("clear() -> lista vacía:", lista)


# ============================================================
# 5) MODIFICAR ELEMENTOS
# ============================================================
print("\n=== 5) MODIFICAR ELEMENTOS ===")

lista = [0, 1, 2, 3, 4]
lista[1] = "Nueva variable"
print("Modificar por índice:", lista)


# ============================================================
# 6) BÚSQUEDA Y CONSULTA
# ============================================================
print("\n=== 6) BÚSQUEDA Y CONSULTA ===")

lista = [1, 2, 2, 3, 4]

print("Lista:", lista)
print("index(2):", lista.index(2))
print("count(2):", lista.count(2))
print("3 in lista:", 3 in lista)
print("5 not in lista:", 5 not in lista)


# ============================================================
# 7) ORDENAMIENTO Y REVERSO
# ============================================================
print("\n=== 7) ORDENAMIENTO Y REVERSO ===")

lista.sort()
print("sort() ascendente:", lista)

lista.sort(reverse=True)
print("sort(reverse=True):", lista)

lista.reverse()
print("reverse():", lista)

nueva = sorted(lista)
print("sorted(lista) (no modifica original):", nueva)


# ============================================================
# 8) COPIAR LISTAS
# ============================================================
print("\n=== 8) COPIAR LISTAS ===")

copia1 = lista.copy()
copia2 = lista[:]
copia3 = list(lista)

referencia = lista  # ❌ NO es copia

print("copy():", copia1)
print("slicing [:]:", copia2)
print("list():", copia3)
print("referencia:", referencia)


# ============================================================
# 9) OPERADORES CON LISTAS
# ============================================================
print("\n=== 9) OPERADORES CON LISTAS ===")

lista1 = [1, 2]
lista2 = [3, 4]

print("Concatenar (+):", lista1 + lista2)
print("Repetir (*):", lista1 * 3)


# ============================================================
# 10) FUNCIONES BUILT-IN
# ============================================================
print("\n=== 10) FUNCIONES BUILT-IN ===")

numeros = [3, 7, 1, 9]

print("Lista:", numeros)
print("len():", len(numeros))
print("max():", max(numeros))
print("min():", min(numeros))
print("sum():", sum(numeros))
print("any():", any(numeros))
print("all():", all(numeros))


# ============================================================
# 11) ITERAR LISTAS
# ============================================================
print("\n=== 11) ITERAR LISTAS ===")

print("Recorrido simple:")
for n in numeros:
    print(n)

print("Con enumerate():")
for i, v in enumerate(numeros):
    print(f"Índice {i} -> Valor {v}")


# ============================================================
# 12) COMPRENSIÓN DE LISTAS
# ============================================================
print("\n=== 12) COMPRENSIÓN DE LISTAS ===")

cuadrados = [x**2 for x in range(5)]
pares = [x for x in range(10) if x % 2 == 0]

print("Cuadrados:", cuadrados)
print("Pares:", pares)


# ============================================================
# 13) ZIP / MAP / FILTER
# ============================================================
print("\n=== 13) ZIP / MAP / FILTER ===")

print("zip():", list(zip([1, 2], ["a", "b"])))
print("map():", list(map(lambda x: x * 2, [1, 2, 3])))
print("filter():", list(filter(lambda x: x > 2, [1, 2, 3, 4])))


# ============================================================
# 14) CONVERSIÓN A LISTA
# ============================================================
print("\n=== 14) CONVERSIÓN A LISTA ===")

print("Desde tupla:", list((1, 2, 3)))
print("Desde set:", list({1, 2, 3}))
print("Desde string:", list("hola"))


# ============================================================
# 15) DESEMPAQUETADO
# ============================================================
print("\n=== 15) DESEMPAQUETADO ===")

a, b, c = [10, 20, 30]
print("a, b, c:", a, b, c)

a, *resto = [1, 2, 3, 4]
print("a y resto:", a, resto)

*inicio, ultimo = [1, 2, 3, 4]
print("inicio y último:", inicio, ultimo)


# ============================================================
# 16) COMPARACIONES
# ============================================================
print("\n=== 16) COMPARACIONES ===")

print("[1, 2] == [1, 2]:", [1, 2] == [1, 2])
print("[1, 2] < [1, 3]:", [1, 2] < [1, 3])
