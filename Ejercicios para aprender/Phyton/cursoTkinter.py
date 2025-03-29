from tkinter import *

rooth = Tk()
#estamos creando las dos etiquetas
myLabel1 = Label(rooth, text="Hello World!")
myLabel2 = Label(rooth, text="Bob")

#Estamos poniendo las etiquetas en la ventana con las coordenadas de columnas y filas
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

rooth.mainloop()