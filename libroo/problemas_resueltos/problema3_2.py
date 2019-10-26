BAND = 'T'
SUMSER = 0
I = 2
while(I <= 1800):
    SUMSER = SUMSER + I
    print(I)
    if BAND == 'T':
        BAND = 'F' 
        I = I + 3
    else:
        BAND = 'T' 
        I = I + 2
print(f"La suma de esta serie es de {SUMSER}.")
print("Fin del programa.")
