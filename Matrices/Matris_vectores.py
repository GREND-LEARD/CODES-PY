def muestra(F,C,FC):
    print ("matriz resultante")
    for i in range (F):
        for j in range (C):
            print (FC[1][j], end =" ")
        print()


def remplazo(vector,FC):
    leng=len(vector)
    for i in range (leng):
        for j in range (leng):
            FC[1][j]= vector [j]
    return FC


def original(F,C,FC):
    print ("matriz original")
    for i in range (F):
        for j in range (C):
            print (FC[1][j], end =" ")
        print()




def matrizfc(FC,F,C):
    for i in range (F):
        FC.append([])
        for j in range (C):
            FC[i].append(0)
    return FC

def vectororiginal(vector):
    print (" vector original ")


def vectorn (N,vector):
        for i in range(N):
            x= int(input("ingrese el valor : "))
            vector.append(x)
            return vector



def programa ():
    vector =[]
    FC = []
    N= int(input("ingrese la cantidad de valores del vector: "))
    F= int(input("ingresse el valor de filas: "))
    C= int(input("ingrese el valor de columnas: "))
    vectorn (N,vector)
    vectororiginal (vector)
    matrizfc (FC,F,C)
    original (F,C,FC)
    remplazo (vector,FC)
    muestra (F,C,FC)
programa()  # se llama a la función programa para que ejecute todo el programa.

    # Llenado del vector

