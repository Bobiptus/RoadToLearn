cadena = []
conteo = float(0)
archivo = open("Prueba.txt", "w+")

while conteo < 10:
    cadena.append(float(input("Numero a capturar: ")))
    #archivo.write(cadena[conteo])
    conteo += 1
archivo.write(cadena[0:9])   
archivo.close
