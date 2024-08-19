x = int(input("ingrese el primer valor: "))
y = int(input("ingrese el segundo valor: "))

if (x>y and x>=50):
    print(" X>Y asi que se suma y es mayor o igual a 50: ",x+y)

elif(x<y or x<0):
    print(" X<Y asi que se resta: ",x-y)
    
else:
    print(" X=Y asi que queda igual ")

    # (or) = es para cumplir una serie de condiciones
    # (and) = es para que todas las condiciones se cumplan = si o si
    # (not) = es para negar una serie de condiciones