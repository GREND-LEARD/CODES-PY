# listas-vectores ingresar datos dentro de ellas 
# cada objeto es independiente no depende de una key cada objeto es unico 

lista =["hola","amigo"]
print (lista)
print(lista[0],lista[1]) #lista tipo string

lista_enteros=[1,2,3,4,5,6,7,8,9,10]
print(lista_enteros) #lista de tipo enteros

enteros=[]   # 1. lista vacia, depende de x
acumulador=0 # 4. aqui sumara los valores acumulados
x=int(input("ingrese la cantidad de valores en la lista: ")) #2. esto es la cantidad de datos, no el dato
for i in range (x):
    y=int(input("ingrese el valor: ")) #3.  valores ingresados dependen de aqui
    acumulador+=y
    enteros.append(y) # 5. se ingresaran los valores a la lista
print (enteros)
print("acumulador",acumulador)

print (enteros[-1])