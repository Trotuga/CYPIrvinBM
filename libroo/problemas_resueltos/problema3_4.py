NOM = 0
SUE = float(input("Ingrese el sueldo del empleado: "))
while(SUE != -1):
    if SUE < 1000:
        NSUE = SUE * 1.15
    else:
        NSUE = SUE * 1.12
    NOM += NSUE
    print(f"El nuevo sueldo es de {NSUE}.")
    SUE = float(input("Ingrese el sueldo del empleado: "))
print(f"La nomina es de {NOM}.")
print("Fin del programa.")
