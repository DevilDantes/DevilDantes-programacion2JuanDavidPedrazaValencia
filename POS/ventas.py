import json
from tkinter import *
from tkinter import ttk, messagebox
import ttkbootstrap as tb

class Ventana(tb.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.ventana_login()

    def leer_usuarios(self):
        try:
            with open("D:\DevilDantes-programacion2JuanDavidPedrazaValencia-main\POS\database.json", "r", encoding='utf-8') as file:
                return json.load(file)["users"]
        except FileNotFoundError:
            return []

    def guardar_usuarios(self, usuarios):
        with open("D:\DevilDantes-programacion2JuanDavidPedrazaValencia-main\POS\database.json", "w", encoding='utf-8') as file:
            json.dump({"users": usuarios}, file, indent=4)

    def ventana_login(self):
        self.frame_login = Frame(self)
        self.frame_login.pack(fill=BOTH, expand=True)

        self.lblframe_login = LabelFrame(self.frame_login, text='Acceso')
        self.lblframe_login.pack(padx=10, pady=10, fill=BOTH, expand=True)

        lbltitulo = ttk.Label(self.lblframe_login, text='Inicio de sesión', font=("Times", 22))
        lbltitulo.pack(padx=10, pady=10)

        self.txt_usuario = ttk.Entry(self.lblframe_login, width=40)
        self.txt_usuario.pack(padx=10, pady=10)

        self.txt_clave = ttk.Entry(self.lblframe_login, width=40, show='*')
        self.txt_clave.pack(padx=10, pady=10)

        btn_acceso = ttk.Button(self.lblframe_login, text='Login', width=38, command=self.logueo)
        btn_acceso.pack(padx=10, pady=10)

    def ventana_menu(self):
        self.frame_left = Frame(self)
        self.frame_left.grid(row=0, column=0, sticky=NS)
        self.frame_center = Frame(self)
        self.frame_center.grid(row=0, column=1, sticky=NSEW)
        self.frame_right = Frame(self, width=400)
        self.frame_right.grid(row=0, column=2, sticky=NSEW)

        for idx, text in enumerate(['Productos', 'Ventas', 'Clientes', 'Compras', 'Usuario', 'Reportes', 'Backup', 'Restaurar DB']):
            command = self.ventana_lista_usuarios if text == 'Usuario' else None
            btn = ttk.Button(self.frame_left, text=text, width=15, command=command)
            btn.grid(row=idx, column=0, padx=10, pady=5)

        lbl2 = Label(self.frame_center, text='Aquí pondremos las ventanas que creemos')
        lbl2.grid(row=0, column=0, padx=10, pady=10)

        lbl3 = Label(self.frame_right, text='Aquí pondremos las búsquedas para la ventana')
        lbl3.grid(row=0, column=0, padx=10, pady=10)

    def logueo(self):
        usuarios = self.leer_usuarios()
        nombre_usuario = self.txt_usuario.get()
        contraseña_usuario = self.txt_clave.get()

        for usuario in usuarios:
            if usuario['username'] == nombre_usuario and usuario['password'] == contraseña_usuario:
                self.frame_login.pack_forget()
                self.ventana_menu()
                return

        messagebox.showerror('Acceso', 'El usuario o la contraseña son incorrectos. Intente de nuevo.')

    def ventana_lista_usuarios(self):
        self.frame_lista_usuarios = Frame(self.frame_center)
        self.frame_lista_usuarios.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.lblframe_botones_listusu = LabelFrame(self.frame_lista_usuarios)
        self.lblframe_botones_listusu.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        btn_nuevo_usuario = tb.Button(self.lblframe_botones_listusu, text='Nuevo', width=15, bootstyle='success', command=self.nuevo_usuario)
        btn_nuevo_usuario.grid(row=0, column=0, padx=5, pady=5)
        btn_actualizar_usuario = tb.Button(self.lblframe_botones_listusu, text='Actualizar', width=15, bootstyle='info', command=self.actualizar_usuario)
        btn_actualizar_usuario.grid(row=0, column=1, padx=5, pady=5)
        btn_eliminar_usuario = tb.Button(self.lblframe_botones_listusu, text='Eliminar', width=15, bootstyle='danger', command=self.eliminar_usuario)
        btn_eliminar_usuario.grid(row=0, column=2, padx=5, pady=5)

        self.lblframe_busqueda_listusu = LabelFrame(self.frame_lista_usuarios)
        self.lblframe_busqueda_listusu.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

        txt_busqueda_usuarios = ttk.Entry(self.lblframe_busqueda_listusu, width=95)
        txt_busqueda_usuarios.grid(row=0, column=0, padx=5, pady=5)

        self.lblframe_tree_listusu = LabelFrame(self.frame_lista_usuarios)
        self.lblframe_tree_listusu.grid(row=2, column=0, padx=10, pady=10, sticky=NSEW)

        columnas = ("id", "name", "lastname", "username", "password", "role")
        self.tree_lista_usuarios = ttk.Treeview(self.lblframe_tree_listusu, columns=columnas, height=17, show='headings')
        self.tree_lista_usuarios.grid(row=0, column=0, sticky=NSEW)

        self.tree_lista_usuarios.heading("id", text="ID", anchor=W)
        self.tree_lista_usuarios.heading("name", text="Nombre", anchor=W)
        self.tree_lista_usuarios.heading("lastname", text="Apellido", anchor=W)
        self.tree_lista_usuarios.heading("username", text="Usuario", anchor=W)
        self.tree_lista_usuarios.heading("password", text="Contraseña", anchor=W)
        self.tree_lista_usuarios.heading("role", text="Rol", anchor=W)
        self.tree_lista_usuarios['displaycolumns'] = ("id", "name", "lastname", "username", "password", "role")

        tree_scroll_listausu = ttk.Scrollbar(self.lblframe_tree_listusu, orient=VERTICAL, command=self.tree_lista_usuarios.yview)
        self.tree_lista_usuarios.configure(yscroll=tree_scroll_listausu.set)
        tree_scroll_listausu.grid(row=0, column=1, sticky=NS)

        self.mostrar_usuarios()

    def mostrar_usuarios(self):
        usuarios = self.leer_usuarios()
        registros = self.tree_lista_usuarios.get_children()
        for elementos in registros:
            self.tree_lista_usuarios.delete(elementos)
        for usuario in usuarios:
            self.tree_lista_usuarios.insert("", "end", text=usuario['id'], values=(usuario['id'], usuario['name'], usuario['lastname'], usuario['username'], usuario['password'], usuario['role']))

    def nuevo_usuario(self):
        ventana_nuevo_usuario = Toplevel(self)
        ventana_nuevo_usuario.title("Nuevo Usuario")
        ventana_nuevo_usuario.geometry("400x300")

        Label(ventana_nuevo_usuario, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        txt_nombre = Entry(ventana_nuevo_usuario)
        txt_nombre.grid(row=0, column=1, padx=10, pady=10)

        Label(ventana_nuevo_usuario, text="Apellido").grid(row=1, column=0, padx=10, pady=10)
        txt_apellido = Entry(ventana_nuevo_usuario)
        txt_apellido.grid(row=1, column=1, padx=10, pady=10)

        Label(ventana_nuevo_usuario, text="Usuario").grid(row=2, column=0, padx=10, pady=10)
        txt_usuario = Entry(ventana_nuevo_usuario)
        txt_usuario.grid(row=2, column=1, padx=10, pady=10)

        Label(ventana_nuevo_usuario, text="Contraseña").grid(row=3, column=0, padx=10, pady=10)
        txt_contraseña = Entry(ventana_nuevo_usuario, show='*')
        txt_contraseña.grid(row=3, column=1, padx=10, pady=10)

        Label(ventana_nuevo_usuario, text="Rol").grid(row=4, column=0, padx=10, pady=10)
        txt_rol = Entry(ventana_nuevo_usuario)
        txt_rol.grid(row=4, column=1, padx=10, pady=10)

        btn_guardar = Button(ventana_nuevo_usuario, text="Guardar", command=lambda: self.guardar_nuevo_usuario(txt_nombre.get(), txt_apellido.get(), txt_usuario.get(), txt_contraseña.get(), txt_rol.get(), ventana_nuevo_usuario))
        btn_guardar.grid(row=5, column=0, columnspan=2, pady=10)

    def guardar_nuevo_usuario(self, nombre, apellido, usuario, contraseña, rol, ventana):
        usuarios = self.leer_usuarios()
        nuevo_id = str(len(usuarios) + 1)
        nuevo_usuario = {
            "id": nuevo_id,
            "name": nombre,
            "lastname": apellido,
            "username": usuario,
            "password": contraseña,
            "role": rol
        }
        usuarios.append(nuevo_usuario)
        self.guardar_usuarios(usuarios)
        self.mostrar_usuarios()
        ventana.destroy()

    def actualizar_usuario(self):
        item_seleccionado = self.tree_lista_usuarios.selection()
        if item_seleccionado:
            item = self.tree_lista_usuarios.item(item_seleccionado)
            id_usuario = item['text']
            usuarios = self.leer_usuarios()
            for usuario in usuarios:
                if usuario['id'] == id_usuario:
                    usuario['name'] = "NombreActualizado"
                    usuario['lastname'] = "ApellidoActualizado"
                    usuario['username'] = "UsuarioActualizado"
                    usuario['password'] = "ContraseñaActualizada"
                    usuario['role'] = "admin"
            self.guardar_usuarios(usuarios)
            self.mostrar_usuarios()

    def eliminar_usuario(self):
        item_seleccionado = self.tree_lista_usuarios.selection()
        if item_seleccionado:
            item = self.tree_lista_usuarios.item(item_seleccionado)
            id_usuario = item['text']
            usuarios = self.leer_usuarios()
            usuarios = [usuario for usuario in usuarios if usuario['id'] != id_usuario]
            self.guardar_usuarios(usuarios)
            self.mostrar_usuarios()

def main():
    app = Ventana()
    app.title('Sistema POS')
    app.state('zoomed')
    app.mainloop()

if __name__ == '__main__':
    main()