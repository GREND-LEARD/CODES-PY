# (while) = mientras , mientras se cumpla la condicion se repite cuantas veces

"""""
acumulador =0
x = 1 
while(x==1):
    print ("hola")
    x=int(input("ingrese el valor a cambiar x: "))
    acumulador+=x
print("programa terminado")
print("acumulador: ",acumulador)
"""""
"""""
contador=0
x= "hola"
while (x == "hola"):
    contador +=1
    print ("adios")
    x=input("ingrese la frase para cambiar x: ")
print("programa terminado")
print("cantidad de veces repetidas",contador)
"""""


numero = 0
suma = 0

while (numero <= 10):
    suma = numero + suma
    numero = numero + 1
    print ("La suma es " + str(suma))
    
    print("programa terminado")
    