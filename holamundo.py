#variables
x = 5
y = "chanchito triste"

#multiples variables
a, b, c = 'lala' , 'lele' , 'lili'

print(x, y)
print(a , b , c)

#string
palabra = 'hola mundo'

#numeros
entero = 20
conDecimal = 20.2  #float
complejo =1j

print(palabra, entero, conDecimal, complejo)

print('*********************************************')
print('**************LISTA**************************')
print('*********************************************')

lista =['hola', 'mundo', 'perrito', 'perrito']
lista.append(1)
lista.append(2)
lista.append(3)
lista2 = lista.copy()
lista.append(4)
print("lista 1: " ,lista, "lista 2 :",lista2)

print("lista 2:" , lista2.count('perrito'))

# print("tamaño de la lista 1:", len(lista))

# # ACCEDIEMDO A ELEMENTOS DE UNA LISTA
# print(lista[2])

# # eliminando elementos de una lista
# #pop elimina el ultimo elemento de la lista
# lista.remove('hola')
# print(lista)

# #usando reverse
# lista.reverse()
# print(lista)


# print('*********************************************')
# print('**************TUPLAS*************************')
# print('*********************************************')

# #las tuplas no pueden ser modificadas 

# tupla = ('hola', 'esta', 'es', 'una', 'tupla')
# print(tupla)

# #convirtiendo una tupla en lista
# listaDeTupla = list(tupla)
# listaDeTupla.append('chanchito')
# print(listaDeTupla)

# #RANGE

# print('*********************************************')
# print('**************RANGE**************************')
# print('*********************************************')

# rango = range(6)
# print(rango)

# #DICCCIONARIO

# print('*********************************************')
# print('**************DICCCIONARIO*******************')
# print('*********************************************')

# diccionario = {
#     "nombre": "michi 1",
#     "raza":'persa',
#     'edad': 5
# }
# print(diccionario)
# print(diccionario['raza'])
# print(diccionario.get('nombre'))
# diccionario['nombre']= 'fluffy'
# print(diccionario)
# print(len(diccionario))
# diccionario['ronronea'] = 'Si'
# print(diccionario)
# #diccionario.pop("ronronea")
# #diccionario.popitem() # elimina el ultimo valor del diccionario
# copiaGatito = diccionario.copy()
# del diccionario['ronronea'] # otra forma de eliminar un elemento del diccionario
# print(diccionario)
# diccionario.clear()
# print(diccionario, copiaGatito)

# ## DICCIONARIOS ANIDADOS DICT
# gatitos1 = {
#     'Fluffy' : {
#         'nombre' : 'Fluffy',
#         'edad': 4    
#     },
#     'Michi': {
#         'nombre': 'Black Michi',
#         'edad': 5
#     }
# }
# print(gatitos1)
# # ----------------------------
# fluffy = {
#     'nombre' : 'Fluffy',
#     'edad': 4 
# }

# Michi = {
#     'nombre': 'Black Michi',
#     'edad': 5
# }
# gatitos = {
#     'Fluffy' : fluffy,
#     'Michi': Michi
# }

# print(gatitos)

# # constructor dict


# perritos = dict(nombre = 'pulgoso', edad = 5)
# print(perritos)

# #-----------------------------

# # BOOLEANOS
# print('BOOLEANOS')

# verdad = True
# falso = False
# print(verdad, falso)
