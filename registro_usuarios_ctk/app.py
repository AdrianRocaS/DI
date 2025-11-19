import customtkinter as ctk
from controller.app_controller import AppController

if __name__ == "__main__":
    # Configuramos la apariencia
    ctk.set_appearance_mode("System")   # "Light"/"Dark" permitido
    ctk.set_default_color_theme("blue") # “green” o “dark-blue” opcional

    app = ctk.CTk()
    app.title("Registro de Usuarios (CTk + MVC)")
    app.geometry("900x600")

    # Definimos el Controlador
    controller = AppController(app)

    # Inicia el bucle principal de la UI
    app.mainloop()