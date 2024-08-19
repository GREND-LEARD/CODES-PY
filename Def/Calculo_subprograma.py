def sumadas (valor_1,valor_2):
    suma = x+y
    return suma # es una funcion para almacenar valores que se devuelven a la variable principal
def porciento (porcentaje):
    porcentaje= suma *1.10
    return porcentaje

x = int(input("ingrese el primer valor: "))
y= int(input("ingrese el segundo valor: "))

suma=sumadas (x,y)
porcentaje=porciento(suma)  #para hacer que el valor de la funcion se almacene en la variable se hace con retourn

print ("la sumatoria es de: ",suma)

print ("el porcentaje es del 10% de la sumatoria es de: ",porcentaje)

#el retourn devuelve los valores selccionados