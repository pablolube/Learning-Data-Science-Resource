nombre_usuarios=["Alex","Smith","Hermoso"]
contraseñas=("1234","Sh","o")
roles = ["Admin", "User", "Guest"]

usuarios_zip = zip(nombre_usuarios, contraseñas)

usuarios_lista = list(usuarios_zip)
usuarios_diccionario = dict(zip(nombre_usuarios, contraseñas))


print(usuarios_zip)
print(usuarios_lista)
print(usuarios_diccionario)


usuarios_zip3 = zip(nombre_usuarios, contraseñas,roles)
usuarios_lista3=list(usuarios_zip3)
print("ACA IMPRIME 3")
print(usuarios_lista3)