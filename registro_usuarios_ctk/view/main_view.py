import customtkinter as ctk
import tkinter
from pathlib import Path
from PIL import Image


class MainView:
    def __init__(self, master):
        self.master = master
        self.indice_seleccionado = None

        # CONFIGURACIÓN DEL GRID PRINCIPAL
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

        master.grid_rowconfigure(0, weight=0)
        master.grid_rowconfigure(1, weight=1)
        master.grid_rowconfigure(2, weight=0)

        # BARRA SUPERIOR
        self.frame_top = ctk.CTkFrame(master, corner_radius=0, fg_color="transparent")
        self.frame_top.grid(row=0, column=0, columnspan=2,
                            sticky="ew", padx=15, pady=(10, 0))

        self.frame_top.grid_columnconfigure(0, weight=1)
        self.frame_top.grid_columnconfigure(1, weight=0)
        self.frame_top.grid_columnconfigure(2, weight=0)
        self.frame_top.grid_columnconfigure(3, weight=0)
        self.frame_top.grid_columnconfigure(4, weight=0)

        # Buscar
        self.label_buscar = ctk.CTkLabel(self.frame_top, text="Buscar:")
        self.label_buscar.grid(row=0, column=0, sticky="w", padx=(5, 5))

        self.entry_buscar = ctk.CTkEntry(self.frame_top, width=230)
        self.entry_buscar.grid(row=0, column=0, sticky="w", padx=(70, 15))

        # Género
        self.label_genero = ctk.CTkLabel(self.frame_top, text="Género:")
        self.label_genero.grid(row=0, column=1, padx=(10, 5))

        self.option_genero = ctk.CTkOptionMenu(
            self.frame_top,
            values=["todos", "masculino", "femenino", "otro"]
        )
        self.option_genero.set("todos")
        self.option_genero.grid(row=0, column=2, padx=(0, 15))

        # Botón Eliminar
        self.boton_eliminar = ctk.CTkButton(self.frame_top, text="Eliminar", width=100)
        self.boton_eliminar.grid(row=0, column=3, padx=(0, 10))
        # Botón Añadir
        self.boton_añadir = ctk.CTkButton(self.frame_top, text="Añadir", width=100)
        self.boton_añadir.grid(row=0, column=4, padx=(0, 5))

        # PANEL IZQUIERDO (Usuarios)
        self.frame_left = ctk.CTkFrame(master, corner_radius=10)
        self.frame_left.grid(row=1, column=0, sticky="nsew", padx=15, pady=15)

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
        self.frame_right.grid(row=1, column=1, sticky="nsew", padx=15, pady=15)

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

        # PANEL INFERIOR
        self.frame_bottom = ctk.CTkFrame(master, corner_radius=10)
        self.frame_bottom.grid(row=2, column=0, columnspan=2, sticky="ew",
                               padx=15, pady=(0, 15))

        self.frame_bottom.grid_columnconfigure(0, weight=0)
        self.frame_bottom.grid_columnconfigure(1, weight=1)
        self.frame_bottom.grid_columnconfigure(2, weight=0)

        # Botón autoguardado
        self.boton_autoguardar = ctk.CTkButton(
            self.frame_bottom,
            text="Auto-guardar (10s): OFF",
            width=180
        )
        self.boton_autoguardar.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Contador
        self.label_contador = ctk.CTkLabel(self.frame_bottom, text="0 usuarios visibles.")
        self.label_contador.grid(row=0, column=1, pady=10)

        # Botón Salir
        self.boton_salir = ctk.CTkButton(self.frame_bottom, text="Salir",
                                         width=100, command=master.destroy)
        self.boton_salir.grid(row=0, column=2, padx=20, pady=10, sticky="e")


        # MENÚ SUPERIOR
        self.menubar = tkinter.Menu(master)
        master.config(menu=self.menubar)
        self.menu_archivo = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Archivo", menu=self.menu_archivo)
        # Opciones FASE 3
        self.menu_archivo.add_command(label="Cargar")
        self.menu_archivo.add_command(label="Guardar")
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=master.destroy)

    # Actualización de la lista
    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback,
                                  on_doble_click_callback=None):

        # Primero desactivar comandos antiguos
        for child in self.lista_scroll.winfo_children():
            try:
                child.configure(command=lambda: None)
            except Exception:
                pass
        # Luego destruirlos
        for child in self.lista_scroll.winfo_children():
            child.destroy()

        #Crear botones nuevos
        for i, usuario in enumerate(usuarios):
            texto = f"{usuario.nombre} — {usuario.edad} — {usuario.genero}"

            boton = ctk.CTkButton(
                self.lista_scroll,
                text=texto,
                anchor="w",
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            boton.pack(fill="x", pady=3, padx=5)

            # Doble clic para editar (si está disponible)
            if on_doble_click_callback:
                boton.bind("<Double-Button-1>",
                           lambda e, idx=i: on_doble_click_callback(idx))
    # Mostrar detalles
    def mostrar_detalles_usuario(self, usuario):

        # Destruir y recrear el label del avatar para evitar estados raros
        try:
            self.avatar_label.destroy()
        except Exception:
            pass

        self.avatar_label = ctk.CTkLabel(self.frame_right, text="", image=None)
        self.avatar_label.pack(padx=20, pady=10, anchor="nw")
        self._image_refs.clear()

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
                    ctk_image = ctk.CTkImage(light_image=img, dark_image=img, size=(120, 120))
                    self._image_refs["avatar"] = ctk_image
                    self.avatar_label.configure(image=ctk_image, text="")
                except:
                    self.avatar_label.configure(text="(Error cargando imagen)", image=None)
            else:
                self.avatar_label.configure(text="(Avatar no encontrado)", image=None)
        else:
            self.avatar_label.configure(text="(Sin avatar)", image=None)

    # FASE 4
    def actualizar_contador(self, n):
        if n == 1:
            txt = "1 usuario visible."
        else:
            txt = f"{n} usuarios visibles."
        self.label_contador.configure(text=txt)

    def actualizar_estado_autoguardado(self, on: bool):
        texto = "Auto-guardar (10s): ON" if on else "Auto-guardar (10s): OFF"
        self.boton_autoguardar.configure(text=texto)