SERIE = 0
N = int(input("Ingrese un numero entero que sera el ultimo termino de esta serie: "))
BAND = 'T'
I = 1
for N in range(1,N + 1,I):
    if BAND == 'T':
        SERIE = SERIE + (1 / I)
        BAND = 'F'
    else:
        SERIE = SERIE - (1 / I)
        BAND = 'T'
    I = I + 1
print(SERIE)
print("Fin del programa.")
