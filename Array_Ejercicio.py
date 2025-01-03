#Realizar un algoritmo que me permite la carga de 5 numeros en un vector, una vez cargados debe determinar cual es el
# mayor de ellos.

numeros = []

for i in range(0,5,1):
    numero = int(input(f"Ingrese un numero al array {i}: "))
    numeros.append(numero) #los numeros se agregan al array con append desde la variable numero que esta ingresando el usuario

mayor = numeros[0]
posicion = 0

for i in range(0,5,1):
    if numeros[i] > mayor:
        mayor = numeros[i]
        posicion = i

print(f"El numero mayor del array es el: {mayor} y esta en la posicion del array: {posicion} ")