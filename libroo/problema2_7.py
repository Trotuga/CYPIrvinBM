A = int(input("Escribe el primer numero: "))
B = int(input("Escribe el segundo numero: "))
C = int(input("Escribe el tercer numero: "))
if A < B:
    if B < C:
        print("Los numeros estan en orden creciente. ")
    else:
        print("LOs numeros no estan en orden creciente. ")
else:
    print("Los numero no estan en orden creciente. ")
