participacion = 0.0
primerExamen = 0.0
segundoExamen = 0.0
examenFinal = 0.0

participacion = float(input("Ingrese la nota de participacion: "))
primerExamen = float(input("Ingrese la nota del primer examen: "))
segundoExamen = float(input("Ingrese la nota del segundo examen: "))
examenFinal = float(input("Ingrese la nota del examen final: "))

#Porcentajes
participacion = participacion * 0.10
primerExamen = primerExamen * 0.25
segundoExamen = segundoExamen * 0.25
examenFinal = examenFinal * 0.40

calificacionFinal = (participacion + primerExamen + segundoExamen + examenFinal)
print("\nLa calificacion final es: ", calificacionFinal)

