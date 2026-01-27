"""
===========================================
APUNTE – COMPREHENSION DE DICCIONARIOS
===========================================

Sintaxis general:
diccionario = {
    clave: expresion
    for clave, valor in iterable
    if condicion_opcional
}

• iterable suele ser un diccionario usando .items()
• .items() devuelve pares (clave, valor)
• Se puede aplicar lógica, fórmulas o funciones
"""

# ------------------------------------------------
# EJEMPLO 1: CONVERSION DE TEMPERATURAS
# ------------------------------------------------
# Diccionario original en grados Fahrenheit
# NOTA: claves duplicadas se sobrescriben automáticamente
ciudades_en_f = {
    'New York': 32,
    'Orlando': 32,
    'Chicago': 75,
    'Los Angeles': 100,
    'Nueva Orleados': 50
}

# Formula de conversión:
# °C = (°F − 32) × 5 / 9
ciudades_en_c = {
    ciudad: (fahrenheit - 32) * 5 / 9
    for ciudad, fahrenheit in ciudades_en_f.items()
}

print("Temperaturas en Celsius:")
print(ciudades_en_c)


# ------------------------------------------------
# EJEMPLO 2: FILTRADO DE DICCIONARIOS
# ------------------------------------------------
# Diccionario con estado del clima
clima = {
    'New York': 'Nieve',
    'Nordelta': 'Soleado',
    'Boston': 'Soleado',
    'Kenedy': 'Nublado'
}

# Se filtran solo las ciudades con clima "Soleado"
# IMPORTANTE: usar == para comparar
clima_soleado = {
    ciudad: estado
    for ciudad, estado in clima.items()
    if estado == 'Soleado'
}

print("\nCiudades con clima soleado:")
print(clima_soleado)


# ------------------------------------------------
# EJEMPLO 3: CONDICIONAL DENTRO DE LA EXPRESION
# ------------------------------------------------
# Clasificación térmica según temperatura en °C
# Operador ternario:
# valor_si_true if condicion else valor_si_false
frio_calor = {
    ciudad: ("Calor" if temperatura >= 10 else "Frio")
    for ciudad, temperatura in ciudades_en_c.items()
}

print("\nClasificación Frio / Calor:")
print(frio_calor)


# ------------------------------------------------
# EJEMPLO 4: USANDO UNA FUNCION
# ------------------------------------------------
# Función para evaluar temperatura en Fahrenheit
def check_temperatura(valor):
    """
    Devuelve una clasificación térmica:
    • >= 70  -> Calor
    • 40-60  -> Normal
    • < 40   -> Frio
    """
    if valor >= 70:
        return "Calor"
    elif 60 >= valor >= 40:
        return "Normal"
    else:
        return "Frio"


# Aplicación de la función dentro de la comprensión
como_esta = {
    ciudad: check_temperatura(temperatura)
    for ciudad, temperatura in ciudades_en_f.items()
}

print("\nEstado térmico según Fahrenheit:")
print(como_esta)
