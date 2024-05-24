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
        super().__init__()
        self.title("Panel de Clientes")
        self.resizable(False, False)
        self.ancho_pantalla = self.winfo_screenwidth()
        self.alto_pantalla = self.winfo_screenheight()
        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")

        menubar = tk.Menu(self)
        menuclientes = tk.Menu(menubar, tearoff=0)
        menuclientes.add_command(label="Administracion de Cliente")
        menubar.add_cascade(label="Clientes", menu=menuclientes)

        menucategorias = tk.Menu(menubar, tearoff=0)
        menucategorias.add_command(label="Administracion de Categorias")
        menubar.add_cascade(label="Categorias", menu=menucategorias)

        menuproducto = tk.Menu(menubar, tearoff=0)
        menuproducto.add_command(label="Administracion de Productos")
        menubar.add_cascade(label="Productos", menu=menuproducto)

        menuventas = tk.Menu(menubar, tearoff=0)
        menuventas.add_command(label="Administracion de Ventas")
        menubar.add_cascade(label="Ventas", menu=menuventas)

        self.config(menu=menubar)

        self.frame_user_info = tk.Frame(self, bd=0, relief=tk.SOLID, width=200)
        self.frame_user_info.pack(side=tk.LEFT, padx=4, pady=5, fill="y")
        texto = tk.Label(self.frame_user_info, text="Panel de Clientes", font=('Times', 20))
        texto.pack(padx=20, pady=4)
        self.usrimg = utl.leer_imagen(r"D:\LoginApp\imagenes\userinfo.png", (128, 128))
        self.imgfacebook = utl.leer_imagen(r"D:\LoginApp\imagenes\face.png", (32, 32))
        self.imglinkedin = utl.leer_imagen(r"D:\LoginApp\imagenes\linkedin.png", (32, 32))
        self.imgwebsite = utl.leer_imagen(r"D:\LoginApp\imagenes\website.png", (32, 32))
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

    def main_productos(self):
        self.limpiar_panel(self.frame_dinamyc)
        tk.Label(self.frame_dinamyc, text="PRODUCTOS A LA VENTA", font=('Times', 16), fg="#9fa8da").pack(padx=20, pady=4)

        # Llamar a la función para listar productos
        self.listar_productos()

    def obtener_categorias(self):
        with open("D:\LoginApp\db_products.json", "r", encoding='utf-8') as file:
            productos = json.load(file)["productos"]
            categorias = list(set(producto["categoria"] for producto in productos))
            categorias.insert(0, "Todas")
        return categorias

    def listar_productos(self):
        # Limpiar el frame
        self.limpiar_panel(self.frame_dinamyc)

        frame_productos = tk.Frame(self.frame_dinamyc)
        frame_productos.pack(fill="both", expand=1, padx=10, pady=10)

        self.tabla_productos = ttk.Treeview(frame_productos, columns=("Nombre", "Precio", "Stock", "Categoría"))
        self.tabla_productos.heading("#0", text="ID")
        self.tabla_productos.heading("Nombre", text="Nombre")
        self.tabla_productos.heading("Precio", text="Precio")
        self.tabla_productos.heading("Stock", text="Stock")
        self.tabla_productos.heading("Categoría", text="Categoría")

        scrollbar_vertical = ttk.Scrollbar(frame_productos, orient="vertical", command=self.tabla_productos.yview)
        self.tabla_productos.configure(yscroll=scrollbar_vertical.set)
        scrollbar_vertical.pack(side="right", fill="y")

        self.tabla_productos.pack(fill="both", expand=1)

        with open("D:\LoginApp\db_products.json", "r", encoding='utf-8') as file:
            productos = json.load(file)["productos"]

        # Filtrar productos por búsqueda y categoría
        busqueda = self.var_busqueda.get().lower()
        categoria = self.var_categoria.get()
        productos_filtrados = [
            producto for producto in productos
            if (busqueda in producto["nombre"].lower()) and (categoria == "Todas" or producto["categoria"] == categoria)
        ]

        for producto in productos_filtrados:
            self.tabla_productos.insert("", "end", text=f'{producto["id"]}', values=(f'{producto["nombre"]}', f'{producto["precio"]}', f'{producto["stock"]}', f'{producto["categoria"]}'))

        btn_vender = tk.Button(self.frame_dinamyc, text="Vender", font=('Times', 14), command=self.vender_producto)
        btn_vender.pack(pady=10)

    def vender_producto(self):
        selected_item = self.tabla_productos.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un producto para vender")
            return

        producto_id = self.tabla_productos.item(selected_item)["text"]

        with open("D:\LoginApp\db_products.json", "r", encoding='utf-8') as file:
            productos = json.load(file)

        for producto in productos["productos"]:
            if producto["id"] == producto_id:
                if producto["stock"] > 0:
                    producto["stock"] -= 1
                    with open('D:\LoginApp\db_products.json', 'w') as jf:
                        json.dump(productos, jf, indent=4, ensure_ascii=True)
                        messagebox.showinfo('Info', f'Producto {producto["nombre"]} vendido con éxito', parent=self)
                        self.listar_productos()
                        return
                else:
                    messagebox.showwarning("Advertencia", "No hay stock disponible para este producto")
                    return

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


