cliente =input ("ingrese si para facturar un cliente: ")
while (cliente == "si" or cliente == "SI" or cliente == "sI" or cliente == "Si"):
    contador=0               #los contadores van siempre aqui arriba
    acumulador=0             #los acumuladores van siempre aqui abajo
    nombre = input ("ingrese el nombre del cliente: ") #esto ya es dominio del while
    cantidad = int(input("ingresar la cantidad de productos que lleva: ")) 
    for i in range (cantidad):            #ciclo anidados uno dentro de otro
        contador+=1
        print ("precio del producto ",contador)
        precio = float(input("ingrese el precio del producto: "))
        acumulador+=precio
    print ("monto total a cancelar",acumulador)
    cliente = input ("ingrese si para facturar a otro cliente: ")
print ("programa terminado")


#entender los dominios, mientras estemos en el dominio de un ciclo o una condicion siempre estaremos dentro 