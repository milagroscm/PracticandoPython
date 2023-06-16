#FLUJO DE CONTROL

# 1. Un hombre desea saber si su sueldo es mayor al sueldo mínimo, el programa le pedirá al
# usuario su sueldo actual y el sueldo mínimo. Si el sueldo es mayor al mínimo se debe
# mostrar un mensaje por pantalla indicándolo.

# sueldo_actual = float(input('INGRESE MONTO DE SUELDO ACTUAL '))
# sueldo_minimo = float(input('INGRESE EL SUELDO MINIMO '))

# if sueldo_actual > sueldo_minimo :
#         print('el sueldo ', sueldo_actual , ' es mayor')
# else:
#     print('el sueldo ' ,sueldo_minimo, ' es mayor')


# 2. Construir un pseudocódigo que permita ingresar un número, si el número es mayor de
# 500, se debe calcular y mostrar en pantalla el 18% de este.

# numero = float(input('INGRESE NUMERO : '))
# if numero > 500:
#     numero = numero * 0.18
#     print('el 18% es ', numero)

# 3. Se pide ingresar una letra del alfabeto y mostrar si dicha letra es vocal o consonante.

# letra = input('INGRESE UNA LETRA: ')
# if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#     print(letra ,' es vocal')
# else:
#     print(letra, ' es consonante')

# 4. Diseñe un algoritmo que lea un número de tres cifras y determine si es o no capicúa.

# numero = int(input('INGRESE UN NUMERO : '))

# if numero // 100 == ((numero % 100) % 10):
#     print('EL ' , numero, ' ES CAPICUA ')
# else:
#     print('EL NUMERO ' , numero , ' NO ES CAPICUA')


# 5. Crea una aplicación que nos pida un día de la semana y que nos diga si es un dia laboral
# o no.

dia = input('INGRESE UN DIA DE LA SEMANA :')

if dia == 'sabado' or dia == 'domingo':
    print(dia ,' es un dia no laborable ')
else:
    print(dia ,' es un dia labodable')    
