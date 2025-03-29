registros = int (input ('¿Cuantos registros deseas dar de alta? '))

while registros > 0:
    
    #Captura de datos
    names = input('Nombres: ')
    last_name = input('Apellidos: ')
    phone = input('Numero de telefono: ')
    email = input('e-mail: ')
    #Conteo de caracteres
    count_names = (names)
    count_lastnames = (last_name)
    count_phone = (phone)
    count_email = ('email')
    
    #Inician condiciones
    if range (5,50):
        print('Hola '+ names +' '+last_name+' en breve recibiras un correo a '+email)
        registros = registros - 1
        pass
    else:
        print ("Nombre debe de ser mayor a 5 caracteres y menos de 100")
    print('Hola '+ names +' '+last_name+' en breve recibiras un correo a '+email)
    registros = registros - 1

print ('Excelente día')    
