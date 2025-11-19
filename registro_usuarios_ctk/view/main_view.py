import customtkinter as ctk
import tkinter
from typing import Callable, List, TYPE_CHECKING
from PIL import Image

if TYPE_CHECKING:
    from model.usuario_model import Usuario


class MainView(ctk.CTkFrame):
    #Esta clase crea la interfaz gráfica

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.grid_rowconfigure(0, weight=0)  # Fila de controles no crece
        self.grid_rowconfigure(1, weight=1)  # Fila de contenido sí crece
        self.grid_columnconfigure(0, weight=1)  # El frame principal crece en ancho

        # Atributo para mantener la imagen cargada y evitar que sea eliminada por GC
        self._current_avatar = None

        self._crear_menu_bar()
        self._crear_barra_controles()
        self._crear_widgets_contenido()  # Contiene la lista y los detalles

    def _crear_menu_bar(self):

        # Crear barra de Archivo y Ayuda
        self.menubar = tkinter.Menu(self.master)
        self.master.config(menu=self.menubar)
        self.menu_archivo = tkinter.Menu(self.menubar, tearoff=0)
        self.menu_ayuda = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Archivo", menu=self.menu_archivo)
        self.menubar.add_cascade(label="Ayuda", menu=self.menu_ayuda)

    def _crear_barra_controles(self):
        # Crear barra de controles Buscar, Género, Eliminar, Añadir
        controles_frame = ctk.CTkFrame(self, fg_color="transparent")
        controles_frame.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        # Grid para las opciones de la barra de control
        controles_frame.grid_columnconfigure(0, weight=0)
        controles_frame.grid_columnconfigure(1, weight=1)
        controles_frame.grid_columnconfigure(2, weight=0)
        controles_frame.grid_columnconfigure(3, weight=0)
        controles_frame.grid_columnconfigure(4, weight=10)
        controles_frame.grid_columnconfigure(5, weight=0)
        controles_frame.grid_columnconfigure(6, weight=0)

        # Label Buscar
        ctk.CTkLabel(controles_frame, text="Buscar:").grid(row=0, column=0, padx=(0, 5), sticky="w")

        # Entry Buscar
        self.buscar_entry = ctk.CTkEntry(controles_frame, width=200)  # Añadimos un ancho mínimo
        self.buscar_entry.grid(row=0, column=1, padx=(0, 5), sticky="ew")

        # Label Género
        ctk.CTkLabel(controles_frame, text="Género:").grid(row=0, column=2, padx=(0, 5), sticky="w")

        # ComboBox Género
        self.genero_combobox = ctk.CTkComboBox(controles_frame,
                                               values=["todos", "Masculino", "Femenino", "Otro"],
                                               width=100,
                                               fg_color=("#3b8ed0"),
                                               button_color=("#36719f"))

        self.genero_combobox.set("todos")
        self.genero_combobox.grid(row=0, column=3, sticky="w")


        # 6. Botón Eliminar
        self.eliminar_button = ctk.CTkButton(controles_frame, text="Eliminar")
        self.eliminar_button.grid(row=0, column=5, padx=(0, 10), sticky="w")

        # 7. Botón Añadir
        self.add_user_button = ctk.CTkButton(controles_frame, text="Añadir")
        self.add_user_button.grid(row=0, column=6, sticky="w")

    def _crear_widgets_contenido(self):
        # Lista de usuarios y Detalles del usuario seleccionado
        contenido_frame = ctk.CTkFrame(self, fg_color="transparent")
        contenido_frame.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="nsew")

        # Configuración de las 2 columnas para el contenido:
        contenido_frame.grid_columnconfigure(0, weight=1)
        contenido_frame.grid_columnconfigure(1, weight=1)
        contenido_frame.grid_rowconfigure(0, weight=1)

        # --- LISTA DE USUARIOS (COLUMNA 0) ---
        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(contenido_frame)
        self.lista_usuarios_scrollable.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        self.lista_usuarios_scrollable.columnconfigure(0, weight=1)

        # Detalles del usuario
        detalles_frame = ctk.CTkFrame(contenido_frame)
        detalles_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
        detalles_frame.grid_columnconfigure(0, weight=1)

        # Etiqueta para el Avatar
        self.avatar_label = ctk.CTkLabel(detalles_frame, text="(avatar)")
        # sticky="n" mantiene arriba, pady superior para bajarlo un poco
        self.avatar_label.grid(row=0, column=0, pady=(20, 10), sticky="n")

        # Mostrar los datos
        self.nombre_label = ctk.CTkLabel(detalles_frame, text="Nombre: -", justify="left")
        self.nombre_label.grid(row=1, column=0, sticky="w", padx=20, pady=2)

        self.edad_label = ctk.CTkLabel(detalles_frame, text="Edad: -", justify="left")
        self.edad_label.grid(row=2, column=0, sticky="w", padx=20, pady=2)

        self.genero_label = ctk.CTkLabel(detalles_frame, text="Género: -", justify="left")
        self.genero_label.grid(row=3, column=0, sticky="w", padx=20, pady=2)

        # Peso para el espacio vacío para que los elementos se queden arriba
        detalles_frame.grid_rowconfigure(4, weight=1)

    def actualizar_lista_usuarios(self, usuarios: List['Usuario'], on_seleccionar_callback: Callable[[int], None]):

        # Limpiar widgets antiguos de la lista
        for widget in self.lista_usuarios_scrollable.winfo_children():
            widget.destroy()

        # Crear un botón por cada usuario
        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx),
                fg_color="transparent",
                text_color=("black", "white"),
                hover_color=("gray80", "gray20")
            )
            btn.grid(row=i, column=0, sticky="ew", padx=5, pady=2)

    def mostrar_detalles_usuario(self, usuario: 'Usuario', imagen: ctk.CTkImage = None):
        # Actualiza los label con la información del usuario seleccionado
        if usuario:
            self.nombre_label.configure(text=f"Nombre: {usuario.nombre}")
            self.edad_label.configure(text=f"Edad: {usuario.edad} años")
            self.genero_label.configure(text=f"Género: {usuario.genero}")

            # Imagen
            if imagen and isinstance(imagen, ctk.CTkImage):
                self._current_avatar = imagen
                self.avatar_label.configure(text="", image=imagen)
            else:
                self.avatar_label.configure(text="(avatar)", image=None)
                self._current_avatar = None
        else:
            # Estará sin completar al iniciar el programa
            self.nombre_label.configure(text="Nombre: -")
            self.edad_label.configure(text="Edad: -")
            self.genero_label.configure(text="Género: -")
            self.avatar_label.configure(text="(avatar)", image=None)
            self._current_avatar = None