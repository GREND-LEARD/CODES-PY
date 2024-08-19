lista=[]
n = int(input("ingrese la cantidad de valores de la lista: "))
xc= int(input("ingrese el valor a buscar: "))


vector=[] #se puede usar un vector para almacenar un mensaje que queiramos mostrar que hace referencia a la primera lista


for i in range(n):
    nc=int(input("ingrese el valor al conjunto: "))
    lista.append(nc) # funcion para agregar valores a una lista .append
    if nc == xc:
        vector.append("el valor de x: "+str(xc)+ " esta en el conjunto en la posicion: "+str(i+1)) 
print(vector)