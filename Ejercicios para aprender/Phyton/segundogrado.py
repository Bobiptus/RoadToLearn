#inicio
import math


print ("OPERACION DE SEGUNDO GRADO\n\n")
a = float(input("Dame el valor de A: "))
b = float(input("Dame el valor de B: "))
c = float(input("Dame el valor de C: "))

#Operación
d = (b**2) - 4*a*c

#Condiciones
if (d > 0):
    print ("Raices reales y diferentes\n")
    x1 = (-b + math.sqrt(d)/2/a)
    x2 = (-b - math.sqrt(d)/2/a)
    print(x1)
    print(x2)

if(d == 0):
    print("Raices reales e iguales\n")
    x1 = -b/2/a
    x2 = x1
    print(x1)
    print(x2)

if(d < 0):
    print("Raices complejas y conjugadas\n")
    x1_parte_real = -b/2/a
    x1_parte_imp = math.sqrt(d)/2/a
    x2_parte_real = -b/2/a
    x2_parte_imp = -math.sqrt(d)/2/a
    print(x1_parte_real)
    print(x1_parte_imp)
    print(x2_parte_real)
    print(x2_parte_imp)

#FIN DE CODIGO