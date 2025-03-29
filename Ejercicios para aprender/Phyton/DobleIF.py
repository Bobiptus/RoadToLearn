#INICIO CODIGO

numerador = float(input("Dame el valor de numerador: "))
denominador = float(input("Dame el valor del denominador (No puede ser 0): "))

if denominador != 0:
    print ("Condicion aceptada")
    check = True
else:
    print ("Condicion rechazada")
    check = False

if (check == True):
    resultado = numerador / denominador
    print("El resultado es: ", resultado)