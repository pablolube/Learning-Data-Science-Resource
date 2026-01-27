"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */

"""

# ============================================================
#           RECURSIVIDAD EN PYTHON – APUNTE COMPLETO
# ============================================================

print("\n================================================")
print("RECURSIVIDAD: CASOS DE USO Y EJEMPLOS EN PYTHON")
print("================================================")


# ============================================================
# 1) CONTAR HACIA ATRÁS (EJEMPLO BÁSICO)
# ============================================================


print("\n1) CONTAR HACIA ATRÁS")

def contar_para_atras(start):
    int(start)
    print(start)
    if start==0:
        return
        
    else:
        contar_para_atras(start-1)
        
start = int(input("Ingrese un número: "))
print("Empieza  a contar")
contar_para_atras(start)

# ============================================================
# 2) SUMA RECURSIVA
 # ============================================================
print("\n2) SUMA RECURSIVA")

def suma(n):
    if n == 0:
        return 0
    return n + suma(n - 1)

print("Resultado suma(5):", suma(5))



###############################
# 2 BIS  SUMATORIA LISTA 
##################################

lista = []
while True:
    entrada = input('Ingresa números para sumar, para terminar ingresa "F": ')
    
    if entrada.upper() == "F":  # Acepta "f" o "F"
        break  # Sale del bucle
    
    try:
        valor = int(entrada)
        lista.append(valor)
    except ValueError:
        print("¡Eso no es un número válido!")
        
print("Lista final:", lista)
print("Suma:", sum(lista))


def suma_recursiva(lista):
    if not lista:
        return 0
    else:
        return lista[0]+suma_recursiva(lista[1:])
    

#  ============================================================
# 3) FACTORIAL (PROBLEMA MATEMÁTICO)
# ============================================================
print("\n3) FACTORIAL")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial de 5:", factorial(5))


# ============================================================
# 4) RECORRER UNA LISTA
# ============================================================
print("\n4) RECORRER LISTA")

def recorrer_lista(lista, i=0):
    if i == len(lista):
        print("Fin de la lista")
        return
    print("Elemento:", lista[i])
    recorrer_lista(lista, i + 1)

recorrer_lista([10, 20, 30, 40])


# ============================================================
# 5) BUSCAR UN ELEMENTO EN UNA LISTA
# ============================================================
print("\n5) BÚSQUEDA RECURSIVA")

def buscar(lista, valor, i=0):
    if i == len(lista):
        return False
    if lista[i] == valor:
        return True
    return buscar(lista, valor, i + 1)

print("Buscar 30:", buscar([10, 20, 30, 40], 30))
print("Buscar 99:", buscar([10, 20, 30, 40], 99))


# ============================================================
# 6) PROCESAR LISTAS ANIDADAS
# ============================================================
print("\n6) LISTAS ANIDADAS")

def aplanar(lista):
    for elemento in lista:
        if isinstance(elemento, list):
            aplanar(elemento)
        else:
            print("Elemento:", elemento)

aplanar([1, [2, [3, 4]], 5])


# ============================================================
# 7) MÁXIMO DE UNA LISTA (DIVIDE Y VENCERÁS)
# ============================================================
print("\n7) MÁXIMO DE UNA LISTA")

def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    resto_max = maximo(lista[1:])
    return lista[0] if lista[0] > resto_max else resto_max

print("Máximo:", maximo([3, 7, 2, 9, 1]))


# ============================================================
# 8) FIBONACCI (EJEMPLO CLÁSICO)
# ============================================================
print("\n8) FIBONACCI")

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(6):", fibonacci(6))


# ============================================================
# 9) GRAFO – DFS (RECORRIDO EN PROFUNDIDAD)
# ============================================================
print("\n9) DFS EN GRAFOS")

grafo = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

def dfs(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()

    if nodo in visitados:
        return

    visitados.add(nodo)
    print("Visitando:", nodo)

    for vecino in grafo[nodo]:
        dfs(grafo, vecino, visitados)

dfs(grafo, "A")


# ============================================================
# 10) BACKTRACKING – PERMUTACIONES
# ============================================================
print("\n10) PERMUTACIONES")

def permutar(lista):
    if len(lista) == 1:
        return [lista]

    resultado = []
    for i in range(len(lista)):
        resto = lista[:i] + lista[i+1:]
        for p in permutar(resto):
            resultado.append([lista[i]] + p)
    return resultado

print("Permutaciones de [1,2,3]:")
for p in permutar([1, 2, 3]):
    print(p)


# ============================================================
# RESUMEN FINAL
# ============================================================
print("\n================================================")
print("RESUMEN DE RECURSIVIDAD")
print("================================================")

print("""
✔ Una función recursiva:
  - Se llama a sí misma
  - Tiene un CASO BASE
  - Reduce el problema en cada llamada

✔ Usos ideales:
  - Árboles
  - Grafos
  - Backtracking
  - Divide y vencerás
  - Problemas matemáticos

❌ No usar cuando:
  - Un bucle es más simple
  - La profundidad es muy grande
""")
