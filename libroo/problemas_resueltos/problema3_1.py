SUMPAR = 0
SUMIMP = 0
CUEPAR = 0
for I in range(0,271,1):
    NUM = int(input("Ingrese un numero entero positivo: "))
    if NUM != 0:
        if ((-1) ** NUM) > 0:
            SUMPAR += NUM
            CUEPAR += 1
        else:
            SUMIMP += NUM
    else:
        I += 1
PROPAR = SUMPAR / CUEPAR
print(f"El promedio de los numeros pares ingresados es {PROPAR} y la suma de los impares es de {CUEPAR}.")
print("Fin del programa.")
