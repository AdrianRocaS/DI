import customtkinter as ctk
import tkinter
from pathlib import Path
from PIL import Image


class MainView:
    def __init__(self, master):
        self.master = master

        # CONFIGURACIÓN DEL GRID PRINCIPAL
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=2)
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=0)

        # PANEL IZQUIERDO (Usuarios)
        self.frame_left = ctk.CTkFrame(master, corner_radius=10)
        self.frame_left.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)

        # Título
        self.label_usuarios = ctk.CTkLabel(
            self.frame_left, text="Usuarios", font=("Arial", 20, "bold")
        )
        self.label_usuarios.pack(pady=(10, 5))

        # Scrollable frame
        self.lista_scroll = ctk.CTkScrollableFrame(self.frame_left)
        self.lista_scroll.pack(fill="both", expand=True, padx=10, pady=10)

        # PANEL DERECHO (Detalles)
        self.frame_right = ctk.CTkFrame(master, corner_radius=10)
        self.frame_right.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

        # Título
        self.label_detalles = ctk.CTkLabel(
            self.frame_right, text="Detalles del Usuario", font=("Arial", 20, "bold")
        )
        self.label_detalles.pack(pady=(10, 5))

        # Labels de detalle
        self.detalle_nombre = ctk.CTkLabel(self.frame_right, text="Nombre: -", anchor="w")
        self.detalle_nombre.pack(padx=20, pady=8, anchor="nw")

        self.detalle_edad = ctk.CTkLabel(self.frame_right, text="Edad: -", anchor="w")
        self.detalle_edad.pack(padx=20, pady=8, anchor="nw")

        self.detalle_genero = ctk.CTkLabel(self.frame_right, text="Género: -", anchor="w")
        self.detalle_genero.pack(padx=20, pady=8, anchor="nw")

        self.detalle_avatar = ctk.CTkLabel(self.frame_right, text="Avatar: -", anchor="w")
        self.detalle_avatar.pack(padx=20, pady=8, anchor="nw")

        # Avatar imagen
        self.avatar_label = ctk.CTkLabel(self.frame_right, text="", image=None)
        self.avatar_label.pack(padx=20, pady=10, anchor="nw")

        # Mantener referencias
        self._image_refs = {}

        # PANEL INFERIOR (Añadir Usuario + Salir)
        self.frame_bottom = ctk.CTkFrame(master, corner_radius=10)
        self.frame_bottom.grid(row=1, column=0, columnspan=2, sticky="ew",
                               padx=15, pady=(0, 15))

        self.boton_añadir = ctk.CTkButton(self.frame_bottom, text="Añadir Usuario", width=150)
        self.boton_añadir.pack(side="left", padx=20, pady=10)

        self.boton_salir = ctk.CTkButton(self.frame_bottom, text="Salir",
                                         width=100, command=master.destroy)
        self.boton_salir.pack(side="right", padx=20, pady=10)

        # MENÚ SUPERIOR
        self.menubar = tkinter.Menu(master)
        master.config(menu=self.menubar)
        self.menu_archivo = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Archivo", menu=self.menu_archivo)

    # Actualización de la lista
    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):

        for child in self.lista_scroll.winfo_children():
            child.destroy()

        for i, usuario in enumerate(usuarios):
            boton = ctk.CTkButton(
                self.lista_scroll,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            boton.pack(fill="x", pady=5, padx=10)

    # Mostrar detalles
    def mostrar_detalles_usuario(self, usuario):

        if usuario is None:
            self.detalle_nombre.configure(text="Nombre: -")
            self.detalle_edad.configure(text="Edad: -")
            self.detalle_genero.configure(text="Género: -")
            self.detalle_avatar.configure(text="Avatar: -")
            self.avatar_label.configure(image=None, text="")
            return

        self.detalle_nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.detalle_edad.configure(text=f"Edad: {usuario.edad}")
        self.detalle_genero.configure(text=f"Género: {usuario.genero}")
        if usuario.avatar:
            self.detalle_avatar.configure(text="Avatar:")
        else:
            self.detalle_avatar.configure(text="Avatar: (Sin avatar)")

        if usuario.avatar:
            ruta = Path(usuario.avatar)
            if ruta.exists():
                try:
                    img = Image.open(ruta)
                    ctk_image = ctk.CTkImage(img, size=(120, 120))
                    self._image_refs["avatar"] = ctk_image
                    self.avatar_label.configure(image=ctk_image, text="")
                except:
                    self.avatar_label.configure(text="(Error cargando imagen)", image=None)
            else:
                self.avatar_label.configure(text="(Avatar no encontrado)", image=None)
        else:
            self.avatar_label.configure(text="(Sin avatar)", image=None)
