def suma (x,y):
    suma = x + y
    print ("la sumatoria de los valores es: " ,suma)
def resta (x,y):
    resta = x - y
    print ("la resta de los valores es: " ,resta)

def multiplicacion (x,y):
    multiplicacion = x * y
    print ("el producto de los valores es: " ,multiplicacion)

def division (x,y):
    division = x / y
    print ("la division de los valores es :" ,division)

valor_1 = int(input("ingrese el primer digito: "))

valor_2 = int(input("ingrese el segundo digito: "))
print ("menu: ")
print ("1 - suma: ")
print ("2 - resta: ")
print ("3 - multiplicacion: ")
print ("4 - divicion: ")

opcion = int(input("ingrese la opcion: "))

if (opcion == 1): #si opcion es exactamente igual a "2 " entonces retorne suma
    suma(valor_1,valor_2)

elif (opcion == 2): #si opcion es exactamente igual a 
    resta(valor_1,valor_2)

elif (opcion == 3): #si opcion es exactamente igual a
    multiplicacion(valor_1,valor_2)

elif (opcion == 4): #si opcion es exactamente igual a
    division(valor_1,valor_2)

else:
    print ("opcion no valida")
