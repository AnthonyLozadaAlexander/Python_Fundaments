def Secuencia_fibonacci(n):
    #Verificamos si n es valido
    if n <= 0:
        return "El numero debe ser mayor que cero"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    #Inicializamos la secuencia con los primeros dos numeros
    secuencia = [0, 1]
    #Generamos la secuencia de Fibonacci
    print("Paso 1: [0, 1]") # Para ver el paso a paso
    while len(secuencia) < n:

        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
        print(f"Paso {len(secuencia)}: {secuencia}")

    return secuencia

#Numero de elementos que queremos en la secuencia
n = 10
resultado = Secuencia_fibonacci(n)
print(f"Secuencia de fibonacci con {n} elementos: {resultado}")