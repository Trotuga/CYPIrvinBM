COMPRA = float ( input ("Ingrese el total de la compra: "))
if COMPRA < 500:
    P = COMPRA
elif COMPRA <= 1000:
    P = COMPRA - (COMPRA * 0.05)
elif COMPRA <= 7000:
    P = COMPRA - (COMPRA * 0.11)
elif COMPRA <= 15000:
    P = COMPRA - (COMPRA * 0.18)
else:
    P = COMPRA - (COMPRA * 0.25)
print(f"El total a pagar es {P}.")
print("Fin del programa.")
