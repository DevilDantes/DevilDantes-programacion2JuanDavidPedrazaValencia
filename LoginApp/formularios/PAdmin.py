import tkinter as tk
import json
from tkinter import messagebox, ttk
import webbrowser
import util.generic as utl
from formularios.login import *

class PAdmin(tk.Tk):
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        self.tipo_action = "Guardar"
        self.tipo_user = ""
        super().__init__()
        self.title("Panel Administrativo")
        self.resizable(True, True)
        self.ancho_pantalla = self.winfo_screenwidth()
        self.alto_pantalla = self.winfo_screenheight()

        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")

        menubar = tk.Menu(self)
        menuuser = tk.Menu(menubar, tearoff=0)
        menuuser.add_command(label="Administracion de Usuarios", command=self.main_usuarios)
        menubar.add_cascade(label="Usuarios", menu=menuuser)


        menuproducto = tk.Menu(menubar, tearoff=0)
        menuproducto.add_command(label="Administracion de Productos", command=self.main_productos)
        menubar.add_cascade(label="Productos", menu=menuproducto)


        self.config(menu=menubar)

        # frame user_info
        self.frame_user_info = tk.Frame(self, bd=0, relief=tk.SOLID, width=200)
        self.frame_user_info.pack(side=tk.LEFT, padx=4, pady=5, fill="y")
        texto = tk.Label(self.frame_user_info, text="PANEL ADMINISTRATIVO", font=('Times', 20))
        texto.pack(padx=20, pady=4)
        self.usrimg = utl.leer_imagen(r"D:\LoginApp\imagenes\userinfo.png", (128, 128))
        self.imgfacebook = utl.leer_imagen(r"D:\LoginApp\imagenes\face.png", (32, 32))
        self.imglinkedin = utl.leer_imagen(r"D:\LoginApp\imagenes\linkedin.png", (32, 32))
        self.imgwebsite = utl.leer_imagen(r"D:\LoginApp\imagenes\website.png", (32, 32))
        self.imglogout = utl.leer_imagen(r"D:\LoginApp\imagenes\logout.png", (32, 32))
        tk.Label(self.frame_user_info, image=self.usrimg).pack(padx=30, pady=4)
        tk.Label(self.frame_user_info, text=self.name, font=('Times', 14)).pack(padx=40, pady=4)
        tk.Label(self.frame_user_info, text=self.email, font=('Times', 14)).pack(padx=50, pady=4)
        tk.Button(self.frame_user_info, image=self.imgfacebook, command=self.abrirface).place(x=100, y=300)
        tk.Button(self.frame_user_info, image=self.imglinkedin, command=self.abrirlink).place(x=140, y=300)
        tk.Button(self.frame_user_info, image=self.imgwebsite, command=self.abrirweb).place(x=180, y=300)
        tk.Button(self.frame_user_info, image=self.imglogout, command=self.logout).place(x=220, y=300)

        # frame_data
        self.frame_data = tk.Frame(self, bd=0, relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)
        textobienvenida = tk.Label(self.frame_data, text="BIENVENIDO AL SISTEMA", font=('Times', 20))
        textobienvenida.pack(padx=20, pady=4)

        # frame_dinamyc
        self.frame_dinamyc = tk.Frame(self.frame_data, bd=0, relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_dinamyc.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)

    def main_usuarios(self):
        self.formulario_usuario()
        self.listar_usuarios()

    def formulario_usuario(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc, text="\uf0c9 REGISTRO DE USUARIOS", font=('Times', 16), fg="#9fa8da")
        labelform.place(x=70, y=30)

        labelcedula = tk.Label(self.frame_dinamyc, text="Cedula:", font=('Times', 14))
        labelcedula.place(x=70, y=100)
        self.ccedula = tk.Entry(self.frame_dinamyc, width=40)
        self.ccedula.place(x=220, y=100)

        labelnombre = tk.Label(self.frame_dinamyc, text="Nombre completo:", font=('Times', 14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=40)
        self.cnombre.place(x=220, y=130)

        labelusuario = tk.Label(self.frame_dinamyc, text="Username:", font=('Times', 14))
        labelusuario.place(x=70, y=160)
        self.cusuario = tk.Entry(self.frame_dinamyc, width=40)
        self.cusuario.place(x=220, y=160)

        labelclave = tk.Label(self.frame_dinamyc, text="Contraseña:", font=('Times', 14))
        labelclave.place(x=500, y=100)
        self.cclave = tk.Entry(self.frame_dinamyc, width=40, show="*")
        self.cclave.place(x=600, y=100)

        labelcorreo = tk.Label(self.frame_dinamyc, text="Correo:", font=('Times', 14))
        labelcorreo.place(x=500, y=130)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=40)
        self.ccorreo.place(x=600, y=130)

        labeltipo = tk.Label(self.frame_dinamyc, text="Rol:", font=('Times', 14))
        labeltipo.place(x=500, y=160)
        self.listatipo = tk.Listbox(self.frame_dinamyc, selectmode="Single", width=40, height=2)
        self.listatipo.place(x=600, y=160)
        self.listatipo.insert(1, "Administrador")
        self.listatipo.insert(2, "Vendedor")
        self.listatipo.insert(3, "Cliente")

        btnguardar = tk.Button(self.frame_dinamyc, text="\uf0c7 GUARDAR", font=('Times', 14), command=self.save_user)
        btnguardar.place(x=870, y=130)

    def listar_usuarios(self):
        tk.Label(self.frame_dinamyc, text="\uf00b LISTADO DE USUARIOS", font=('Times', 16), fg="#9fa8da").place(x=70, y=200)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("NombreCompleto", "Username", "Email", "Rol"))
        self.tablausuarios.heading("#0", text="Cedula")
        self.tablausuarios.heading("NombreCompleto", text="Nombre Completo")
        self.tablausuarios.heading("Username", text="Usuario")
        self.tablausuarios.heading("Email", text="Email")
        self.tablausuarios.heading("Rol", text="Rol")
        with open("D:\LoginApp\db_users.json", "r", encoding='utf-8') as self.file:
            self.db_users = json.load(self.file)
            for usuarios in self.db_users["users"]:
                self.tablausuarios.insert("", "end", text=f'{usuarios["id"]}', values=(f'{usuarios["name"]}', f'{usuarios["username"]}', f'{usuarios["email"]}', f'{usuarios["role"]}'))
        self.tablausuarios.place(x=70, y=250)
        btneliminar = tk.Button(self.frame_dinamyc, text="\uf0c7 Eliminar", font=('Times', 14), command=self.delete_user)
        btneliminar.place(x=70, y=520)
        btnupdate = tk.Button(self.frame_dinamyc, text="\uf0c7 Actualizar", font=('Times', 14), command=self.update_user)
        btnupdate.place(x=200, y=520)

    def save_user(self):
        for index in self.listatipo.curselection():
            self.tipo_user = self.listatipo.get(index)
        if self.ccedula.get() == "" or self.cnombre.get() == "" or self.cusuario.get() == "" or self.ccorreo.get() == "" or self.cclave.get() == "" or self.tipo_user == "":
            messagebox.showinfo('Info', "Debe llenar todos los campos", parent=self)
            return
        else:
            with open("D:\LoginApp\db_users.json", "r", encoding='utf-8') as self.file:
                self.db_users = json.load(self.file)

                if self.tipo_action == "Actualizar":
                    for usuarios in self.db_users["users"]:
                        if usuarios["id"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                            usuarios["name"] = self.cnombre.get()
                            usuarios["username"] = self.cusuario.get()
                            usuarios["password"] = self.cclave.get()
                            usuarios["email"] = self.ccorreo.get()
                            usuarios["role"] = self.tipo_user
                            with open('D:\LoginApp\db_users.json', 'w') as jf:
                                json.dump(self.db_users, jf, indent=4, ensure_ascii=True)
                                messagebox.showinfo('Info', "Usuario actualizado con exito", parent=self)
                                self.limpiar_panel(self.frame_dinamyc)
                else: 
                    self.db_users["users"].append({
                        'id': self.ccedula.get(),
                        'name': self.cnombre.get(),
                        'username': self.cusuario.get(),
                        'password': self.cclave.get(),
                        'email': self.ccorreo.get(),
                        'role': self.tipo_user
                    })
                    with open('D:\LoginApp\db_users.json', 'w') as jf:
                        json.dump(self.db_users, jf, indent=4, ensure_ascii=True)
                        messagebox.showinfo('Info', "Usuario registrado con exito", parent=self)
                        self.limpiar_panel(self.frame_dinamyc)

    def delete_user(self):
        with open("D:\LoginApp\db_users.json", "r", encoding='utf-8') as self.file:
            self.db_users = json.load(self.file)
            for usuarios in self.db_users["users"]:
                if usuarios["id"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                    self.db_users["users"].remove(usuarios)
                    with open('D:\LoginApp\db_users.json', 'w') as jf:
                        json.dump(self.db_users, jf, indent=4, ensure_ascii=True)
                        messagebox.showinfo('Info', "Usuario eliminado con exito", parent=self)
                        self.limpiar_panel(self.frame_dinamyc)
                        break

    def update_user(self):
        with open("D:\LoginApp\db_users.json", "r", encoding='utf-8') as self.file:
            self.db_users = json.load(self.file)
            for usuarios in self.db_users["users"]:
                if usuarios["id"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                    self.ccedula.delete(0, tk.END)
                    self.ccedula.insert(0, usuarios["id"])
                    self.ccedula.config(state="disabled")
                    self.cnombre.delete(0, tk.END)
                    self.cnombre.insert(0, usuarios["name"])
                    self.cusuario.delete(0, tk.END)
                    self.cusuario.insert(0, usuarios["username"])
                    self.cclave.delete(0, tk.END)
                    self.cclave.insert(0, usuarios["password"])
                    self.ccorreo.delete(0, tk.END)
                    self.ccorreo.insert(0, usuarios["email"])
                    self.tipo_action = "Actualizar"

    def limpiar_panel(self, panel):
        # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()

    def logout(self):
        self.destroy()

    def abrirface(self):
        url = "https://www.facebook.com"
        webbrowser.open_new_tab(url)

    def abrirlink(self):
        url = "https://www.linkedin.com"
        webbrowser.open_new_tab(url)

    def abrirweb(self):
        url = "https://itcloud.com.co"
        webbrowser.open_new_tab(url)

    def main_productos(self):
        self.formulario_producto()
        self.listar_productos()

    def formulario_producto(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc, text="REGISTRO DE PRODUCTOS", font=('Times', 16), fg="#9fa8da")
        labelform.place(x=70, y=30)

        labelid = tk.Label(self.frame_dinamyc, text="ID:", font=('Times', 14))
        labelid.place(x=70, y=100)
        self.cid = tk.Entry(self.frame_dinamyc, width=40)
        self.cid.place(x=220, y=100)

        labelnombre = tk.Label(self.frame_dinamyc, text="Nombre:", font=('Times', 14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=40)
        self.cnombre.place(x=220, y=130)

        labelprecio = tk.Label(self.frame_dinamyc, text="Precio:", font=('Times', 14))
        labelprecio.place(x=70, y=160)
        self.cprecio = tk.Entry(self.frame_dinamyc, width=40)
        self.cprecio.place(x=220, y=160)

        labelstock = tk.Label(self.frame_dinamyc, text="Stock:", font=('Times', 14))
        labelstock.place(x=500, y=100)
        self.cstock = tk.Entry(self.frame_dinamyc, width=40)
        self.cstock.place(x=600, y=100)

        labelimagen = tk.Label(self.frame_dinamyc, text="Ruta Imagen:", font=('Times', 14))
        labelimagen.place(x=500, y=130)
        self.cimagen = tk.Entry(self.frame_dinamyc, width=40)
        self.cimagen.place(x=600, y=130)

        labelcategoria = tk.Label(self.frame_dinamyc, text="Categoría:", font=('Times', 14))
        labelcategoria.place(x=500, y=160)
        self.ccategoria = tk.Entry(self.frame_dinamyc, width=40)
        self.ccategoria.place(x=600, y=160)

        btnguardar = tk.Button(self.frame_dinamyc, text="GUARDAR", font=('Times', 14), command=self.save_producto)
        btnguardar.place(x=870, y=130)

    def listar_productos(self):
        tk.Label(self.frame_dinamyc, text="LISTADO DE PRODUCTOS", font=('Times', 16), fg="#9fa8da").place(x=70, y=200)
        self.tablaproductos = ttk.Treeview(self.frame_dinamyc, columns=("Nombre", "Precio", "Stock", "Imagen", "Categoría"))
        self.tablaproductos.heading("#0", text="ID")
        self.tablaproductos.heading("Nombre", text="Nombre")
        self.tablaproductos.heading("Precio", text="Precio")
        self.tablaproductos.heading("Stock", text="Stock")
        self.tablaproductos.heading("Imagen", text="Imagen")
        self.tablaproductos.heading("Categoría", text="Categoría")
        
        self.product_images = {}  # Dictionary to hold the images to prevent garbage collection
        
        with open("D:\LoginApp\db_products.json", "r", encoding='utf-8') as self.file:
            self.db_products = json.load(self.file)
            for producto in self.db_products["productos"]:
                try:
                    img = Image.open(producto["image_path"])
                    img = img.resize((50, 50), Image.ANTIALIAS)  # Resize image to fit in the Treeview
                    photo = ImageTk.PhotoImage(img)
                    self.product_images[producto["id"]] = photo
                    image_item = self.product_images[producto["id"]]
                except Exception as e:
                    image_item = "No image"
                
                self.tablaproductos.insert("", "end", text=f'{producto["id"]}', 
                                        values=(f'{producto["nombre"]}', f'{producto["precio"]}', f'{producto["stock"]}', image_item, f'{producto["categoria"]}'))
        self.tablaproductos.place(x=70, y=250)
        
        btneliminar = tk.Button(self.frame_dinamyc, text="Eliminar", font=('Times', 14), command=self.delete_producto)
        btneliminar.place(x=70, y=520)
        btnupdate = tk.Button(self.frame_dinamyc, text="Actualizar", font=('Times', 14), command=self.update_producto)
        btnupdate.place(x=200, y=520)

    def save_producto(self):
        if self.cid.get() == "" or self.cnombre.get() == "" or self.cprecio.get() == "" or self.cstock.get() == "" or self.cimagen.get() == "" or self.ccategoria.get() == "":
            messagebox.showinfo('Info', "Debe llenar todos los campos", parent=self)
            return
        else:
            with open("D:\LoginApp\db_products.json", "r", encoding='utf-8') as self.file:
                self.db_products = json.load(self.file)

                if self.tipo_action == "Actualizar":
                    for producto in self.db_products["productos"]:
                        if producto["id"] == self.tablaproductos.item(self.tablaproductos.selection())["text"]:
                            producto["nombre"] = self.cnombre.get()
                            producto["precio"] = self.cprecio.get()
                            producto["stock"] = self.cstock.get()
                            producto["image_path"] = self.cimagen.get()
                            producto["categoria"] = self.ccategoria.get()
                            with open('D:\LoginApp\db_products.json', 'w') as jf:
                                json.dump(self.db_products, jf, indent=4, ensure_ascii=True)
                                messagebox.showinfo('Info', "Producto actualizado con éxito", parent=self)
                                self.limpiar_panel(self.frame_dinamyc)
                else:
                    self.db_products["productos"].append({
                        'id': self.cid.get(),
                        'nombre': self.cnombre.get(),
                        'precio': self.cprecio.get(),
                        'stock': self.cstock.get(),
                        'image_path': self.cimagen.get(),
                        'categoria': self.ccategoria.get()
                    })
                    with open('D:\LoginApp\db_products.json', 'w') as jf:
                        json.dump(self.db_products, jf, indent=4, ensure_ascii=True)
                        messagebox.showinfo('Info', "Producto registrado con éxito", parent=self)
                        self.limpiar_panel(self.frame_dinamyc)

    def delete_producto(self):
        with open("D:\LoginApp\db_products.json", "r", encoding='utf-8') as self.file:
            self.db_products = json.load(self.file)
            for producto in self.db_products["productos"]:
                if producto["id"] == self.tablaproductos.item(self.tablaproductos.selection())["text"]:
                    self.db_products["productos"].remove(producto)
                    with open('D:\LoginApp\db_products.json', 'w') as jf:
                        json.dump(self.db_products, jf, indent=4, ensure_ascii=True)
                        messagebox.showinfo('Info', "Producto eliminado con éxito", parent=self)
                        self.limpiar_panel(self.frame_dinamyc)
                        break

    def update_producto(self):
        with open("D:\LoginApp\db_products.json", "r", encoding='utf-8') as self.file:
            self.db_products = json.load(self.file)
            for producto in self.db_products["productos"]:
                if producto["id"] == self.tablaproductos.item(self.tablaproductos.selection())["text"]:
                    self.cid.delete(0, tk.END)
                    self.cid.insert(0, producto["id"])
                    self.cid.config(state="disabled")
                    self.cnombre.delete(0, tk.END)
                    self.cnombre.insert(0, producto["nombre"])
                    self.cprecio.delete(0, tk.END)
                    self.cprecio.insert(0, producto["precio"])
                    self.cstock.delete(0, tk.END)
                    self.cstock.insert(0, producto["stock"])
                    self.cimagen.delete(0, tk.END)
                    self.cimagen.insert(0, producto["image_path"])
                    self.ccategoria.delete(0, tk.END)
                    self.ccategoria.insert(0, producto["categoria"])
                    self.tipo_action = "Actualizar"


