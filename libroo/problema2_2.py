P = int(input("Escribe el primer valor entero: "))
Q = int(input("Escribe el segundo valor entero: "))

EXP = (P**3) + (Q**4) - 2*(P**2)
if EXP < 680:
    print(f"El algoritmo si funciona con {P} y {Q}. ")
else:
    print(f"El algoritmo no funciona con {P} y {Q}. ")
print("FIN")

