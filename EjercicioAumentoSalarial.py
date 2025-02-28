print("-----------------------------------------------")
salario = int(input("Ingrese el salario del profesor: "))
print("-----------------------------------------------")

if salario > 0 and salario < 18000:
    salario = salario + (salario * 0.12)

    print("----------------------------------------------")
    print("El nuevo salario del profesor sera: ", salario)
    print("----------------------------------------------")

elif salario >= 18000 and salario < 30000:
    salario = salario + (salario * 0.08)

    print("----------------------------------------------")
    print("El nuevo salario del profesor sera: ", salario)
    print("----------------------------------------------")

elif salario >= 30000 and salario < 50000:
    salario = salario + (salario * 0.07)

    print("----------------------------------------------")
    print("El nuevo salario del profesor sera: ", salario)
    print("----------------------------------------------")

else:
    salario = salario + (salario * 0.6)

    print("----------------------------------------------")
    print("El nuevo salario del profesor sera: ", salario)
    print("----------------------------------------------")
