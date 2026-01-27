
#--------------------------------------------------------------------
# VERIFICACION DE EXISTENCIA DE ARCHIVOS
#--------------------------------------------------------------------
import os
path= "C:\\Users\\Usuario\\Desktop\\test.txt"
if os.path.exists(path):
    print ("Existe")
    if os.path.isfile(path):
        print("es un archivo")
    if os.path.isdir(path):
        print("es un archivo")
    else:
        print("No es una carpeta")   
else:
    print("No existe")


#--------------------------------------------------------------------
# LECTURA DE ARCHIVOS
#--------------------------------------------------------------------

with open(path) as file:
    print(file.read())
print(file.closed) # Para saber si esta cerado 

try:
    with open('test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("El archivo no ha sido encontrado")


#--------------------------------------------------------------------
# Agregar y leer archivos en python
#--------------------------------------------------------------------
texto="Hola el secreto de la vida es \n, esto es un poco de texto \n que tengas un buen dia bebe"
with open(path,"w+") as file:
    file.write(texto)
    file.seek(0)
    print(file.read())


#--------------------------------------------------------------------
# Copiar archivos
#--------------------------------------------------------------------

"""Utilizaremos el modulo shutil que tiene 3 metodos"""
#shutil.copyfile(src, dst)  # solo contenido
#shutil.copy(src, dst)      # contenido + permisos
#shutil.copy2(src, dst)     # contenido + permisos + metadata (fecha, etc.)
import shutil
origen = "archivos/text.txt"
shutil.copyfile(origen,"archivos/copy.txt")

# Mover archivos
origen="archivos/text2.txt"
destino="archivosdestino/text2.txt"
try:
    if os.path.exists(destino):
        print("Ya hay un archivo en este destino!")
    else:
        os.replace(origen,destino)
        print(origen + "El origen fue movido")
except FileNotFoundError:
    print (origen + " No fue encontrado " )


#--------------------------------------------------------------------
# Mover directorios (sobreescribe)
#--------------------------------------------------------------------
origen="folder"
destino="archivosdestino/folder"
try:
    if os.path.exists(destino):
        print("Ya existe una carpeta en el destino")
    else:
        os.replace(origen,destino)
        print(origen + "El origen fue movido")
except FileNotFoundError:
    print (origen + " No fue encontrado " )

#--------------------------------------------------------------------
# Mueve sin sobreescribir 
#--------------------------------------------------------------------


import shutil
import os

origen = "archivos/text2.txt"
destino = "archivosdestino/text2.txt"

if os.path.exists(destino):
    print("❌ Ya existe un archivo con ese nombre")
else:
    shutil.move(origen, destino)
    print("✅ Archivo movido sin sobrescribir")


#--------------------------------------------------------------------

#--------------------------------------------------------------------
try:       
    os.remove("archivosdestinos/text2")
except FileNotFoundError:
    print (origen + " No fue encontrado " )
except PermissionError:
    print ("Lo siento no tienes permiso para eliminar esta carpeta" )000


##--------------------------------------------------------------------
# BORRAR CARPETA VACIA (SALVAND ERROR CON REMOVE)
##--------------------------------------------------------------------

try:   
    os.remove("archivosdestinos/text2")
except FileNotFoundError:
    print (origen + " No fue encontrado " )
except PermissionError:
    print ("Lo siento no tienes permiso para eliminar esta carpeta" )


##--------------------------------------------------------------------
# BORRAR CARPETA VACIA (SALVAND ERROR CON REMOVE)
##--------------------------------------------------------------------


path= 'folder'
try:   
    os.remove(path) # elmina archivos
    os.rmdir(path) #elimina carpetas vacias
    shutil.removetree(path) # Elimina carpetas con todo su contenido y subcarpetads  OJO no va a la papelera
    os.rmdir("archivosdestinos/text2")
except FileNotFoundError:
    print (origen + " No fue encontrado " )
except PermissionError:
    print ("Lo siento no tienes permiso para eliminar esta carpeta" )
except OSError:
    print("No puedes eliminar eso usando esa funcion")
else:
    print(path )from send2trash import send2trash


# FUNCIONES PARA ENVIAR A LA PAPELERA

send2trash("archivo.txt")      # archivo
send2trash("carpeta")          # carpeta
send2trash("ruta/completa") 