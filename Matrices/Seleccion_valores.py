#todo lo externo lo maneja el valor i
#todo lo interno lo maneja el valor j

"""""
m=[1,2],[3,4],[5,4] 
for i in range (3): # maneja todo lo de una lista
    for j in range (2): # maneja todo lo dentro de una lista
        print(m[i][j],end=" ")
    print ()
"""""

"""""
a=[]
m=3
n=2

for i in range (m):
    a.append([])
    for j in range (n):
        a[i].append(None)

#impresion

for i in range (m):
    for j in range (n):
        print(a[i][j],end=" ")
    print()
"""


# importancion por valores ramdom python

from random import*
fila =3
columnas=3

a=[[randint(1,100) for i in range(fila)] for j in range (columnas)]
for f in range(fila):
    for c in range (columnas):
        print(a[f][c],end=" ")
    print()