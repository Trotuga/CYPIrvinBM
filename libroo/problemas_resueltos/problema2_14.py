TIPOENF = int ( input ("Ingrese el tipo de enfermedad del paciente: "))
EDAD = int ( input ("Ingrese la edad del paciente: "))
DIAS = int ( input ("Ingrese la cantidad de dias que el paciente estuvo hospitalizado: "))
if TIPOENF == 1:
    COSTOT = DIAS * 25
elif TIPOENF == 2:
    COSTOT = DIAS * 16
elif TIPOENF == 3:
    COSTOT = DIAS * 20
elif TIPOENF == 4:
    COSTOT = DIAS * 32
if EDAD >= 14 and EDAD <= 22:
    COSTOT = COSTOT * 1.10
print(f"El costo total es de {COSTOT}.")
print("Fin del programa.")
