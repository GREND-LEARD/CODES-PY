nombre = input("Ingrese el nombre del cliente: ")
productos = int(input("Ingrese la cantiga del producto: " ))
precio = float(input("Ingrese el precio de los productos: "))

linea="="*70

cancelar=productos*precio
print ()
print(linea)
print() 

print("Nombres del cliente:",nombre)
print("Cantidad de productos:",productos)
print(linea)
print("monto cancelar:",cancelar)

if productos:
    (productos > 1)
    print ("Producto adicional")

else:
    print("No se realizaron ventas")