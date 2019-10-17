  
SUE = float ( input ( "Ingrese su sueldo: "))
CATE = int ( input ( "Ingrese su categoria: "))
HE = int ( input ( "Ingrese las horas extra que trabajaste: "))
PHE = float ( 0 )
NSUE = float ( 0 )
if CATE == 1:
    PHE = 30
elif CATE == 2:
    PHE = 38
elif CATE == 3:
    PHE = 50
elif CATE == 4:
    PHE = 70
elif CATE > 4:
    PHE = 0
if HE > 30:
    NSUE = SUE + 30 * PHE
else:
    NSUE = SUE + HE * PHE
print(f"Tu nuevo sueldo es {NSUE}.")
print("Fin del programa.")

