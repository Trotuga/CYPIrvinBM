A = int(input("Escribe un numero: "))
B = int(input("Escribe otro numero: "))
C = int(input("Escribe otro numero: "))
if A > B:
    if A > C:
        print(f"El numero {A} es el mayor. ")
    elif A == C:
        print(f"El numero {A} y {C} Son iguales y son los mayores. ")
    else:
        print(f"El numero {C} es el mayor. ")
elif A == B:
    if A > C:
        print(f"{A} y {B} son iguales y son los mayores. ")
    elif A == C:
        print(f"Los tres numeros {A} son iguales. ")
    else: 
        print(f"El numero {C} es el mayor. ")
elif B > C:
    print(f" El numero {B} es el mayor. ")
else:
    print(f"El numero {C} es el mayor. ")
print("Fin. ")

