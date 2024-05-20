import tkinter as tk
from tkinter import messagebox, ttk
import json

class PCategorias(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Panel Categorías")
        self.resizable(False, False)
        
        menubar = tk.Menu(self)
        menucategorias = tk.Menu(menubar, tearoff=0)
        menucategorias.add_command(label="Crear Categoría", command=self.crear_categoria_form)
        menucategorias.add_command(label="Listar Categorías", command=self.listar_categorias)
        menubar.add_cascade(label="Categorías", menu=menucategorias)
        self.config(menu=menubar)
        
        self.frame_data = tk.Frame(self, bd=0, relief=tk.SOLID)
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)

    def crear_categoria_form(self):
        self.limpiar_panel(self.frame_data)
        labelform = tk.Label(self.frame_data, text="REGISTRO DE CATEGORÍAS", font=('Times', 16), fg="#9fa8da")
        labelform.place(x=70, y=70)
        
        labelnombre = tk.Label(self.frame_data, text="Nombre:", font=('Times', 14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_data, width=80)
        self.cnombre.place(x=220, y=130)

        btnguardar = tk.Button(self.frame_data, text="GUARDAR", font=('Times', 14), command=self.save_categoria)
        btnguardar.place(x=220, y=200)
    
    def save_categoria(self):
        new_categoria = {
            "nombre": self.cnombre.get(),
        }

        try:
            with open("categorias.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"categorias": []}

        data["categorias"].append(new_categoria)

        with open("categorias.json", "w") as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo('Info', "Categoría registrada con éxito", parent=self)
        self.limpiar_panel(self.frame_data)

    def listar_categorias(self):
        self.limpiar_panel(self.frame_data)
        labelform = tk.Label(self.frame_data, text="LISTADO DE CATEGORÍAS", font=('Times', 16), fg="#9fa8da")
        labelform.place(x=70, y=70)
        
        self.tablacategorias = ttk.Treeview(self.frame_data, columns=("Nombre"))
        self.tablacategorias.heading("#0", text="ID")
        self.tablacategorias.heading("Nombre", text="Nombre")

        try:
            with open("categorias.json", "r") as file:
                data = json.load(file)
                for i, categoria in enumerate(data["categorias"], start=1):
                    self.tablacategorias.insert("", "end", text=str(i), values=(categoria["nombre"]))
        except FileNotFoundError:
            pass

        self.tablacategorias.place(x=70, y=100)

    def limpiar_panel(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = PCategorias()
    app.mainloop()
