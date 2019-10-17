PREB = float(input("Escribe el valor del articulo: "))
IMP = 0
if PREB > 500:
    IMP = (20*0.30) + (PREB - 40)*0.50
elif PREB > 40:
    IMP = (20*0.30) + (PREB - 40)*0.40
elif PREB > 20:
    IMP = (20*0.30) + (PREB - 40)*0.30
else:
    IMP = 0
PRET = PREB + IMP
print(f"El precio basico de su producto es {PREB} y el precio total de su producto es {PRET}. ")
print("FIN")

