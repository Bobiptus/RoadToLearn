totalnumeros = None
totalarreglos = None
verificador = int(0)

while totalarreglos is None:
    try:
        while verificador > 0:
            totalarreglos = int ("¿Cuantos arreglos quieres capturar? ")
            if totalarreglos < 2:
                print ("No pueden ser menos de 2 arreglos\n\n")
            else:
                verificador = totalarreglos
    except ValueError:
        print ("Solo puedes capturar numeros")


while totalarreglos > 0:
    lista = []
    while totalnumeros is None:
        try:
            while verificador < 3:
                totalnumeros = int(input ("¿Cuantos numeros quieres capturar? "))
                if totalnumeros < 3:
                    print ("No pueden ser menos de 3 numeros\n\n")
                else:
                    verificador = totalnumeros
        except ValueError:
            print ("\n** Solo ingresar numeros **")

    while (len(lista) != totalnumeros):
        try:
            lista.append(int(input("Número a capturar: ")))
        except ValueError:
            print("Solo numeros es permitido")
    open ("arreglos.txt","w")
    f.write(lista)

