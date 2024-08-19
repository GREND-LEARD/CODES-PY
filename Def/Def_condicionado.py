#subprograma
def ciclo(x):
    contador=-1
    while(x == "si" or x== "SI" or x== "sI" or x=="Si"):
        contador+=1
        x = input ("ingrese si para repetir el ciclo: ") # manipilar variables que no estan dentro del ciclo
    print("veces repetidas: ",contador)



# ya sabemos la condicion
x = input ("ingrese si para ingresar al ciclo: ")
if (x == "si" or x== "SI" or x== "sI" or x=="Si"):
    print ("bienvenido")
    ciclo (x)

    #hola