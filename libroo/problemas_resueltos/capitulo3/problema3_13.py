ARSU = 0
ARNO = 0
MERSU = 50000
ARCE = 0
I = 1
for I in range(1,13,I):
    RNO = float(input("Ingrese la cantidad de lluvia en la region norte del pais: "))
    RCE = float(input("Ingrese la cantidad de lluvia en la region centro del pais: "))
    RSU = float(input("Ingrese la cantidad de lluvia en la region sur del pais: "))
    ARNO += RNO
    ARCE += RCE
    ARSU += RSU
    if RSU < MERSU:
        MERSU = RSU
        MES = I
    else:
        I += 1
PRORCE = ARCE / 12
print(f"Promedio region centro: ",PRORCE)
print(f"Mes con menor lluvia en la region sur: ",MES)
print(f"Registro del mes: ",MERSU)
if ARNO > ARCE:
    if ARNO > ARSU:
        print("La region con mayor lluvia es la norte.")
    else:
        print("La reguion con mayor lluvia es la region sur.")
else:
    if ARCE > ARSU:
        print("La region con mayor lluvia es la region centro.")
    else:
        print("La region con mayor lluvia es la region sur.")
print("Fin del programa.")a
