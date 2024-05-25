import tkinter as tk
from tkinter import messagebox
import json
import util.generic as utl
from PIL import Image, ImageTk
import uuid  # Para generar IDs únicos

class Registro(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registro")
        self.resizable(True, True)
        utl.centrar_ventana(self, 500, 500)

        # Widgets del formulario de registro
        self.texto = tk.Label(self, text="Registro", font=('Times', 20))
        self.texto.pack(padx=10, pady=10)

        self.lnombre = tk.Label(self, text="Nombre:", font=('Times', 14))
        self.lnombre.pack(padx=10, pady=5)
        self.cnombre = tk.Entry(self, width=30, font=('Times', 12))
        self.cnombre.pack(fill=tk.X, padx=10, pady=10)

        self.lusuario = tk.Label(self, text="Usuario:", font=('Times', 14))
        self.lusuario.pack(padx=10, pady=5)
        self.cusuario = tk.Entry(self, width=30, font=('Times', 12))
        self.cusuario.pack(fill=tk.X, padx=10, pady=10)

        self.lclave = tk.Label(self, text="Clave:", font=('Times', 14))
        self.lclave.pack(padx=10, pady=5)
        self.cclave = tk.Entry(self, width=30, font=('Times', 12), show="*")
        self.cclave.pack(fill=tk.X, padx=10, pady=10)

        self.lemail = tk.Label(self, text="Email:", font=('Times', 14))
        self.lemail.pack(padx=10, pady=5)
        self.cemail = tk.Entry(self, width=30, font=('Times', 12))
        self.cemail.pack(fill=tk.X, padx=10, pady=10)

        self.bguardar = tk.Button(self, text="Guardar", font=('Times', 16), command=self.registrar_usuario)
        self.bguardar.pack(padx=10, pady=10)

    def registrar_usuario(self):
        # Obtener datos del formulario
        nombre = self.cnombre.get()
        usuario = self.cusuario.get()
        clave = self.cclave.get()
        email = self.cemail.get()

        # Validar que los campos no estén vacíos
        if not nombre or not usuario or not clave or not email:
            messagebox.showerror("Error", "Todos los campos son obligatorios", parent=self)
            return

        # Cargar datos existentes
        try:
            with open("D:\\LoginApp\\db_users.json", "r", encoding='utf-8') as file:
                db_users = json.load(file)
        except FileNotFoundError:
            db_users = {"users": []}

        # Verificar si el usuario ya existe
        for usuarios in db_users["users"]:
            if usuarios["username"] == usuario:
                messagebox.showerror("Error", "El usuario ya existe", parent=self)
                return

        # Añadir el nuevo usuario
        nuevo_usuario = {
            "id": str(uuid.uuid4()),  # Generar un ID único
            "name": nombre,
            "username": usuario,
            "password": clave,
            "email": email,
            "role": "Cliente"  # Puedes cambiar el rol según sea necesario
        }
        db_users["users"].append(nuevo_usuario)

        # Guardar los cambios en el archivo JSON
        with open("D:\\LoginApp\\db_users.json", "w", encoding='utf-8') as file:
            json.dump(db_users, file, indent=4)

        messagebox.showinfo("Éxito", "Usuario registrado exitosamente", parent=self)
        self.destroy()
