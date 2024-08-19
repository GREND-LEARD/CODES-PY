lista=[]
# 1 
acumulador=0
contador=0
# 2
menor=1000
cedula_menor=0
nombre_menor=""
# 3
menores=0
# 4
edades_registradas=0
edad_registro=0

#inicio del programa

x=int(input("ingrese la cantidad de alumnos que quiera registar: "))
for i in range (x):
    nombre=input("ingrese nombre: ")
    cedula=int(input("ingrese la identificacion del estudiante: "))
    edad=int(input("ingrese la edad del estudiante: "))
    seccion=int(input("ingrese la seccion del estudiante: "))
    acumulador+=edad
    contador+=1
    # 1
    promedio=acumulador/contador
    # 2
    if edad<menor:
        menor=edad
        cedula_menor=cedula
        nombre_menor=nombre
    # 3
    if edad>promedio:
        menores+=1  
    #4
    if edad != edad_registro:
        edad_registro=edad
        edades_registradas+=1
        lista.append(edad)
print ("edad media de la seccion "+str (promedio))
print(nombre_menor," ",cedula_menor, "es el menor de todos con: ",menor, "años")
print ("cantidad de alumnos cuya edad es menor que el promedio: ",menores)
print(lista)