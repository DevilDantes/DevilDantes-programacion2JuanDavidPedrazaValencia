import tkinter as tk
from PIL import Image, ImageTk 


ventana=tk.Tk()
ventana.title("Tecnar App")
ventana.geometry("800x500")
ventana.resizable(False,False)

frame = tk.Frame(ventana, width=300, height=800, relief="raised", bd=1, bg="skyblue")
frame.grid(row=0, column=0,pady=0)

imagen=Image.open("C:\\Users\\Biblioteca\\Desktop\\Foto\\icono.png")
imagen = imagen.resize((100, 100) )  
imagen = ImageTk.PhotoImage(imagen)
label = tk.Label(frame, image=imagen)
label.image = imagen
label.place(relx=0.5, rely=0.3, anchor="center")

etiqueta = tk.Label(ventana, text="LOGIN", bg="black", fg="white", font=("Arial", 16), width=20, height=2, anchor="center")
etiqueta.grid(row=0, column=1, pady=1, sticky="n")

usuario = tk.Label(ventana, text="Usuario:")
usuario.grid(row=1, column=5, pady=10, sticky="n")


ventana.mainloop()
