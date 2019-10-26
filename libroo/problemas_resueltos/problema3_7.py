MED = 0
CHI = 0
GRA = 0
N = int(input("Ingese el numero de ventas: "))
I = 1
for I in range(1,N + 1,I):
    V = float(input("Ingrese el total de la venta: "))
    if V <= 200:
        CHI += 1
    else:
        if V < 400:
            MED += 1
        else:
            GRA += 1
    I += 1
print(f"La cantidad total de ventas menores a 200 es de {CHI}, la cantidad de ventas mayores a 200 y menores a 400 es {MED} y mayores a 400 es {GRA}.")
