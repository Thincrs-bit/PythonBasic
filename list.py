demo_list =[ 1, 2, 3, 4, 5]
string_list =["uno","dos","tres", "cuatro"]
 
#constructor 
# -number_list = list ((1,2,3,4,5))
# -print (number_list)

#variable rango 
# -r = list(range(1,10))
# -print(r)

#len es para ver la  longitud de una lista
# -print(len(string_list))

#saber si un elemento existe en una lista
#- print('tres' in string_list)

#cambiar un valor en el list
#- string_list[1] = 'uno'
#- print((string_list))

# agregar un valor a la lista
#- string_list.append('cinco')
#- print((string_list))

#para agregar mas de dos valores 
#- string_list.extend( ['cinco, seis'] )
#- print((string_list))

#inertar apartir de una posicion en la lista 
#- string_list.insert(0,'cero')
#- string_list.insert(len(string_list),'cinco')
#- print(string_list)

#remover de una lista
#- string_list.pop()
#- string_list.pop(2)
#- string_list.remove('uno')
#- print(string_list)

# limpiar toda la lista
#- string_list.clear()
#- print(string_list) 

#ordenar valores por el alfabeto a - z o de z-a reverse=True
string_list.sort(reverse=True)

print(string_list)

#obtener el indice de un objeto de la lista
print(string_list.index('tres'))