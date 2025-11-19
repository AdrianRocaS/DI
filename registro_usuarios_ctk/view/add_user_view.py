# view/add_user_view.py
import customtkinter as ctk
from pathlib import Path


class AddUserView:

    def __init__(self, master):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.resizable(False, False)
        self.window.grab_set()

        # Variables de control para los RadioButtons
        self.genero_var = ctk.StringVar(value="Otro")
        self.avatar_var = ctk.StringVar(value="avatar3.png")

        self._crear_widgets()

        # Centrar la ventana
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = master.winfo_x() + (master.winfo_width() // 2) - (width // 2)
        y = master.winfo_y() + (master.winfo_height() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')

        self.window.transient(master)
        self.window.lift()

    def _crear_widgets(self):
        frame = ctk.CTkFrame(self.window)
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        frame.grid_columnconfigure(0, weight=1)  # Usamos una sola columna ancha

        row_idx = 0

        # Nombre
        ctk.CTkLabel(frame, text="Nombre:", anchor="w").grid(row=row_idx, column=0, padx=10, pady=(10, 2), sticky="w")
        row_idx += 1
        self.nombre_entry = ctk.CTkEntry(frame)
        self.nombre_entry.grid(row=row_idx, column=0, padx=10, pady=(0, 10),
                               sticky="ew")  # sticky="ew" para que sea ancho
        row_idx += 1

        # Edad
        ctk.CTkLabel(frame, text="Edad:", anchor="w").grid(row=row_idx, column=0, padx=10, pady=(2, 2), sticky="w")
        row_idx += 1
        self.edad_entry = ctk.CTkEntry(frame)
        self.edad_entry.grid(row=row_idx, column=0, padx=10, pady=(0, 10),
                             sticky="ew")  # sticky="ew" para que sea ancho
        row_idx += 1

        # Género (RadioButtons)
        ctk.CTkLabel(frame, text="Género:", font=ctk.CTkFont(weight="bold"), anchor="w").grid(row=row_idx, column=0,
                                                                                              padx=10, pady=(10, 5),
                                                                                              sticky="w")
        row_idx += 1

        # Botones de Género
        ctk.CTkRadioButton(frame, text="Masculino", variable=self.genero_var, value="Masculino").grid(row=row_idx,
                                                                                                      column=0, padx=20,
                                                                                                      pady=2,
                                                                                                      sticky="w")
        row_idx += 1
        ctk.CTkRadioButton(frame, text="Femenino", variable=self.genero_var, value="Femenino").grid(row=row_idx,
                                                                                                    column=0, padx=20,
                                                                                                    pady=2, sticky="w")
        row_idx += 1
        ctk.CTkRadioButton(frame, text="Otro", variable=self.genero_var, value="Otro").grid(row=row_idx, column=0,
                                                                                            padx=20, pady=2, sticky="w")
        row_idx += 1

        # --- Separador Visual ---
        ctk.CTkFrame(frame, height=1, fg_color="gray").grid(row=row_idx, column=0, padx=10, pady=(10, 10), sticky="ew")
        row_idx += 1

        # Avatar (RadioButtons)
        ctk.CTkLabel(frame, text="Avatar:", font=ctk.CTkFont(weight="bold"), anchor="w").grid(row=row_idx, column=0,
                                                                                              padx=10, pady=(0, 5),
                                                                                              sticky="w")
        row_idx += 1

        # Botones de Avatar
        self.avatar_options = [
            ("Avatar 1", "avatar1.png"),
            ("Avatar 2", "avatar2.png"),
            ("Avatar 3", "avatar3.png")
        ]

        for text, filename in self.avatar_options:
            # Usamos un value de ejemplo para el archivo
            ctk.CTkRadioButton(frame, text=text, variable=self.avatar_var, value=filename).grid(row=row_idx, column=0,
                                                                                                padx=20, pady=2,
                                                                                                sticky="w")
            row_idx += 1

        # Mensaje de Error
        self.error_label = ctk.CTkLabel(frame, text="", text_color="red")
        self.error_label.grid(row=row_idx, column=0, padx=10, pady=(10, 5), sticky="ew")
        row_idx += 1

        # Fila de los botones de acción
        frame.grid_rowconfigure(row_idx, weight=1)  # Empuja los botones hacia abajo

        # Botones Guardar/Cancelar (alineados a la derecha)
        btn_frame = ctk.CTkFrame(frame, fg_color="transparent")
        btn_frame.grid(row=row_idx, column=0, padx=10, pady=(10, 0), sticky="se")

        self.cancelar_button = ctk.CTkButton(btn_frame, text="Cancelar", fg_color="gray", command=self.window.destroy)
        self.cancelar_button.pack(side="left", padx=(0, 10))

        self.guardar_button = ctk.CTkButton(btn_frame, text="Guardar")
        self.guardar_button.pack(side="left")

    def get_data(self) -> dict:
        return {
            'nombre': self.nombre_entry.get().strip(),
            'edad': self.edad_entry.get().strip(),
            'genero': self.genero_var.get(),
            'avatar': self.avatar_var.get()
        }