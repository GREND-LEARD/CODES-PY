

"""""

Matriz 1

from random import*

filas=3
colomnas=3

a=[[randint(1,100) for i in range(filas)]for j in range(colomnas)] # "a" es la totalidad de mi matriz
for f in a:
    print(f)
c=int(input("seleccione una colomna: "))
b=[]
for f in range(len(a)):   # "len" da la cantidad de valores que tiene esa lista
    b.append(a[f][c-1]) # "c" no es la totalidad, es solo una
print(b)
"""""

# Matriz 2

fila = 2
columna=2
a=[[int(input("ingrese el valor: ")) for i in range(fila)]for j in range(columna)]
for f in a:
    print(f)
c=int(input("seleccione una fila: "))
b=[]
for f in range(len(a)):   # "len" da la cantidad de valores que tiene esa lista
    b.append(a[c-1][f-1]) # "c" no es la totalidad, es solo una
print(b)