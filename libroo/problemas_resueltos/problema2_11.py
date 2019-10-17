C = int ( input ( "Escribe la clave de tu zona: "))
NM = int ( input ( "Escribe el total de minutos de tu llamada: "))
if C == 12:
    COST = NM * 2
elif C == 15:
    COST = NM * 2.2
elif C == 18:
    COST = NM * 4.5
elif C == 19:
    COST = NM * 3.5
elif C == 23:
    COST = NM * 6
elif C == 25:
    COST = NM * 6
elif C == 29:
    COST = NM * 5
print(f"El costo total de tu llamada es de {COST}.")
print("Fin del programa.")
