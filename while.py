otra = True 
suma = 0.0
while(otra== True):
    cal = float(input("Calificacion: "))
    suma += cal
    otra = bool(int(input("Hay mas alumnos ( 0 no, 1 si.) ")))
print("Suma ",suma)
print("END  ")
