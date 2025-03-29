capital = int (input ("Dame el capital: "))
tasa = input ("Dame el interes: ")
meses = int (input ("Dame los meses: "))

interes_simple = capital*tasa*meses
interes_compuesto = capital*pow(1+tasa, meses)

print ("Interes simple: %0.2f"%interes_simple)
print ("Interes compuesto: %0.2f"%interes_compuesto)