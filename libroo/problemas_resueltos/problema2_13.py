MAT = int ( input ("Ingresa tu matricula: "))
CARR = int (input( "Ingresa el numero de la carrera que deseas solicitar (1: Economia, 2: Computacion, 3: Contabilidad, 4: Administracion): "))
SEM = int ( input ("Ingresa el semestre que estas cursando: "))
PROM = float ( input ("Ingresa tu promedio actual: "))
if CARR == 1:
    if SEM >= 6 and PROM >= 8.8:
        print(f"El alumno con matricula {MAT} fue aceptado en la carrera de Economia.")
elif CARR == 2:
    if SEM > 6 and PROM > 8.5:
        print(f"El alumno con matricula {MAT} fue aceptado en la carrera de Computacion.")
elif CARR == 3:
    if SEM > 5 and PROM > 8.5:
        print(f"El alumno con matricula {MAT} fue aceptado en la carrera Contabilidad.")
elif CARR == 4:
    if SEM > 5 and PROM > 8.5:
        print(f"El alumno con matricula {MAT} fue aceptado en la carrera Administracion.")
print("Fin del programa.")
