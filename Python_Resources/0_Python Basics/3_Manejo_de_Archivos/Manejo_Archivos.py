with open ("archivo.txt",'r+') as archivo:
    contenido=archivo.read(10)
    
    print("Contenido inicial del archivo 1:", contenido)
    archivo.seek(5,0)
    archivo.write("Nuevo Contenido." + contenido )
    archivo.seek(0)
    contenido2=archivo.read()
    print(archivo.tell())
    print(contenido2)
    
with open("+mi archivo.txt","r") as archivo:
    linea1=archivo.readline()
    linea2=archivo.readline()
    print("Linea 1",linea1)
    print("Linea 2",linea2)
    archivo.seek(0)
    lineas=archivo.readlines()
    print("usando redlines",lineas)