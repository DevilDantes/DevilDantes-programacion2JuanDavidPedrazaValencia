import tkinter as tk
from tkinter import messagebox, ttk
import json

class PProductos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Panel Productos")
        self.resizable(False, False)

        menubar = tk.Menu(self)
        menuproductos = tk.Menu(menubar, tearoff=0)
        menuproductos.add_command(label="Crear Producto", command=self.crear_producto_form)
        menuproductos.add_command(label="Listar Productos", command=self.listar_productos)
        menubar.add_cascade(label="Productos", menu=menuproductos)
        self.config(menu=menubar)

        self.frame_data = tk.Frame(self, bd=0, relief=tk.SOLID)
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)

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
