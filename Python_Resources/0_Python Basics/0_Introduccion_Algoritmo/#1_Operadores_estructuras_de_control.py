

"""
* EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""


# * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
"""   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits..."""

#Aritmeticos

print(f"Suma: 10 + 3={10 + 9}")
print(f"Resta: 10 - 3={10 - 9}")
print(f"Multiplicacion: 10 * 3={10 * 9}")
print(f"Division: 10 / 3={10 / 9}")
print(f"Modulo: 10 % 3={10 % 9}")
print(f"Division Entera: 10 // 3={10 // 9}")
print(f"Potencia: 10 **2= {10 ** 2}")


#Logicos
print(f"Operador OR  { 10+3==12 and 5-1==4}")
print(f"Operador AND { 10+3==12 or 5-1==4}")
print(f"Operador NOT  {not 10+3==14}")


#Comparacion
print(f"Igualdad == {10 == 9}")
print(f"Desigualdad != {10 != 9}")
print(f"Mayor Igual >=  {10 >= 9}")
print(f"Menor Igual <= {10 <= 9}")
print(f"Mayor  >  {10 > 9}")
print(f"Menor < {10 < 9}")

# Operadores de asignación
my_number = 11  # asignación
print(my_number)
my_number += 1  # suma y asignación
print(my_number)
my_number -= 1  # resta y asignación
print(my_number)
my_number *= 2  # multiplicación y asignación
print(my_number)
my_number /= 2  # división y asignación
print(my_number)
my_number %= 2  # módulo y asignación
print(my_number)
my_number **= 1  # exponente y asignación
print(my_number)
my_number //= 1  # división entera y asignación
print(my_number)

#Operadores de identidad
# Esto te muestra si ocupan el mismo deposito de memoria
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
# Trabajo como conjuntos si pertenecen o no al conjunto

print(f"'u' in 'mouredev' = {'u' in 'mouredev'}")
print(f"'b' not in 'mouredev' = {'b' not in 'mouredev'}")

# Operadores de bit
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010 
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001 
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

"""
Estructuras de control    


 Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
Condicionales, iterativas, excepciones...
 Debes hacer print por consola del resultado de todos los ejemplos.

"""
#Estructuras de control

#Condicionales
# IF - IF/ELSE - IF-elif-else

my_string="Pablo"
if my_string == "Pablo":
    print("Esta persona es pablo")
elif my_string=="Juan":
    print("Este es  Juan")
else: 
    print("No es ninguno de los 2")

#CONDICIONAL TERNARIO 
edad=20
mensaje = "Mayor" if edad >= 18 else "Menor"

#MATCH AND CASE
opcion="5"
opcion=input("Ingrese su opcion ")
match opcion:
    case "1":
        print ("Opcion 1 - Guardar Archivo")
    case  "2":
        print ("Opcion 2 - Eliminar Archivo")
    case "3":
        print ("Opcion 3 - Salir del programa")
    case _:
        print ("Error OPCION NO EXISTE")
####################################################################
#Bucle While 
####################################################################

#while clasico
i = 0
while i < 5:
    print(i)
    i += 1

#while infinto
while True:
    opcion=input("Ingrese para Terminar")
    if opcion=="Salir":
        break

#Otro while con break
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1

#While anidado 
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, j)
        j += 1
    i += 1

print("""
####################################################################
# FOR
####################################################################
""")

for i in range(5):
    print(i)

for letra in "Python":
    print(letra)

print("""
####################################################################
# CONTROL DE FLUJOS
####################################################################
""")

#BREAK
for i in range(10):
    if i == 5:
        break
    print(i)


#CONTINUE
for i in range(5):
    if i == 2:
        continue
    print(i)


#PASS
if edad > 18:
    pass

print("""
####################################################################
# CONTROL CON EXCEPCIONES
####################################################################
""")
# try - except 
try:
    x = int("abc")
except ValueError:
    print("Error de conversión")

# try - except - ELSE
try:
    x = int("10")
except ValueError:
    print("Error")
else:
    print("Conversión correcta")

# try - except - finally
try:
    archivo = open("datos.txt")
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    print("Fin del proceso")

#  Estructuras de control con contexto

with open ("Archivo",r) as archivo:
    contenido=archivo.read()

"""
Actividad Extra
"""
for i in range(10,56):
    if i %2==0 and i!=16 and i %3==0:
        print(i)
