import tkinter as tk
import json
from tkinter import messagebox, ttk
import webbrowser
from PIL import Image, ImageTk
import util.generic as utl

class Clientes(tk.Tk):
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        self.tipo_action = "Guardar"
        self.tipo_user = ""
        self.carrito = {}
        super().__init__()
        self.title("Panel de Clientes")
        self.resizable(True, True)
        self.ancho_pantalla = self.winfo_screenwidth()
        self.alto_pantalla = self.winfo_screenheight()
        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")

        menubar = tk.Menu(self)
        menuuser = tk.Menu(menubar, tearoff=0)
        menuuser.add_command(label="Actualizar Perfil", command=self.formulario_actualizar_perfil)
        menubar.add_cascade(label="Usuarios", menu=menuuser)

        menuventas = tk.Menu(menubar, tearoff=0)
        menuventas.add_command(label="Carrito de Compras", command=self.ver_carrito)
        menubar.add_cascade(label="Ventas", menu=menuventas)

        self.config(menu=menubar)

        self.frame_user_info = tk.Frame(self, bd=0, relief=tk.SOLID, width=200)
        self.frame_user_info.pack(side=tk.LEFT, padx=4, pady=5, fill="y")
        texto = tk.Label(self.frame_user_info, text="Panel de Clientes", font=('Times', 20))
        texto.pack(padx=20, pady=4)
        self.usrimg = utl.leer_imagen(r"D:\\LoginApp\\imagenes\\userinfo.png", (128, 128))
        self.imgfacebook = utl.leer_imagen(r"D:\\LoginApp\\imagenes\\face.png", (32, 32))
        self.imglinkedin = utl.leer_imagen(r"D:\\LoginApp\\imagenes\\linkedin.png", (32, 32))
        self.imgwebsite = utl.leer_imagen(r"D:\\LoginApp\\imagenes\\website.png", (32, 32))
        tk.Label(self.frame_user_info, image=self.usrimg).pack(padx=30, pady=4)
        tk.Label(self.frame_user_info, text=self.name, font=('Times', 14)).pack(padx=40, pady=4)
        tk.Label(self.frame_user_info, text=self.email, font=('Times', 14)).pack(padx=50, pady=4)
        tk.Button(self.frame_user_info, image=self.imgfacebook, command=self.abrirface).place(x=100, y=300)
        tk.Button(self.frame_user_info, image=self.imglinkedin, command=self.abrirlink).place(x=140, y=300)
        tk.Button(self.frame_user_info, image=self.imgwebsite, command=self.abrirweb).place(x=180, y=300)

        self.frame_data = tk.Frame(self, bd=0, relief=tk.SOLID, width=f"{self.ancho_pantalla - 200}")
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)
        textobienvenida = tk.Label(self.frame_data, text="BIENVENIDO AL SISTEMA", font=('Times', 20))
        textobienvenida.pack(padx=20, pady=4)

        self.frame_dinamyc = tk.Frame(self.frame_data, bd=0, relief=tk.SOLID, width=f"{self.ancho_pantalla - 200}")
        self.frame_dinamyc.pack(side=tk.BOTTOM, padx=4, pady=5, fill="both", expand=1)

        # Variables para la búsqueda y categoría
        self.var_busqueda = tk.StringVar()
        self.var_categoria = tk.StringVar()

        # Añadir barra de búsqueda y menú desplegable de categorías
        self.frame_search = tk.Frame(self.frame_data)
        self.frame_search.pack(padx=10, pady=10, fill="x")

        tk.Label(self.frame_search, text="Buscar:", font=('Times', 12)).pack(side=tk.LEFT, padx=5)
        tk.Entry(self.frame_search, textvariable=self.var_busqueda, font=('Times', 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_search, text="Buscar", font=('Times', 12), command=self.listar_productos).pack(side=tk.LEFT, padx=5)

        tk.Label(self.frame_search, text="Categoría:", font=('Times', 12)).pack(side=tk.LEFT, padx=5)
        categorias = self.obtener_categorias()
        self.var_categoria.set("Todas")
        categoria_menu = ttk.Combobox(self.frame_search, textvariable=self.var_categoria, values=categorias, state='readonly')
        categoria_menu.pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_search, text="Filtrar", font=('Times', 12), command=self.listar_productos).pack(side=tk.LEFT, padx=5)

        # Llamar a la función para listar productos
        self.listar_productos()

    def formulario_actualizar_perfil(self):
        self.limpiar_panel(self.frame_dinamyc)

        frame_actualizar = tk.Frame(self.frame_dinamyc, bd=0, relief=tk.SOLID)
        frame_actualizar.pack(fill="both", expand=1, padx=10, pady=10)

        tk.Label(frame_actualizar, text="Actualizar Perfil", font=('Times', 20)).pack(pady=10)

        tk.Label(frame_actualizar, text="Nombre:", font=('Times', 14)).pack(pady=5)
        entry_nombre = tk.Entry(frame_actualizar, width=30, font=('Times', 14))
        entry_nombre.insert(0, self.name)
        entry_nombre.pack(pady=5)

        tk.Label(frame_actualizar, text="Usuario:", font=('Times', 14)).pack(pady=5)
        entry_usuario = tk.Entry(frame_actualizar, width=30, font=('Times', 14))
        entry_usuario.insert(0, self.username)
        entry_usuario.pack(pady=5)

        tk.Label(frame_actualizar, text="Correo Electrónico:", font=('Times', 14)).pack(pady=5)
        entry_email = tk.Entry(frame_actualizar, width=30, font=('Times', 14))
        entry_email.insert(0, self.email)
        entry_email.pack(pady=5)

        tk.Label(frame_actualizar, text="Contraseña:", font=('Times', 14)).pack(pady=5)
        entry_password = tk.Entry(frame_actualizar, width=30, font=('Times', 14), show="*")
        entry_password.pack(pady=5)

        tk.Button(frame_actualizar, text="Actualizar", font=('Times', 14), command=lambda: self.actualizar_perfil(entry_nombre, entry_usuario, entry_email, entry_password)).pack(pady=20)

    def actualizar_perfil(self, entry_nombre, entry_usuario, entry_email, entry_password):
        nuevo_nombre = entry_nombre.get()
        nuevo_usuario = entry_usuario.get()
        nuevo_email = entry_email.get()
        nueva_password = entry_password.get()

        if not nuevo_nombre or not nuevo_usuario or not nuevo_email:
            messagebox.showerror("Error", "Todos los campos excepto la contraseña son obligatorios", parent=self)
            return

        with open("D:\\LoginApp\\db_users.json", "r", encoding='utf-8') as file:
            db_users = json.load(file)

        for user in db_users["usuarios"]:
            if user["username"] == self.username:
                user["name"] = nuevo_nombre
                user["username"] = nuevo_usuario
                user["email"] = nuevo_email
                if nueva_password:
                    user["password"] = nueva_password
                break

        with open("D:\\LoginApp\\db_users.json", "w", encoding='utf-8') as file:
            json.dump(db_users, file, indent=4, ensure_ascii=False)

        self.name = nuevo_nombre
        self.username = nuevo_usuario
        self.email = nuevo_email

        tk.Label(self.frame_user_info, text=self.name, font=('Times', 14)).pack(padx=40, pady=4)
        tk.Label(self.frame_user_info, text=self.email, font=('Times', 14)).pack(padx=50, pady=4)

        messagebox.showinfo("Éxito", "Perfil actualizado exitosamente", parent=self)

    def main_productos(self):
        self.limpiar_panel(self.frame_dinamyc)
        tk.Label(self.frame_dinamyc, text="PRODUCTOS A LA VENTA", font=('Times', 16), fg="#9fa8da").pack(padx=20, pady=4)

        # Llamar a la función para listar productos
        self.listar_productos()

    def obtener_categorias(self):
        with open("D:\\LoginApp\\db_products.json", "r", encoding='utf-8') as file:
            productos = json.load(file)["productos"]
            categorias = list(set(producto["categoria"] for producto in productos))
            categorias.insert(0, "Todas")
        return categorias

    def listar_productos(self):
        self.limpiar_panel(self.frame_dinamyc)

        frame_productos = tk.Frame(self.frame_dinamyc)
        frame_productos.pack(fill="both", expand=1, padx=10, pady=10)

        self.tablaproductos = ttk.Treeview(frame_productos, columns=("Nombre", "Precio", "Stock", "Categoría", "Imagen"))
        self.tablaproductos.heading("#0", text="ID")
        self.tablaproductos.heading("Nombre", text="Nombre")
        self.tablaproductos.heading("Precio", text="Precio")
        self.tablaproductos.heading("Stock", text="Stock")
        self.tablaproductos.heading("Imagen", text="Imagen")
        self.tablaproductos.heading("Categoría", text="Categoría")

        scrollbar_vertical = ttk.Scrollbar(frame_productos, orient="vertical", command=self.tablaproductos.yview)
        self.tablaproductos.configure(yscroll=scrollbar_vertical.set)
        scrollbar_vertical.pack(side="right", fill="y")

        self.tablaproductos.pack(fill="both", expand=1)

        with open("D:\\LoginApp\\db_products.json", "r", encoding='utf-8') as file:
            productos = json.load(file)["productos"]

        busqueda = self.var_busqueda.get().lower()
        categoria = self.var_categoria.get()
        productos_filtrados = [
            producto for producto in productos
            if (busqueda in producto["nombre"].lower()) and (categoria == "Todas" or producto["categoria"] == categoria)
        ]

        for producto in productos_filtrados:
            self.tablaproductos.insert("", "end", text=f'{producto["id"]}', values=(f'{producto["nombre"]}', f'{producto["precio"]}', f'{producto["stock"]}', f'{producto["categoria"]}', f'{producto["image_path"]}'))

        self.var_cantidad = tk.IntVar()
        tk.Label(self.frame_dinamyc, text="Cantidad:", font=('Times', 14)).pack(pady=5)
        tk.Entry(self.frame_dinamyc, textvariable=self.var_cantidad, font=('Times', 14)).pack(pady=5)

        btn_agregar_carrito = tk.Button(self.frame_dinamyc, text="Agregar al Carrito", font=('Times', 14), command=self.agregar_al_carrito)
        btn_agregar_carrito.pack(pady=10)

    def agregar_al_carrito(self):
        selected_item = self.tablaproductos.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un producto para agregar al carrito")
            return

        cantidad = self.var_cantidad.get()
        if cantidad <= 0:
            messagebox.showwarning("Advertencia", "Ingrese una cantidad válida")
            return

        producto_id = self.tablaproductos.item(selected_item)["text"]
        producto_info = self.tablaproductos.item(selected_item)["values"]

        with open("D:\\LoginApp\\db_products.json", "r", encoding='utf-8') as file:
            productos = json.load(file)["productos"]

        for producto in productos:
            if producto["id"] == producto_id:
                if producto["stock"] == 0:
                    messagebox.showwarning("Advertencia", "El producto está agotado")
                    return
                if producto["stock"] >= cantidad:
                    if producto_id in self.carrito:
                        if self.carrito[producto_id]["cantidad"] + cantidad <= producto["stock"]:
                            self.carrito[producto_id]["cantidad"] += cantidad
                        else:
                            messagebox.showwarning("Advertencia", "No hay suficiente stock disponible para esta cantidad")
                            return
                    else:
                        self.carrito[producto_id] = {
                            "nombre": producto_info[0],
                            "precio": producto_info[1],
                            "stock": producto["stock"],
                            "cantidad": cantidad
                        }
                    messagebox.showinfo('Info', f'Producto {producto["nombre"]} agregado al carrito', parent=self)
                    return
                else:
                    messagebox.showwarning("Advertencia", "No hay stock disponible para esta cantidad")
                    return

    def ver_carrito(self):
        self.limpiar_panel(self.frame_dinamyc)
        tk.Label(self.frame_dinamyc, text="CARRITO DE COMPRAS", font=('Times', 16), fg="#9fa8da").pack(padx=20, pady=4)

        frame_carrito = tk.Frame(self.frame_dinamyc)
        frame_carrito.pack(fill="both", expand=1, padx=10, pady=10)

        self.tablacarrito = ttk.Treeview(frame_carrito, columns=("Nombre", "Precio", "Cantidad", "Total"))
        self.tablacarrito.heading("#0", text="ID")
        self.tablacarrito.heading("Nombre", text="Nombre")
        self.tablacarrito.heading("Precio", text="Precio")
        self.tablacarrito.heading("Cantidad", text="Cantidad")
        self.tablacarrito.heading("Total", text="Total")

        scrollbar_vertical = ttk.Scrollbar(frame_carrito, orient="vertical", command=self.tablacarrito.yview)
        self.tablacarrito.configure(yscroll=scrollbar_vertical.set)
        scrollbar_vertical.pack(side="right", fill="y")

        self.tablacarrito.pack(fill="both", expand=1)

        total_a_pagar = 0
        for producto_id, detalles in self.carrito.items():
            total = float(detalles["precio"]) * detalles["cantidad"]
            total_a_pagar += total
            self.tablacarrito.insert("", "end", text=producto_id, values=(detalles["nombre"], detalles["precio"], detalles["cantidad"], total))

        tk.Label(self.frame_dinamyc, text=f"Total a Pagar: ${total_a_pagar:.2f}", font=('Times', 16)).pack(pady=10)
        tk.Button(self.frame_dinamyc, text="Procesar Compra", font=('Times', 14), command=self.procesar_compra).pack(pady=10)

    def procesar_compra(self):
        with open("D:\\LoginApp\\db_products.json", "r", encoding='utf-8') as file:
            productos = json.load(file)

        for producto_id, detalles in self.carrito.items():
            for producto in productos["productos"]:
                if producto["id"] == producto_id:
                    producto["stock"] -= detalles["cantidad"]

        with open('D:\\LoginApp\\db_products.json', 'w', encoding='utf-8') as file:
            json.dump(productos, file, indent=4, ensure_ascii=False)

        messagebox.showinfo("Éxito", "Compra procesada exitosamente", parent=self)
        self.carrito = {}
        self.ver_carrito()

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()

    def abrirface(self):
        url = "https://www.facebook.com"
        webbrowser.open_new_tab(url)

    def abrirlink(self):
        url = "https://www.linkedin.com"
        webbrowser.open_new_tab(url)

    def abrirweb(self):
        url = "https://itcloud.com.co"
        webbrowser.open_new_tab(url)
