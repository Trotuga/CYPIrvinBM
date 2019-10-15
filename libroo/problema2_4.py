M = input("Escribe la matricula : ")
C1 = int(input("Escribe la primera calificacion: "))
C2 = int(input("Escribe la segunda calificacion: "))
C3 = int(input("Escribe la tercera calificacion: "))
C4 = int(input("Escribe la cuarta calificacion: "))
C5 = int(input("Escribe la quinta calificacion: "))
P = (C1+ C1+ C3+ C4+ C5)/5
if P >=6:
    print(f"El estudiante con matricula {M} y promedio {P} esta aprobado. ")
else:
    print(f"El estudiante con matricula {M} y promedio {P} esta reprobado.  ")



