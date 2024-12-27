x = 5
y = "Development"

print(x)
print(y)

print(f"El valor de x es {x} y el valor de y es {y}")

print("--------------------------------------------------")

name = str(input("Ingresa tu nombre: "))

print(f"Hola, Bienvenido {name}")

print("--------------------------------------------------")

num1 = int(input("Ingresa un numero para determinar si es par o impar: "))

if num1 % 2 == 0:
    print(f"El numero {num1} es par")
else:
    print(f"El numero {num1} es impar")

print("--------------------------------------------------")

num2 = int(input("Ingresa un numero para determinar si es positivo o negativo: "))

if num2 > 0:
    print(f"El numero {num2} es positivo")
else:
    print(f"El numero {num2} es negativo")

print("--------------------------------------------------")

# Crear un bucle que imprima los números del 1 al 10

num3 = 0

while num3 <= 10:
    print(num3)
    num3 += 1

print("--------------------------------------------------")

x = 5 # aqui a la variable x se le esta asignando un valor de 5, el cual cambia el valor de la variable x a un numero
# entero 5.

y = 6

z = x + y

print(f"La suma de {x} + {y} es:", z)