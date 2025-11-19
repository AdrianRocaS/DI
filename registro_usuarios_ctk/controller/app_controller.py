import customtkinter as ctk
from model.usuario_model import GestorUsuarios
from view.main_view import MainView
from pathlib import Path
from PIL import Image

# Enlaza el modelo y la vista
class AppController:

    def __init__(self, master):
        self.master = master
        self.model = GestorUsuarios()
        self.view = MainView(master)
        self.view.pack(fill="both", expand=True)  # Muestra la vista

        # Caché para mantener vivas las imágenes de los avatares
        self.avatar_images = {}

        # Rutas seguras
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"

        # Llamar a la lista al iniciar
        self.refrescar_lista_usuarios()

    def _cargar_avatar(self, filename: str) -> ctk.CTkImage | None:

        # Carga una imagen y la guarda o la recupera
        if filename in self.avatar_images:
            return self.avatar_images[filename]

        ruta_imagen = self.ASSETS_PATH / filename

        # En caso de no encontrar la imagen, muestra un mensaje
        if not ruta_imagen.exists():
            print(f"Advertencia: Archivo de avatar no encontrado en {ruta_imagen}")
            return None

        try:
            # Abrimos la imagen
            pil_image = Image.open(ruta_imagen)
            ctk_image = ctk.CTkImage(
                light_image=pil_image,
                dark_image=pil_image,
                size=(150, 150)
            )
            # Guardamos la imagen
            self.avatar_images[filename] = ctk_image
            return ctk_image
        except Exception as e:
            print(f"Error cargando imagen {filename}: {e}")
            return None

    def refrescar_lista_usuarios(self):

        usuarios = self.model.listar()
        self.view.actualizar_lista_usuarios(usuarios, self.seleccionar_usuario)

    def seleccionar_usuario(self, indice: int):

        # Selecciona el usuario indicado
        usuario_seleccionado = self.model.obtener_usuario_por_indice(indice)

        if usuario_seleccionado:
            # Carga la imagen de ese usuario
            avatar_image = self._cargar_avatar(usuario_seleccionado.avatar)

            # Muestra la información del usuario seleccionado y su avatar
            self.view.mostrar_detalles_usuario(usuario_seleccionado, avatar_image)
        else:
            # Elimina la información sobre el usuario en caso de que se seleccione uno inválido
            self.view.mostrar_detalles_usuario(None)