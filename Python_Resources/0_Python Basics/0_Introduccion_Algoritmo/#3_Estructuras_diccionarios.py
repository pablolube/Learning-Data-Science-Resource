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

# ============================================================
#           DICCIONARIOS EN PYTHON – GUÍA COMPLETA
# ============================================================

# ------------------------------------------------------------
# 1) CREACIÓN DE DICCIONARIOS
# ------------------------------------------------------------
dic_vacio = {}
dic = {"a": 1, "b": 2, "c": 3}
dic2 = dict(x=10, y=20)
dic3 = dict([("a", 1), ("b", 2)])

print("\n1) CREACIÓN DE DICCIONARIOS")
print("dic_vacio:", dic_vacio)
print("dic:", dic)
print("dic2:", dic2)
print("dic3:", dic3)


# ------------------------------------------------------------
# 2) ACCESO A VALORES
# ------------------------------------------------------------
print("\n2) ACCESO A VALORES")
print("dic['a']:", dic["a"])
print("dic.get('a'):", dic.get("a"))
print("dic.get('z', 0):", dic.get("z", 0))


# ------------------------------------------------------------
# 3) AGREGAR Y MODIFICAR ELEMENTOS
# ------------------------------------------------------------
dic["d"] = 4
dic["a"] = 100
dic.update({"e": 5, "f": 6})

print("\n3) AGREGAR Y MODIFICAR")
print("dic actualizado:", dic)


# ------------------------------------------------------------
# 4) ELIMINAR ELEMENTOS
# ------------------------------------------------------------
del dic["b"]
valor = dic.pop("a")
dic.pop("x", None)
ultimo = dic.popitem()

print("\n4) ELIMINAR ELEMENTOS")
print("Valor eliminado con pop('a'):", valor)
print("Último par eliminado (popitem):", ultimo)
print("Diccionario final:", dic)


# ------------------------------------------------------------
# 5) CONSULTA Y BÚSQUEDA
# ------------------------------------------------------------
print("\n5) CONSULTA Y BÚSQUEDA")
print("'c' in dic:", "c" in dic)
print("'z' not in dic:", "z" not in dic)
print("Claves:", dic.keys())
print("Valores:", dic.values())
print("Items:", dic.items())


# ------------------------------------------------------------
# 6) RECORRER DICCIONARIOS
# ------------------------------------------------------------
print("\n6) RECORRER DICCIONARIOS")
for clave in dic:
    print("Clave:", clave)

for valor in dic.values():
    print("Valor:", valor)

for clave, valor in dic.items():
    print(f"{clave} => {valor}")


# ------------------------------------------------------------
# 7) COPIAR DICCIONARIOS
# ------------------------------------------------------------
copia1 = dic.copy()
copia2 = dict(dic)
referencia = dic

print("\n7) COPIAR DICCIONARIOS")
print("Copia con copy():", copia1)
print("Copia con dict():", copia2)
print("Referencia (no copia):", referencia)


# ------------------------------------------------------------
# 8) COMBINAR DICCIONARIOS
# ------------------------------------------------------------
d1 = {"a": 1}
d2 = {"b": 2}

d3 = d1 | d2
d4 = {**d1, **d2}

print("\n8) COMBINAR DICCIONARIOS")
print("Con operador | :", d3)
print("Con ** :", d4)


# ------------------------------------------------------------
# 9) FUNCIONES BUILT-IN
# ------------------------------------------------------------
nums = {"a": 3, "b": 7, "c": 1}

print("\n9) FUNCIONES BUILT-IN")
print("len:", len(nums))
print("max (clave):", max(nums))
print("min (clave):", min(nums))
print("sum (valores):", sum(nums.values()))
print("any:", any(nums.values()))
print("all:", all(nums.values()))


# ------------------------------------------------------------
# 10) DICCIONARIOS ANIDADOS
# ------------------------------------------------------------
alumno = {
    "nombre": "Pablo",
    "edad": 20,
    "notas": {
        "math": 8,
        "prog": 9
    }
}

print("\n10) DICCIONARIOS ANIDADOS")
print("Nombre:", alumno["nombre"])
print("Nota de programación:", alumno["notas"]["prog"])


# ------------------------------------------------------------
# 11) DICCIONARIOS POR COMPRENSIÓN
# ------------------------------------------------------------
cuadrados = {x: x**2 for x in range(5)}
pares = {x: x for x in range(10) if x % 2 == 0}

print("\n11) DICCIONARIOS POR COMPRENSIÓN")
print("Cuadrados:", cuadrados)
print("Pares:", pares)


# ------------------------------------------------------------
# 12) setdefault()
# ------------------------------------------------------------
dic = {}
dic.setdefault("a", 0)
dic.setdefault("a", 100)

print("\n12) SETDEFAULT")
print("Diccionario:", dic)


# ------------------------------------------------------------
# 13) CONVERSIÓN A DICCIONARIO
# ------------------------------------------------------------
print("\n13) CONVERSIÓN A DICCIONARIO")
print("Desde lista de tuplas:", dict([("a", 1), ("b", 2)]))
print("Desde zip:", dict(zip(["x", "y"], [10, 20])))


# ------------------------------------------------------------
# 14) ORDENAR DICCIONARIOS
# ------------------------------------------------------------
dic = {"a": 3, "b": 1, "c": 2}

print("\n14) ORDENAR DICCIONARIOS")
print("Ordenado por clave:", sorted(dic))
print("Items ordenados:", sorted(dic.items()))
print("Ordenado por valor:", sorted(dic.items(), key=lambda x: x[1]))


# ------------------------------------------------------------
# 15) COMPARACIÓN DE DICCIONARIOS
# ------------------------------------------------------------
print("\n15) COMPARACIÓN DE DICCIONARIOS")
print("Iguales:", {"a": 1, "b": 2} == {"b": 2, "a": 1})
print("Distintos:", {"a": 1} != {"a": 2})


# ------------------------------------------------------------
# 16) EJEMPLO PRÁCTICO – CONTAR OCURRENCIAS
# ------------------------------------------------------------
texto = "hola mundo"
contador = {}

for letra in texto:
    contador[letra] = contador.get(letra, 0) + 1

print("\n16) CONTAR OCURRENCIAS")
print("Texto:", texto)
print("Conteo:", contador)
