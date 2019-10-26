SERIE = 0
N = int(input("Ingresa el ultimo valor de la serie: "))
I = 1
for I in range(1,N + 1,I):
    SERIE = SERIE + (I ** I)
    I += 1
print(SERIE)
