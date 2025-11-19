from model.usuario_model import GestorUsuarios
from view.main_view import MainView
from view.add_user_modal import AddUserModal
from model.usuario_model import Usuario

class AppController:
    def __init__(self, master):
        self.master = master
        # Modelo
        self.gestor = GestorUsuarios()
        # Vista
        self.view = MainView(master)
        self.view.boton_añadir.configure(command=self.abrir_ventana_nuevo_usuario)

        # Conectar la vista con los callbacks del controlador
        self.refrescar_lista_usuarios()


    def refrescar_lista_usuarios(self):
        usuarios = self.gestor.listar()
        # pasamos la función seleccionar_usuario como callback
        self.view.actualizar_lista_usuarios(usuarios, self.seleccionar_usuario)


    def seleccionar_usuario(self, indice: int):
        usuario = self.gestor.obtener_por_indice(indice)
        self.view.mostrar_detalles_usuario(usuario)

    # FASE 2
    def abrir_ventana_nuevo_usuario(self):
        AddUserModal(self.master, self.guardar_nuevo_usuario)

    def guardar_nuevo_usuario(self, nombre, edad, genero, avatar):
        nuevo = Usuario(nombre, edad, genero, avatar)
        self.gestor.añadir(nuevo)
        self.refrescar_lista_usuarios()