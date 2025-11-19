from model.usuario_model import GestorUsuarios
from view.main_view import MainView
from view.add_user_modal import AddUserModal
from model.usuario_model import Usuario
from tkinter import messagebox
from pathlib import Path

class AppController:
    def __init__(self, master):
        self.master = master
        # Modelo
        self.gestor = GestorUsuarios()
        # Vista
        self.view = MainView(master)

        # Estado de FASE 4
        self.usuarios_visibles = []  # lista de (indice_real, usuario)
        self.indice_seleccionado_real = None
        self.auto_guardado_on = False
        self.autoguardado_interval_ms = 10000

        self.view.boton_añadir.configure(command=self.abrir_ventana_nuevo_usuario)
        self.view.boton_eliminar.configure(command=self.eliminar_usuario)
        self.view.boton_autoguardar.configure(command=self.toggle_autoguardado)

        self.view.menu_archivo.entryconfig("Cargar", command=self.cargar_usuarios)
        self.view.menu_archivo.entryconfig("Guardar", command=self.guardar_usuarios)
        self.view.menu_archivo.entryconfig("Salir", command=master.destroy)

        # Filtros
        self.view.entry_buscar.bind("<KeyRelease>", lambda e: self.aplicar_filtros())
        self.view.option_genero.configure(command=lambda _value: self.aplicar_filtros())

        # Carga los datos automáticamente de 'usuarios.csv'
        if Path("usuarios.csv").exists():
            self.cargar_usuarios(silencioso=True)

        # Conectar la vista con los callbacks del controlador
        self.refrescar_lista_usuarios()

        # Programar auto-guardado
        self.programar_autoguardado()


    def refrescar_lista_usuarios(self):
        self.aplicar_filtros()

    def aplicar_filtros(self):
        texto = self.view.entry_buscar.get().strip().lower()
        genero_filtro = self.view.option_genero.get().lower()
        self.usuarios_visibles = []
        for idx_real, usuario in enumerate(self.gestor.listar()):
            # Filtro por texto (nombre)
            if texto and texto not in usuario.nombre.lower():
                continue
            # Filtro por género
            if genero_filtro != "todos" and usuario.genero.lower() != genero_filtro:
                continue

            self.usuarios_visibles.append((idx_real, usuario))

        solo_usuarios = [u for _, u in self.usuarios_visibles]

        self.view.actualizar_lista_usuarios(
            solo_usuarios,
            on_seleccionar_callback=self.seleccionar_usuario,
            on_doble_click_callback=self.editar_usuario
        )
        self.view.actualizar_contador(len(self.usuarios_visibles))

    def seleccionar_usuario(self, indice_visible: int):
        if indice_visible < 0 or indice_visible >= len(self.usuarios_visibles):
            return

        idx_real, usuario = self.usuarios_visibles[indice_visible]

        # Más seguridad
        if idx_real >= len(self.gestor.listar()):
            return

        self.indice_seleccionado_real = idx_real
        self.view.mostrar_detalles_usuario(usuario)
    # FASE 2
    def abrir_ventana_nuevo_usuario(self):
        AddUserModal(self.master, self.guardar_nuevo_usuario)

    def guardar_nuevo_usuario(self, nombre, edad, genero, avatar):
        nuevo = Usuario(nombre, edad, genero, avatar)
        self.gestor.añadir(nuevo)
        self.refrescar_lista_usuarios()

    def editar_usuario(self, indice_visible: int):
        if not self.usuarios_visibles:
            return

        idx_real, usuario = self.usuarios_visibles[indice_visible]
        self.indice_seleccionado_real = idx_real

        def callback_guardar(nombre, edad, genero, avatar, indice=idx_real):
            self.guardar_usuario_editado(indice, nombre, edad, genero, avatar)

        AddUserModal(self.master, callback_guardar, usuario=usuario)

    def guardar_usuario_editado(self, indice_real, nombre, edad, genero, avatar):
        usuario_nuevo = Usuario(nombre, edad, genero, avatar)
        self.gestor.actualizar(indice_real, usuario_nuevo)
        self.refrescar_lista_usuarios()
        self.view.mostrar_detalles_usuario(usuario_nuevo)

    def eliminar_usuario(self):
        # Si no hay usuario seleccionado → error controlado
        if self.indice_seleccionado_real is None:
            messagebox.showwarning("Eliminar", "Selecciona un usuario primero.")
            return

        usuario = self.gestor.obtener_por_indice(self.indice_seleccionado_real)
        if usuario is None:
            messagebox.showwarning("Eliminar", "Usuario no válido.")
            return

        # Confirmación
        if not messagebox.askyesno("Eliminar", f"¿Eliminar a {usuario.nombre}?"):
            return

        # Eliminar del modelo
        self.gestor.eliminar(self.indice_seleccionado_real)

        # Resetear selección
        self.indice_seleccionado_real = None

        # Actualizar vista
        self.refrescar_lista_usuarios()
        self.view.mostrar_detalles_usuario(None)
    # FASE 3
    def guardar_usuarios(self, silencioso=False):
        try:
            ruta = Path("usuarios.csv")
            self.gestor.guardar_csv(ruta)
            if not silencioso:
                messagebox.showinfo("Guardar", "Usuarios guardados correctamente.")
        except Exception as e:
            if not silencioso:
                messagebox.showerror("Error", f"No se pudo guardar:\n{e}")

    def cargar_usuarios(self, silencioso=False):
        try:
            ruta = Path("usuarios.csv")
            self.gestor.cargar_csv(ruta)
            self.refrescar_lista_usuarios()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar:\n{e}")
        if not silencioso:
            messagebox.showinfo("Cargar", "Usuarios cargados correctamente.")

    # FASE 4 (AUTOGUARDADO)
    def toggle_autoguardado(self):
        self.auto_guardado_on = not self.auto_guardado_on
        self.view.actualizar_estado_autoguardado(self.auto_guardado_on)

    def programar_autoguardado(self):
        self.master.after(self.autoguardado_interval_ms, self.autoguardar_tick)

    def autoguardar_tick(self):
        if self.auto_guardado_on:
            self.guardar_usuarios(silencioso=True)
        self.programar_autoguardado()