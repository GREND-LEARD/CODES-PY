cantidad = int (input("ingrese la cantidad de productos: "))
precion =float (input("ingrese el precio: "))

pagar=cantidad*precion

if (cantidad >= 10 and cantidad <=20):
    descuento=pagar*0.80
    final=pagar-descuento
    print("el total a pagar es: ",final)

elif (cantidad >= 10):
    descuento=pagar*0.30
    final=pagar-descuento
    print("el total a pagar es: ",final)

else :
    print("el cliente no tiene descuento y paga",pagar)



# (opcional)
#if (cantidad > 10):
#    final=pagar*0.90
#    print("el total a pagar es: ",final)