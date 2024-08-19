# es una estructura que guardan o almacenan significados
# hay dos tipos el que almacena y lo que se almacena
# los diccionarios tienen de dominio llaves {}
# keys values

mi_diccionario = {"nombre":"Daniel","apellido":"Silva","edad":"18"}
print (mi_diccionario)
print (mi_diccionario["nombre"])


print (mi_diccionario.keys()) #imprime solo los keys
print (mi_diccionario.values()) #imprimesolo los values

#existen ciertas funciones para manipular los diccionarios
#modificar el values

# .setdefault almacena un nuevo dato

mi_diccionario["nombre"]= "juan" #editar valor
mi_diccionario.setdefault("plataforma: ","udemy") # lo almacena con parentecis, agrega valor
print (mi_diccionario)

mi_diccionario.pop("edad") # .pop elimina algo en especifico

mi_diccionario.get("nombre") #. get es para tomar un valor
print (mi_diccionario)

mi_diccionario.clear() #limpia todos los valores 
print (mi_diccionario)





# palabras reservadas de SQL