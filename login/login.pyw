import tkinter as tk 
from PIL import Image, ImageTk

ventana=tk.Tk()
ventana.title("Tecnar App")
ventana.geometry("800x500")
ventana.resizable(False,False)

# Primer frame
frame1 = tk.Frame(ventana, width=300, height=800, relief="raised", bd=1, bg="skyblue")
frame1.grid(row=0, column=0, pady=0)

imagen = Image.open("C:\\Users\\Javier\\Desktop\\login\\icono.png")
imagen = imagen.resize((100, 100))
imagen = ImageTk.PhotoImage(imagen)
label = tk.Label(frame1, image=imagen)
label.image = imagen
label.place(relx=0.5, rely=0.3, anchor="center")

frame2 = tk.Frame(ventana, width=300, height=300, relief="raised", bd=1, bg="lightgrey")
frame2.grid(row=0, column=1, pady=10, padx=10)

def centrar_contenido():
    frame2.update_idletasks()
    width = frame2.winfo_width()
    height = frame2.winfo_height()
    x = (frame2.winfo_toplevel().winfo_width() - width) / 2
    y = (frame2.winfo_toplevel().winfo_height() - height) / 2
    frame2.place(in_=ventana, relx=0.65, rely=0.6, x=-width/2, y=-height/2)

centrar_contenido()

etiqueta = tk.Label(frame2, text="Inicio de Sesion", bg="black", fg="white", font=("Arial", 16), width=20, height=2, anchor="center")
etiqueta.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="n")

usuario_label = tk.Label(frame2, text="Usuario:", bg="lightgrey")
usuario_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

usuario_entry = tk.Entry(frame2)
usuario_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

contrasena_label = tk.Label(frame2, text="Contraseña:", bg="lightgrey")
contrasena_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

contrasena_entry = tk.Entry(frame2, show="*")
contrasena_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

login_button = tk.Button(frame2, text="Iniciar sesión", bg="green", fg="white", font=("Arial", 12))
login_button.grid(row=3, column=0, columnspan=2, pady=10)

registro_button = tk.Button(frame2, text="Registrarse", bg="blue", fg="white", font=("Arial", 12))
registro_button.grid(row=4, column=0, columnspan=2, pady=5)

ventana.mainloop()
