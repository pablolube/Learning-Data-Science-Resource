#Operador Warlus

print(feliz:=True)

# Proceso sin warlus
comidas=[]
while True:
    comida=input("¿Que comida le gusta?")
    if comida=="salir":
        break
    comidas.append(comida)


for comida in comidas:
    print(comida)

# Proceso con Warlus
comidas=[]
while (comida:=input("¿Que comida te gusta?"))!="salir":
    comidas.append(comida)

for comida in comidas:
    print(comida)

