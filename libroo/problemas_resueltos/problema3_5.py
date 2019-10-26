SUMOTR = 0
SUMPOS = 0
CUEPOS = 0
N = int(input("Ingrese la cantidad de datos que se van a ingresar: "))
I = 1
for I in range(1,N + 1,I):
    NUM = int(input("Ingrese un numero entero: "))
    if NUM > 0:
        SUMPOS += NUM
        CUEPOS += 1
    else:
        SUMOTR += NUM
    I += 1
PROGEN = (SUMPOS + SUMOTR) / N
PROPOS = SUMPOS / CUEPOS
print(f"La cantidad de numeros positivos es de {CUEPOS} y su promedio es {PROPOS} y el promedio total es {PROGEN}.")
