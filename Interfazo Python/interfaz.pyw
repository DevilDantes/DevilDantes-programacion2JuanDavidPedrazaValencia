import tkinter as tk 
from PIL import Image, ImageTk 

ventana = tk.Tk()
path = Image.open("C:\\Users\\Biblioteca\\Desktop\\Foto\\pepino.png")
icono = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icono)
ventana.title("Tecnar APP") 


ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight() 

ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")
ventana.resizable(True, True) 
ventana.config(bg="black")
etiqueta = tk.Label(ventana, text="¡Hola, mundo!", bg="black", fg="white", font=("Arial", 16), width=20, height=2, anchor="center")
etiqueta.pack()

def cambiar_texto():
    etiqueta.config(text="¡Hola!")

etiqueta.pack()
boton1 = tk.Button(ventana, text="Cambiar", command=cambiar_texto)
boton1.pack()
boton1.place(x=100, y=100, width=100, height=30)

boton2 = tk.Button(ventana, text="Botón 2", bg="blue", fg="white", font=("Arial", 12))
boton2.pack()
boton2.place(x=100, y=200, width=100, height=40)

boton3 = tk.Button(ventana, text="Deshabilitado", state="disabled")
boton3.pack()
boton3 = tk.Label(ventana, text="Ejemplo")
boton3.place(x=100, y=300, width=100, height=30)

def obtener_texto():
    texto_ingresado = cuadro_texto.get()
    etiqueta.config(text="Texto ingresado: " + texto_ingresado)
etiqueta = tk.Label(ventana, text="Usuario Ingrese: ")
etiqueta.pack()

cuadro_texto = tk.Entry(ventana, width=30)
cuadro_texto.pack()

boton = tk.Button(ventana, text="Obtener Texto", command=obtener_texto)
boton.pack()

marco1 = tk.Frame(ventana, width=200, height=100, bd=2, relief="solid")
marco1.pack()

etiqueta1 = tk.Label(marco1, text="Marco 1")
etiqueta1.pack()
etiqueta3 = tk.Label(marco1, text="Marco 1")
etiqueta3.pack()

marco2 = tk.Frame(ventana, width=200, height=100, bd=2, relief="raised")
marco2.pack()

etiqueta2 = tk.Label(marco2, text="Marco 2")
etiqueta2.pack()

def obtener_seleccion():
    seleccionados = cuadro_lista.curselection()
    for index in seleccionados:
        elemento = cuadro_lista.get(index)
        print("Elemento seleccionado:", elemento)
cuadro_lista = tk.Listbox(ventana, width=30, selectmode="multiple")
cuadro_lista.pack()

elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]

for elemento in elementos:
    cuadro_lista.insert(tk.END, elemento)

boton = tk.Button(ventana, text="Obtener", command=obtener_seleccion)
boton.pack()

def obtener_estado():
    if variable.get() == 1:
        print("La casilla de verificación está seleccionada")
    else:
        print("La casilla de verificación no está seleccionada")
variable = tk.IntVar()

casilla_verificacion = tk.Checkbutton(ventana, text="Opción 1", variable=variable, command=obtener_estado)
casilla_verificacion.pack()

def obtener_seleccion():
    seleccion = variable.get()
    if seleccion == 1:
        print("Opción 1 seleccionada")
    elif seleccion == 2:
        print("Opción 2 seleccionada")
    elif seleccion == 3:
        print("Opción 3 seleccionada")
        
variable = tk.IntVar()

opcion1 = tk.Radiobutton(ventana, text="Opción 1", variable=variable, value=1, command=obtener_seleccion)
opcion1.pack()

opcion2 = tk.Radiobutton(ventana, text="Opción 2", variable=variable, value=2, command=obtener_seleccion)
opcion2.pack()

opcion3 = tk.Radiobutton(ventana, text="Opción 3", variable=variable, value=3, command=obtener_seleccion)
opcion3.pack()


ventana.mainloop()
