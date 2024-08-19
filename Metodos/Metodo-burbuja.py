# para crear el metodo de burbuja necesitamos saber la cantidad de valores que tiene el vector

def ascendente(valor_de_vector): 
    leng=len (vector)-1 #esta es la funcion que indica el valor de la variable (vector)
    for i in range (0,leng):
        for j in range (0,leng):
            if vector[j]> vector[j+1]:
                aux=vector[j]
                vector[j]=vector[j+1]
                vector[j+1]=aux
    print ("forma ascendente")
    print (vector)


def decendente(valor_de_vector): 
    leng=len (vector)-1 #esta es la funcion que indica el valor de la variable (vector)
    for i in range (0,leng):
        for j in range (0,leng):
            if vector[j]< vector[j+1]:
                aux=vector[j]
                vector[j]=vector[j+1]
                vector[j+1]=aux
    print ("forma decendente")
    print (vector)

vector=[]
x=int(input("ingrese la cantidad de valores: "))
for i in range (x):
    y=int(input("ingrese el valor: "))
    vector.append(y)
print(vector)

ascendente(vector)
decendente(vector)

