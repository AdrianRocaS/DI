import customtkinter as ctk
from tkinter import messagebox


class AddUserModal(ctk.CTkToplevel):
    def __init__(self, master, on_save_callback):
        super().__init__(master)
        self.title("Añadir Nuevo Usuario")
        self.geometry("350x480")
        self.resizable(False, False)

        # Modal real
        self.grab_set()

        self.on_save_callback = on_save_callback

        # Variables
        self.var_nombre = ctk.StringVar()
        self.var_edad = ctk.StringVar()
        self.var_genero = ctk.StringVar(value="Otro")
        self.var_avatar = ctk.StringVar(value="avatar1.png")

        # NOMBRE
        ctk.CTkLabel(self, text="Nombre:").pack(pady=(15, 2))
        self.entry_nombre = ctk.CTkEntry(self, textvariable=self.var_nombre, width=250)
        self.entry_nombre.pack(pady=(0, 10))

        # EDAD
        ctk.CTkLabel(self, text="Edad:").pack(pady=(5, 2))
        self.entry_edad = ctk.CTkEntry(self, textvariable=self.var_edad, width=250)
        self.entry_edad.pack(pady=(0, 10))

        # GÉNERO
        ctk.CTkLabel(self, text="Género:").pack(pady=(5, 2))

        frame_genero = ctk.CTkFrame(self, fg_color="transparent")
        frame_genero.pack(pady=(0, 10))

        ctk.CTkRadioButton(frame_genero, text="Masculino",
                           variable=self.var_genero, value="Masculino").pack(anchor="w")
        ctk.CTkRadioButton(frame_genero, text="Femenino",
                           variable=self.var_genero, value="Femenino").pack(anchor="w")
        ctk.CTkRadioButton(frame_genero, text="Otro",
                           variable=self.var_genero, value="Otro").pack(anchor="w")

        # AVATAR
        ctk.CTkLabel(self, text="Avatar:").pack(pady=(10, 2))

        frame_avatar = ctk.CTkFrame(self, fg_color="transparent")
        frame_avatar.pack(pady=(0, 20))

        ctk.CTkRadioButton(frame_avatar, text="Avatar 1",
                           variable=self.var_avatar, value="assets/avatar1.png").pack(anchor="w")
        ctk.CTkRadioButton(frame_avatar, text="Avatar 2",
                           variable=self.var_avatar, value="assets/avatar2.png").pack(anchor="w")
        ctk.CTkRadioButton(frame_avatar, text="Avatar 3",
                           variable=self.var_avatar, value="assets/avatar3.png").pack(anchor="w")

        # BOTÓN GUARDAR
        self.btn_guardar = ctk.CTkButton(self, text="Guardar", width=200,
                                         command=self.guardar_usuario)
        self.btn_guardar.pack(pady=(10, 5))

        # BOTÓN CANCELAR
        self.btn_cancelar = ctk.CTkButton(self, text="Cancelar", width=200,
                                          fg_color="#555", hover_color="#666",
                                          command=self.destroy)
        self.btn_cancelar.pack(pady=(0, 15))

        self.center_modal()

    def center_modal(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (w // 2)
        y = (self.master.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    # VALIDACIONES Y GUARDADO
    def guardar_usuario(self):
        nombre = self.var_nombre.get().strip()
        edad = self.var_edad.get().strip()
        genero = self.var_genero.get()
        avatar = self.var_avatar.get()

        if not nombre:
            messagebox.showerror("Error", "El nombre es obligatorio.")
            return

        if not edad.isdigit() or int(edad) <= 0:
            messagebox.showerror("Error", "La edad debe ser un número mayor que 0.")
            return

        # Crear usuario
        self.on_save_callback(nombre, int(edad), genero, avatar)

        self.destroy()
