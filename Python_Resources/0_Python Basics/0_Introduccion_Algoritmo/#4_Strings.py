# ============================================================
#        OPERACIONES CON CADENAS (STRINGS) EN PYTHON
# ============================================================

print("\n================= 1) ASIGNACIÓN =================")
cadena = "Hola mundo"
print("Cadena original:", cadena)


# ============================================================
# 2) ACCESO Y SLICING
# ============================================================
print("\n================= 2) ACCESO Y SLICING =================")
print("cadena[1] ->", cadena[1])
print("cadena[:] ->", cadena[:])
print("cadena[0:2] ->", cadena[0:2])
print("cadena[::2] ->", cadena[::2])
print("cadena[::-1] (invertida) ->", cadena[::-1])


# ============================================================
# 3) RECORRIDO
# ============================================================
print("\n================= 3) RECORRIDO =================")
for c in cadena:
    print("Carácter:", c)


# ============================================================
# 4) DIVISIÓN (SPLIT)
# ============================================================
print("\n================= 4) SPLIT =================")
palabras = cadena.split(" ")
print("split(' '):", palabras)


# ============================================================
# 5) FORMATEO DE MAYÚSCULAS / MINÚSCULAS
# ============================================================
print("\n================= 5) FORMATEO =================")
print("upper():", cadena.upper())
print("lower():", cadena.lower())
print("capitalize():", cadena.capitalize())
print("swapcase():", cadena.swapcase())
print("title():", cadena.title())
print("casefold():", cadena.casefold())


# ============================================================
# 6) ELIMINAR ESPACIOS
# ============================================================
print("\n================= 6) ELIMINAR ESPACIOS =================")
print("strip():", cadena.strip())
print("lstrip():", cadena.lstrip())
print("rstrip():", cadena.rstrip())


# ============================================================
# 7) BÚSQUEDA Y CONSULTA
# ============================================================
print("\n================= 7) BÚSQUEDA =================")
#cadena.find(subcadena, inicio, fin)
print("find('mundo'):", cadena.find("mundo"))
print("count('o'):", cadena.count("o"))
print("startswith('Hola'):", cadena.startswith("Hola"))
print("endswith('mundo'):", cadena.endswith("mundo"))


# ============================================================
# 8) REEMPLAZO
# ============================================================
print("\n================= 8) REEMPLAZO =================")
print("replace('mundo','Python'):", cadena.replace("mundo", "Python"))


# ============================================================
# 9) UNIÓN (JOIN)
# ============================================================
print("\n================= 9) JOIN =================")
lista = ["Hola", "Mundo", "Python"]
print("Lista:", lista)
print("join():", " ".join(lista))


# ============================================================
# 10) VALIDACIONES (BOOLEANAS)
# ============================================================
print("\n================= 10) VALIDACIONES =================")
print("isalpha():", "Hola".isalpha())
print("isdigit():", "123".isdigit())
print("isalnum():", "Hola123".isalnum())
print("isspace():", "   ".isspace())
print("islower():", "hola".islower())
print("isupper():", "HOLA".isupper())
print("istitle():", "Hola Mundo".istitle())


# ============================================================
# 11) FORMATO DE STRINGS
# ============================================================
print("\n================= 11) FORMATO =================")
nombre = "Pablo"
edad = 25
print("format():", "Nombre: {}, Edad: {}".format(nombre, edad))
print("f-string:", f"Nombre: {nombre}, Edad: {edad}")


# ============================================================
# 12) ALINEACIÓN Y RELLENO
# ============================================================
print("\n================= 12) ALINEACIÓN =================")
print("center():", "Hola".center(20, "-"))
print("ljust():", "Hola".ljust(10, "."))
print("rjust():", "Hola".rjust(10, "."))


# ============================================================
# 13) TABULACIONES
# ============================================================
print("\n================= 13) TABULACIONES =================")
print("expandtabs():", "Hola\tMundo".expandtabs(10))


# ============================================================
# 14) PARTICIÓN
# ============================================================
print("\n================= 14) PARTICIÓN =================")
print("partition('mundo'):", cadena.partition("mundo"))
print("rpartition('o'):", cadena.rpartition("o"))


# ============================================================
# 15) CODIFICACIÓN
# ============================================================
print("\n================= 15) CODIFICACIÓN =================")
print("encode('utf-8'):", "Hola".encode("utf-8"))


# ============================================================
# 16) PREFIJOS Y SUFIJOS (Python 3.9+)
# ============================================================
print("\n================= 16) PREFIJO / SUFIJO =================")
print("removeprefix('Hola '):", cadena.removeprefix("Hola "))
print("removesuffix(' mundo'):", cadena.removesuffix(" mundo"))


# ============================================================
# 17) EJEMPLO EXTRA DE SLICING
# ============================================================
print("\n================= 17) SLICING EXTRA =================")
s = "Python"
print("s[0]:", s[0])
print("s[-1]:", s[-1])
print("s[1:4]:", s[1:4])
print("s[::-1] (invertida):", s[::-1])
