print('*************FUNCIONES ****************')
def miFuncion():
    print('MI PRIMERA FUNCION')

#miFuncion()
#miFuncion()

def imprimeDato(argumentoUno):
    print("Mi argumento es ", argumentoUno)
#imprimeDato('parametro 1')

def imprimeDatos(nombre, apellido):
    print('mi nombre completo es: ' , nombre, apellido)

#imprimeDatos('chanchito', 'feliz')

#usamos * para resivir mas de un argumento en nuestra funcion
# (* -> simbolo reservado, el resultado que devuelva va ser una tupla ) 
def imprimeVariosDatos(*nombre):
    print('los datos son: ', nombre)

#imprimeVariosDatos('chanchito', 'feliz', 'lala', 'lele')

#usamos la llave par llamar a los argumentos sin importar
#el orden
def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

#nombreCompleto(nombre='chanchito', apellido='feliz')

#acceder a los argumentos usando la sintacsis de diccionario
def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

#nombreCompleto2(nombre='chanchito', apellido='feliz')

def miFuncionLista(lista):
    for elemento in lista:
        print(elemento)

#miFuncionLista(['chanchito', 'feliz'])

def concatenaNombre(lista):
    i = ''
    for elemento in lista:
        i = i + ' ' + elemento
    return i
#nombres= concatenaNombre(['chanchito', 'feliz'])
#print(nombres)

# RECURSIVIDAD
print("********Recursividad********")
def recursion(i):
    if(i<1):
        return i
    print(i)
    recursion(i - 1)
recursion(6)