CUECER= 0 
N = int(input("Dame un numero entero positivo: "))
for I in range(1,N,1):
    NUM = int(input("Ingrese un numero entero: "))
    if NUM == 0:
        CUECER += 1
print("EL numero de ceros fue: ",CUECER)
