
#Int = Numeros enteros
#FLoat = Numeros decimales


x = int(input("Ingrese el primer valor: "))
y = int(int(input("Ingrese el segundo valor: ")))

"""""
suma = x+y
resta = x-y
multi = x*y
division = x/y
"""""

print("MENU")
print("1 - Suma")
print("2 - Resta")
print("3 - Multi")
print("4 - Division")

opcion = int(input("Ingrese una opcion: "))


# (opcion==1) = Exactamente igual a uno

if (opcion==1):
    suma=x+y
    print ("La sumatoria es: " + str(suma)) 

elif (opcion==2):
    resta= x-y
    print ("La resta es: "+ str(resta))
    
elif (opcion==3):
    multi=x*y
    print ("El producto es: " + str(multi))
    
elif (opcion==4):
    division=x/y
    print ("La division es: " + str(division))

else:
    print ("Ingrese una opcion valida")