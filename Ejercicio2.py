
On = True
Tarjeta = 0
pago = 0
Datos = ""

print("-------------------BIENVENIDO-------------------")
while On:
    name = str(input("Ingrese su nombre: "))
    pago = float(input("Ingrese el monto a pagar: "))

    if name == "" or name.strip() == "":
        print("El nombre no puede estar vacio")
        Datos = "Incorrectos"

    elif pago <= 0:
        print("El monto a pagar no puede ser cero ni un numero negativo")
        Datos = "Incorrectos"

    else:
        print("Datos Ingresados Correctamente: \n")
        print("Nombre: ", name)
        print("Monto a pagar: ", pago)
        Datos = "Correctos"

    if( Datos == "Correctos"):

       while On:
        print("---------------------------------------------------------------")
        print("Con Que Tarjeta Desea Pagar: ")
        print("1. Sams CLASICA")
        print("2. Sams Gold\n")
        Tarjeta = int(input("Ingrese el numero de la tarjeta: "))

        if Tarjeta == 1:
            Porcentaje = pago * 0.20
            print("---------------------------------------------------------------")
            print("Usted ha elegido la tarjeta Sams CLASICA")
            print("Su Monto A Pagar de: ", pago, " Mas el 20% de Descuento es de: ", (pago - Porcentaje))
            print("---------------------------------------------------------------")
            On = False
        elif Tarjeta == 2:
            Porcentaje = pago * 0.30
            print("---------------------------------------------------------------")
            print("Usted ha elegido la tarjeta Sams Gold")
            print("Su Monto A Pagar de: ", pago, " Mas el 30% de Descuento es de: ", (pago - Porcentaje))
            print("---------------------------------------------------------------")
            On = False
        else:
            print("Error: Dato Invalido")

    elif(Datos == "Incorrectos"):
        print("\nError: Datos Incorrectos")
