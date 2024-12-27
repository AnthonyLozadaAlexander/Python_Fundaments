# Crear un programa para evaluar las calificaciones de los estudiante, el programa debe solicitar que se ingrese su
# calificacion como un numero decimal, el programa debe evaluar la calificacion y mostrar un mensaje de acuerdo a la calificacion

# 0.0 - 5.0: Insuficiente
# 5.0 - 6.0: Suficiente
# 6.0 - 7.0: Bien
# 7.0 - 9.0: Notable

num1 = float(input("Ingrese su calificacion_1: "))
num2 = float(input("Ingrese su calificacion_2: "))
num3 = float(input("Ingrese su calificacion_3: "))
num4 = float(input("Ingrese su calificacion_4: "))

resultado = (num1 + num2 + num3 + num4 / 4)

if resultado >= 0.0 and resultado <= 5.0:
    print("Insuficiente, esfuerzate mas el proximo parcial")

elif resultado >= 5.0 and resultado <= 6.0:
    print("Has Alcanzado la nota suficiente, pero puedes mejorar")

elif resultado >= 6.0 and resultado <= 7.0:
    print("Has Alcanzado Una Buena nota, pero puedes mejorar")

else:
    print("Has Alcanzado Una Nota Notable, Felicidades")



