cuadrado=[]
for i in range(1,11):
    cuadrado.append(i*i)
print(cuadrado)

cuadrado = [i*i for i in range (1,11)]

estudiantes=[100,90,80,70,60,50,40,30,0]

#Con filter y lamda son list comprehension
estudiantes_aprobados=list(filter(lambda x:x>=60,estudiantes))

# Con list comprenhension
estudiantes_aprobados=[i for i in estudiantes if i>=60]