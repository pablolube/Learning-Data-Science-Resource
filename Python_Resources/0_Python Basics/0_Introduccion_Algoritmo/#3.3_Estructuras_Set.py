# ============================================================
#               OPERACIONES CON SET EN PYTHON
# ============================================================

# ------------------------------------------------------------
# 1) CREACIÓN DE SETS
# ------------------------------------------------------------
set1 = {1, 2, 3, 4}
set2 = set([3, 4, 5, 6])
set_vacio = set()   # ⚠️ {} crea un diccionario

print("\n1) CREACIÓN")
print("set1:", set1)
print("set2:", set2)
print("set vacío:", set_vacio)


# ------------------------------------------------------------
# 2) CARACTERÍSTICAS IMPORTANTES
# ------------------------------------------------------------
print("\n2) CARACTERÍSTICAS")
print("No permite duplicados:", {1, 1, 2, 2, 3})
print("No mantiene orden")


# ------------------------------------------------------------
# 3) AGREGAR ELEMENTOS
# ------------------------------------------------------------
set1.add(10)
print("\n3) ADD")
print("Agregar un elemento:", set1)

set1.update([20, 30])
print("Agregar varios (update):", set1)


# ------------------------------------------------------------
# 4) ELIMINAR ELEMENTOS
# ------------------------------------------------------------
set1.remove(10)     # ❌ error si no existe
print("\n4) REMOVE")
print("Después de remove:", set1)

set1.discard(99)    # ✅ no da error
print("Después de discard (no existe):", set1)

elem = set1.pop()   # elimina un elemento aleatorio
print("POP (elemento eliminado):", elem)
print("Set actual:", set1)

set1.clear()
print("CLEAR (vaciar set):", set1)


# ------------------------------------------------------------
# 5) COPIAR SETS
# ------------------------------------------------------------
original = {1, 2, 3}
copia = original.copy()
referencia = original

print("\n5) COPIAR")
print("Original:", original)
print("Copia:", copia)
print("Referencia:", referencia)


# ------------------------------------------------------------
# 6) CONSULTA Y BÚSQUEDA
# ------------------------------------------------------------
setA = {1, 2, 3, 4}

print("\n6) CONSULTA")
print("¿2 está en el set?:", 2 in setA)
print("¿9 NO está en el set?:", 9 not in setA)
print("Cantidad de elementos:", len(setA))

# ORDEN DE SET

s = {3, 1, 4, 2}

ordenado = sorted(s)

print("Set original:", s)
print("Lista ordenada:", ordenado)


# ------------------------------------------------------------
# 7) OPERACIONES ENTRE SETS (MATEMÁTICAS)
# ------------------------------------------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\n7) OPERACIONES MATEMÁTICAS")
print("A:", A)
print("B:", B)

# Unión
print("Unión (A | B):", A | B)
print("Unión (A.union(B)):", A.union(B))

# Intersección
print("Intersección (A & B):", A & B)
print("Intersección (A.intersection(B)):", A.intersection(B))

# Diferencia
print("Diferencia (A - B):", A - B)
print("Diferencia (A.difference(B)):", A.difference(B))

# Diferencia simétrica
print("Dif. simétrica (A ^ B):", A ^ B)
print("Dif. simétrica (A.symmetric_difference(B)):", A.symmetric_difference(B))


# ------------------------------------------------------------
# 8) RELACIONES ENTRE SETS
# ------------------------------------------------------------
C = {1, 2}
D = {1, 2, 3, 4}

print("\n8) RELACIONES")
print("C es subconjunto de D:", C.issubset(D))
print("D es superconjunto de C:", D.issuperset(C))
print("C y D son disjuntos:", C.isdisjoint({5, 6}))


# ------------------------------------------------------------
# 9) OPERACIONES IN-PLACE (MODIFICAN EL SET)
# ------------------------------------------------------------
E = {1, 2, 3}
F = {3, 4, 5}

print("\n9) OPERACIONES IN-PLACE")
print("E inicial:", E)

E |= F
print("E |= F (unión):", E)

E &= {3, 4}
print("E &= {3,4} (intersección):", E)

E -= {4}
print("E -= {4} (diferencia):", E)

E ^= {10, 3}
print("E ^= {10,3} (dif. simétrica):", E)


# ------------------------------------------------------------
# 10) ITERAR SETS
# ------------------------------------------------------------
print("\n10) ITERAR")
for elemento in {10, 20, 30}:
    print("Elemento:", elemento)


# ------------------------------------------------------------
# 11) COMPRENSIÓN DE SETS
# ------------------------------------------------------------
print("\n11) COMPRENSIÓN")
cuadrados = {x**2 for x in range(5)}
pares = {x for x in range(10) if x % 2 == 0}

print("Cuadrados:", cuadrados)
print("Pares:", pares)


# ------------------------------------------------------------
# 12) FUNCIONES BUILT-IN CON SETS
# ------------------------------------------------------------
nums = {3, 7, 1, 9}

print("\n12) BUILT-IN")
print("len:", len(nums))
print("max:", max(nums))
print("min:", min(nums))
print("sum:", sum(nums))
print("any:", any(nums))
print("all:", all(nums))


# ------------------------------------------------------------
# 13) CONVERSIÓN A SET
# ------------------------------------------------------------
print("\n13) CONVERSIÓN")
print("Desde lista:", set([1, 2, 2, 3]))
print("Desde tupla:", set((4, 5, 5)))
print("Desde string:", set("hola"))


# ------------------------------------------------------------
# 14) FROZENSET (SET INMUTABLE)
# ------------------------------------------------------------
fs = frozenset([1, 2, 3])

print("\n14) FROZENSET")
print("FrozenSet:", fs)
# fs.add(4)  ❌ Error: es inmutable
