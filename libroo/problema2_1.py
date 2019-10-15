N = int(input("Escribe el numero de sonidos emitido por un grillo en un minuto: "))
if N > 0:
    T = (N/4) + 40
    print(f"(La temperatura es de: {T} grados. ")
else:
    print("No es valido usar negativos... ")
print("END")

