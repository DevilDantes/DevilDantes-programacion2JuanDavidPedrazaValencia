import tkinter as tk
def registrar():
    Lframenombre=tk.Label(frame, text=cnombre.get())
    Lframenombre.pack()
    Lframeapellido=tk.Label(frame, text=capellido.get())
    Lframeapellido.pack()
    Lframeedad=tk.Label(frame, text=xedad.get())
    Lframeedad.pack()
ventana = tk. Tk()

ventana.title ("Tecnar APP")

ventana.geometry("800x600")

ventana.resizable(True, True)

lnombre= tk.Label(ventana,text="Nombre")
lnombre.place(x=5,y=5)
cnombre=tk.Entry(ventana, width=25)
cnombre.place(x=80,y=10)

lapellido= tk.Label(ventana,text="Apellido")
lapellido.place(x=5,y=40)
capellido=tk.Entry(ventana, width=25)
capellido.place(x=80,y=40)

ledad= tk.Label(ventana,text="Edad")
ledad.place(x=5,y=70)
xedad=tk.Entry(ventana, width=25)
xedad.place(x=80,y=70)

Registrar= tk.Button(ventana,text= "REGISTRAR",bg="grey", command=registrar)
Registrar.place(x=100,y=100)

frame = tk.Frame(ventana, width=300, height=150, relief="raised", bd=1)
frame.place(x=20,y=130)


ventana.mainloop()
