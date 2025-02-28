from tkinter import messagebox


def nuevo_salario():
    if salario.get() < 18000:
        nuevo_salario = salario.get() + (salario.get() * 0.12)
        message = "El nuevo salario del profesor es: " + str(nuevo_salario)
        messagebox.showinfo(message=message)

    elif salario.get() >= 18000 and salario.get() < 30000:
        nuevo_salario = salario.get() + (salario.get() * 0.08)
        message = "El nuevo salario del profesor es: " + str(nuevo_salario)
        messagebox.showinfo(message=message)

    elif salario.get() >= 30000 and salario.get() < 50000:
        nuevo_salario = salario.get() + (salario.get() * 0.07)
        message = "El nuevo salario del profesor es: " + str(nuevo_salario)
        messagebox.showinfo(message=message)
    else:
        nuevo_salario = salario.get() + (salario.get() * 0.06)
        message = "El nuevo salario del profesor es: " + str(nuevo_salario)
        messagebox.showinfo(message=message)

from tkinter import *

Window = Tk()

Window.geometry("295x295+750+400")
Window.title("Aumento De Salario")

# Configurar la cuadrícula para centrar contenido
Window.columnconfigure(0, weight=1)  # Columna 0 se expande horizontalmente
Window.rowconfigure(0, weight=1)     # Fila 0 (para el Label)
Window.rowconfigure(1, weight=1)     # Fila 1 (para el Entry)
Window.rowconfigure(2, weight=1)     # Fila 2 (para el Button)

# Variables
salario = IntVar()

# Crear widgets
lblSalario = Label(Window, text="Ingrese el salario del profesor:")
txtSalario = Entry(Window, textvariable=salario)
btnSalario = Button(Window, text="Calcular Aumento", command=nuevo_salario)

# Posicionar widgets
# sticky = "ew" permite expandir horizontalmente la caja
lblSalario.grid(row=0, column=0, padx=10, pady=10, )
txtSalario.grid(row=1, column=0, padx=10, pady=10, )
btnSalario.grid(row=2, column=0, padx=10, pady=10, )

Window.mainloop()

# print("-----------------------------------------------")
# salario = int(input("Ingrese el salario del profesor: "))
# print("-----------------------------------------------")
#
# if salario > 0 and salario < 18000:
#     salario = salario + (salario * 0.12)
#
#     print("----------------------------------------------")
#     print("El nuevo salario del profesor sera: ", salario)
#     print("----------------------------------------------")
#
# elif salario >= 18000 and salario < 30000:
#     salario = salario + (salario * 0.08)
#
#     print("----------------------------------------------")
#     print("El nuevo salario del profesor sera: ", salario)
#     print("----------------------------------------------")
#
# elif salario >= 30000 and salario < 50000:
#     salario = salario + (salario * 0.07)
#
#     print("----------------------------------------------")
#     print("El nuevo salario del profesor sera: ", salario)
#     print("----------------------------------------------")
#
# else:
#     salario = salario + (salario * 0.6)
#
#     print("----------------------------------------------")
#     print("El nuevo salario del profesor sera: ", salario)
#     print("----------------------------------------------")