import tkinter as tk 
def registrar():
    pop_up = tk.Toplevel(ventana)
    pop_up.title("Datos registrados")
    
    tk.Label(pop_up, text="Nombre: " + cnombre.get()).pack()
    tk.Label(pop_up, text="Apellido: " + capellido.get()).pack()
    tk.Label(pop_up, text="Edad: " + cedad.get()).pack()
    tk.Label(pop_up, text="Dirección: " + cdireccion.get()).pack()
    tk.Label(pop_up, text="Sexo: " + csexo.get()).pack()


ventana=tk.Tk()
ventana.title("Tecnar App")
ventana.geometry("800x600")
ventana.resizable(True,True)

lnombre=tk.Label(ventana,text="nombre:" )
lnombre.grid(row = 0, column = 0, pady = 4)
cnombre=tk.Entry(ventana, width=30)
cnombre.grid(row = 1, column = 0, pady = 4)

lapellido=tk.Label(ventana,text="apellido:" )
lapellido.grid(row = 3, column = 0, pady = 4)
capellido=tk.Entry(ventana, width=30)
capellido.grid(row = 4, column = 0, pady = 4)

ledad=tk.Label(ventana,text="edad:" )
ledad.grid(row = 5, column = 0, pady = 4)
cedad=tk.Entry(ventana, width=30)
cedad.grid(row = 6, column = 0, pady = 4)

ldireccion=tk.Label(ventana,text="direccion:")
ldireccion.grid(row = 7, column= 0, pady= 4)
cdireccion=tk.Entry(ventana, width=30)
cdireccion.grid(row = 8, column = 0, pady = 4)

lsexo=tk.Label(ventana,text="sexo:")
lsexo.grid(row = 9, column= 0, pady= 4)
csexo=tk.Entry(ventana, width=30)
csexo.grid(row = 10, column = 0, pady = 4)

Registrar = tk.Button(ventana, text="Registrar", command=registrar)
Registrar.grid(row = 11, column = 0, pady = 4)


ventana.mainloop()
