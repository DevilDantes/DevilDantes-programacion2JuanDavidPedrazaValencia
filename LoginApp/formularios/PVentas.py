import tkinter as tk
from tkinter import messagebox, ttk
import json
import util.generic as utl

class PVentas(tk.Tk):
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        super().__init__()
        self.title("Panel Ventas")
        self.resizable(False, False)
        
        # Obtener las dimensiones de la pantalla
        self.ancho_pantalla = self.winfo_screenwidth() #método para obtener Ancho
        self.alto_pantalla = self.winfo_screenheight() #método para obtener Alto

        # Establecer el tamaño completo de la ventana
        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")
        
        menubar = tk.Menu(self)  

        menuclientes = tk.Menu(menubar, tearoff=0)
        menuclientes.add_command(label="Crear Cliente", command=self.crear_cliente_form)  
        menuclientes.add_command(label="Listar Clientes", command=self.listar_clientes)  
        menubar.add_cascade(label="Clientes", menu=menuclientes)

        menuventas = tk.Menu(menubar, tearoff=0)
        menuventas.add_command(label="Crear Venta")  
        menuventas.add_command(label="Listar Ventas")  
        menubar.add_cascade(label="Ventas", menu=menuventas)

        menuproducto = tk.Menu(menubar, tearoff=0)
        menuproducto.add_command(label="Crear Producto", command=self.crear_producto_form)  
        menuproducto.add_command(label="Listar Productos", command=self.listar_productos)  
        menubar.add_cascade(label="Producto", menu=menuproducto)   

        self.config(menu=menubar)

        # frame user info
        self.frame_user_info = tk.Frame(self, bd=0, relief=tk.SOLID, width=200)
        self.frame_user_info.pack(side=tk.LEFT, padx=4, pady=5, fill="y")
        texto = tk.Label(self.frame_user_info, text="PANEL VENTAS", font=('Times', 20))
        texto.pack(padx=20, pady=4)
        usrimg = utl.leer_imagen(r"C:\Users\Javier\Downloads\PROGIITECNAR-main\PROGIITECNAR-main\Clase9\LoginApp\imagenes\userinfo.png", (48, 48))
        imgusr = tk.Label(self.frame_user_info, image=usrimg)
        imgusr.pack(padx=30, pady=4)
        texto1 = tk.Label(self.frame_user_info, text=self.name, font=('Times', 14))
        texto1.pack(padx=40, pady=4)
        texto1 = tk.Label(self.frame_user_info, text=self.email, font=('Times', 14))
        texto1.pack(padx=50, pady=4)
        
        # frame_data
        self.frame_data = tk.Frame(self, bd=0, relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)
        textobienvenida = tk.Label(self.frame_data, text="BIENVENIDO AL SISTEMA", font=('Times', 20))
        textobienvenida.pack(padx=20, pady=4)

        # frame_dinamyc
        self.frame_dinamyc = tk.Frame(self.frame_data, bd=0, relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_dinamyc.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)

    def crear_cliente_form(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc, text="\uf0c9 REGISTRO DE CLIENTES", font=('Times', 16), fg="#9fa8da")
        labelform.place(x=70, y=70)

        labelcedula = tk.Label(self.frame_dinamyc, text="Nombre completo:", font=('Times', 14))
        labelcedula.place(x=70, y=130)
        self.ccedula = tk.Entry(self.frame_dinamyc, width=80)
        self.ccedula.place(x=220, y=130)
        
        labelnombre = tk.Label(self.frame_dinamyc, text="Nombre completo:", font=('Times', 14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=80)
        self.cnombre.place(x=220, y=130)

        labeldireccion = tk.Label(self.frame_dinamyc, text="Dirección:", font=('Times', 14))
        labeldireccion.place(x=70, y=160)
        self.cdireccion = tk.Entry(self.frame_dinamyc, width=80)
        self.cdireccion.place(x=220, y=160)

        labeltelefono = tk.Label(self.frame_dinamyc, text="Teléfono:", font=('Times', 14))
        labeltelefono.place(x=70, y=190)
        self.ctelefono = tk.Entry(self.frame_dinamyc, width=80)
        self.ctelefono.place(x=220, y=190)

        labelcorreo = tk.Label(self.frame_dinamyc, text="Correo:", font=('Times', 14))
        labelcorreo.place(x=70, y=220)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=80)
        self.ccorreo.place(x=220, y=220)

        btnguardar = tk.Button(self.frame_dinamyc, text="\uf0c7 GUARDAR", font=('Times', 14), command=self.save_client)
        btnguardar.place(x=220, y=280)
    
    def save_client(self):
        new_client = {
            "cedula": self.ccedula.get(),
            "nombre": self.cnombre.get(),
            "direccion": self.cdireccion.get(),
            "telefono": self.ctelefono.get(),
            "correo": self.ccorreo.get()
        }

        # Leer el archivo JSON existente
        try:
            with open(r"C:\Users\Javier\Downloads\PROGIITECNAR-main\PROGIITECNAR-main\Clase9\LoginApp\clientes.json", 'w', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"clientes": []}

        # Agregar el nuevo cliente a la lista
        data["clientes"].append(new_client)

        # Escribir los datos actualizados en el archivo JSON
        with open("clientes.json", "w") as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo('Info', "Cliente registrado con éxito", parent=self)
        self.limpiar_panel(self.frame_dinamyc)

    def listar_clientes(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc, text="\uf00b LISTADO DE CLIENTES", font=('Times', 16), fg="#9fa8da")
        labelform.place(x=70, y=70)
        
        self.tablaclientes = ttk.Treeview(self.frame_dinamyc, columns=("Cedula","Nombre", "Direccion", "Telefono", "Correo"))
        self.tablaclientes.heading("#0", text="ID")
        self.tablaclientes.heading("Cedula", text="Cédula")
        self.tablaclientes.heading("Nombre", text="Nombre Completo")
        self.tablaclientes.heading("Direccion", text="Dirección")
        self.tablaclientes.heading("Telefono", text="Teléfono")
        self.tablaclientes.heading("Correo", text="Correo")

        try:
            with open(r"C:\Users\Javier\Downloads\PROGIITECNAR-main\PROGIITECNAR-main\Clase9\LoginApp\clientes.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
                for i, cliente in enumerate(data["clientes"], start=1):
                    self.tablaclientes.insert("", "end", text=str(i), values=(cliente["cedula"],cliente["nombre"], cliente["direccion"], cliente["telefono"], cliente["correo"]))
        except FileNotFoundError:
            pass

        self.tablaclientes.place(x=70, y=100)

        # Botones para actualizar y eliminar clientes
        btn_actualizar = tk.Button(self.frame_dinamyc, text="Actualizar", font=('Times', 14), command=self.actualizar_cliente)
        btn_actualizar.place(x=300, y=400)

        btn_eliminar = tk.Button(self.frame_dinamyc, text="Eliminar", font=('Times', 14), command=self.eliminar_cliente)
        btn_eliminar.place(x=400, y=400)

    def actualizar_cliente(self):
        selected_item = self.tablaclientes.selection()
        if not selected_item:
            messagebox.showwarning('Advertencia', 'Seleccione un cliente para actualizar.', parent=self)
            return

        item = self.tablaclientes.item(selected_item)
        cliente_id = item['text']

        with open("clientes.json", "r") as file:
            data = json.load(file)
            cliente = data["clientes"][int(cliente_id) - 1]

        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc, text="\uf0c9 ACTUALIZAR CLIENTE", font=('Times', 16), fg="#9fa8da")
        labelform.place(x=70, y=70)
        
        labelcedula = tk.Label(self.frame_dinamyc, text="Cedula:", font=('Times', 14))
        labelcedula.place(x=70, y=130)
        self.ccedula = tk.Entry(self.frame_dinamyc, width=80)
        self.ccedula.insert(0, cliente["cedula"])
        self.ccedula.place(x=220, y=130)
        
        labelnombre = tk.Label(self.frame_dinamyc, text="Nombre completo:", font=('Times', 14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=80)
        self.cnombre.insert(0, cliente["nombre"])
        self.cnombre.place(x=220, y=130)

        labeldireccion = tk.Label(self.frame_dinamyc, text="Dirección:", font=('Times', 14))
        labeldireccion.place(x=70, y=160)
        self.cdireccion = tk.Entry(self.frame_dinamyc, width=80)
        self.cdireccion.insert(0, cliente["direccion"])
        self.cdireccion.place(x=220, y=160)

        labeltelefono = tk.Label(self.frame_dinamyc, text="Teléfono:", font=('Times', 14))
        labeltelefono.place(x=70, y=190)
        self.ctelefono = tk.Entry(self.frame_dinamyc, width=80)
        self.ctelefono.insert(0, cliente["telefono"])
        self.ctelefono.place(x=220, y=190)

        labelcorreo = tk.Label(self.frame_dinamyc, text="Correo:", font=('Times', 14))
        labelcorreo.place(x=70, y=220)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=80)
        self.ccorreo.insert(0, cliente["correo"])
        self.ccorreo.place(x=220, y=220)

        btnguardar = tk.Button(self.frame_dinamyc, text="\uf0c7 ACTUALIZAR", font=('Times', 14), command=lambda: self.guardar_actualizacion_cliente(cliente_id))
        btnguardar.place(x=220, y=280)

    def guardar_actualizacion_cliente(self, cliente_id):
        with open(r"C:\Users\Javier\Downloads\PROGIITECNAR-main\PROGIITECNAR-main\Clase9\LoginApp\clientes.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            cliente = data["clientes"][int(cliente_id) - 1]
            cliente["cedula"] = self.ccedula.get()
            cliente["nombre"] = self.cnombre.get()
            cliente["direccion"] = self.cdireccion.get()
            cliente["telefono"] = self.ctelefono.get()
            cliente["correo"] = self.ccorreo.get()

        with open(r"C:\Users\Javier\Downloads\PROGIITECNAR-main\PROGIITECNAR-main\Clase9\LoginApp\clientes.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo('Info', "Cliente actualizado con éxito", parent=self)
        self.limpiar_panel(self.frame_dinamyc)
        self.listar_clientes()

    def eliminar_cliente(self):
        selected_item = self.tablaclientes.selection()
        if not selected_item:
            messagebox.showwarning('Advertencia', 'Seleccione un cliente para eliminar.', parent=self)
            return

        confirmar = messagebox.askyesno('Confirmar', '¿Está seguro que desea eliminar este cliente?', parent=self)
        if confirmar:
            item = self.tablaclientes.item(selected_item)
            cliente_id = item['text']

            with open("clientes.json", "r") as file:
                data = json.load(file)
                data["clientes"].pop(int(cliente_id) - 1)

            with open("clientes.json", "w") as file:
                json.dump(data, file, indent=4)

            messagebox.showinfo('Información', 'Cliente eliminado con éxito.', parent=self)
            self.listar_clientes()
    def crear_producto_form(self):
        self.limpiar_panel(self.frame_data)
        labelform = tk.Label(self.frame_data, text="REGISTRO DE PRODUCTOS", font=('Times', 16), fg="#9fa8da")
        labelform.place(x=70, y=70)

        labelnombre = tk.Label(self.frame_data, text="Nombre:", font=('Times', 14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_data, width=80)
        self.cnombre.place(x=220, y=130)

        labelcategoria = tk.Label(self.frame_data, text="Categoría:", font=('Times', 14))
        labelcategoria.place(x=70, y=160)
        self.ccategoria = tk.Entry(self.frame_data, width=80)
        self.ccategoria.place(x=220, y=160)

        labelprecio = tk.Label(self.frame_data, text="Precio:", font=('Times', 14))
        labelprecio.place(x=70, y=190)
        self.cprecio = tk.Entry(self.frame_data, width=80)
        self.cprecio.place(x=220, y=190)

        btnguardar = tk.Button(self.frame_data, text="GUARDAR", font=('Times', 14), command=self.save_producto)
        btnguardar.place(x=220, y=230)

    def save_producto(self):
        new_producto = {
            "nombre": self.cnombre.get(),
            "categoria": self.ccategoria.get(),
            "precio": self.cprecio.get()
        }

        try:
            with open("productos.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"productos": []}

        data["productos"].append(new_producto)

        with open("productos.json", "w") as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo('Info', "Producto registrado con éxito", parent=self)
        self.limpiar_panel(self.frame_data)

    def listar_productos(self):
        self.limpiar_panel(self.frame_data)
        labelform = tk.Label(self.frame_data, text="LISTADO DE PRODUCTOS", font=('Times', 16), fg="#9fa8da")
        labelform.place(x=70, y=70)

        self.tablaproductos = ttk.Treeview(self.frame_data, columns=("Nombre", "Categoría", "Precio"), show='headings')
        self.tablaproductos.heading("Nombre", text="Nombre")
        self.tablaproductos.heading("Categoría", text="Categoría")
        self.tablaproductos.heading("Precio", text="Precio")

        self.tablaproductos.place(x=70, y=100)

        try:
            with open("productos.json", "r") as file:
                data = json.load(file)
                for i, producto in enumerate(data["productos"], start=1):
                    self.tablaproductos.insert("", "end", values=(producto["nombre"], producto["categoria"], producto["precio"]))
        except FileNotFoundError:
            pass

        btn_actualizar = tk.Button(self.frame_data, text="Actualizar", font=('Times', 14), command=self.actualizar_producto_form)
        btn_actualizar.place(x=70, y=400)

        btn_eliminar = tk.Button(self.frame_data, text="Eliminar", font=('Times', 14), command=self.eliminar_producto)
        btn_eliminar.place(x=220, y=400)

    def actualizar_producto_form(self):
        selected_item = self.tablaproductos.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un producto para actualizar")
            return

        item = self.tablaproductos.item(selected_item)
        producto = item['values']

        self.limpiar_panel(self.frame_data)
        labelform = tk.Label(self.frame_data, text="ACTUALIZAR PRODUCTO", font=('Times', 16), fg="#9fa8da")
        labelform.place(x=70, y=70)

        labelnombre = tk.Label(self.frame_data, text="Nombre:", font=('Times', 14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_data, width=80)
        self.cnombre.insert(0, producto[0])
        self.cnombre.place(x=220, y=130)

        labelcategoria = tk.Label(self.frame_data, text="Categoría:", font=('Times', 14))
        labelcategoria.place(x=70, y=160)
        self.ccategoria = tk.Entry(self.frame_data, width=80)
        self.ccategoria.insert(0, producto[1])
        self.ccategoria.place(x=220, y=160)

        labelprecio = tk.Label(self.frame_data, text="Precio:", font=('Times', 14))
        labelprecio.place(x=70, y=190)
        self.cprecio = tk.Entry(self.frame_data, width=80)
        self.cprecio.insert(0, producto[2])
        self.cprecio.place(x=220, y=190)

        btnguardar = tk.Button(self.frame_data, text="ACTUALIZAR", font=('Times', 14), command=lambda: self.update_producto(selected_item))
        btnguardar.place(x=220, y=230)

    def update_producto(self, item):
        updated_producto = {
            "nombre": self.cnombre.get(),
            "categoria": self.ccategoria.get(),
            "precio": self.cprecio.get()
        }

        try:
            with open("productos.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"productos": []}

        item_index = self.tablaproductos.index(item)
        data["productos"][item_index] = updated_producto

        with open("productos.json", "w") as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo('Info', "Producto actualizado con éxito", parent=self)
        self.limpiar_panel(self.frame_data)
        self.listar_productos()

    def eliminar_producto(self):
        selected_item = self.tablaproductos.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un producto para eliminar")
            return

        item = self.tablaproductos.item(selected_item)
        producto = item['values']

        try:
            with open("productos.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"productos": []}

        data["productos"] = [p for p in data["productos"] if p["nombre"] != producto[0]]

        with open("productos.json", "w") as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo('Info', "Producto eliminado con éxito", parent=self)
        self.limpiar_panel(self.frame_data)
        self.listar_productos()


    def limpiar_panel(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
