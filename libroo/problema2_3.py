A = int ( input ( "Introduzca el valor cuadratico de su ecuacion: "))
B = int ( input ( "Introduzca el valor lineal de su ecuacion: "))
C = int ( input ( "Introduzca el valor independiente de su ecuacion: "))
D = (B * 2) - 4 * A * C
X1= 0
X2= 0
if D >= 0:
    X1 = ((-B) + D ** 0.5) / 2 * A 
    X2 = ((-B) - D ** 0.5) / 2 * A 
print(f"Las raices de tu ecuacion son {X1} y {X2}.") 
