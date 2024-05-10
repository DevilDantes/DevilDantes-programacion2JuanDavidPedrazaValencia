import tkinter as tk


class PAdmin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Panel Administrativo")
        self.resizable(False, False)
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight() 

        self.geometry(f"{ancho_pantalla}x{alto_pantalla}")

        frame_menu_lateral = tk.Frame(self, bd=0, width=300,relief=tk.SOLID)
        frame_menu_lateral.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        menu=tk.Label(frame_menu_lateral, text="menu", font=('Times', 20))
        menu.pack(padx=10,pady=30)


        frame_panel_informativo = tk.Frame(self, bd=0,relief=tk.SOLID)
        frame_panel_informativo.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)
        texto=tk.Label(frame_panel_informativo, text="Panel Adminstrativo", font=('Times', 20))
        texto.pack(padx=10,pady=30)
