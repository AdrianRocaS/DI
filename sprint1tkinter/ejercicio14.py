import tkinter as tk
from tkinter import messagebox


class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 12: Aplicación de Registro de Usuarios")
        self.root.geometry("800x600")

        # Lista interna de usuarios
        self.usuarios = []

        # Crear la barra de menu
        menu_principal = tk.Menu(root)
        root.config(menu=menu_principal)

        # Crear un submenu "Archivo"
        menu_archivo = tk.Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Guardar Lista", command=self.guardar_lista)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Cargar Lista", command=self.cargar_lista)
        menu_archivo.add_separator()



        # Entrada de texto para el nombre
        tk.Label(self.root, text="Nombre de Usuario:").pack()
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.pack(pady=10)

        # Crear el Scale
        tk.Label(self.root, text="Edad:").pack()
        self.scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
        self.scale_edad.pack(pady=10)

        # Botones de opción (Radiobutton) para seleccionar el género
        tk.Label(self.root, text="Género:").pack()
        self.genero_var = tk.StringVar(value="Pendiente")
        tk.Radiobutton(self.root, text="Masculino", variable=self.genero_var, value="Masculino").pack()
        tk.Radiobutton(self.root, text="Femenino", variable=self.genero_var, value="Femenino").pack()
        tk.Radiobutton(self.root, text="Otro", variable=self.genero_var, value="Otro").pack()

        # Lista de elementos
        self.listbox = tk.Listbox(self.root, height=10, width=50)
        self.listbox.pack(pady=10)

        # Barra de desplazamiento
        self.scrollbar = tk.Scrollbar(self.root, command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Botones
        tk.Button(self.root, text="Agregar Usuario", command=self.añadir_usuario).pack(pady=5)
        tk.Button(self.root, text="Eliminar Usuario", command=self.eliminar_usuario).pack(pady=5)
        tk.Button(self.root, text="Salir", command=self.salir).pack(pady=5)

    def añadir_usuario(self):
        nombre = self.entry_nombre.get()
        edad = self.scale_edad.get()
        genero = self.genero_var.get()
        if nombre:
            self.listbox.insert(tk.END, f"{nombre} - {edad} - {genero}")
            self.entry_nombre.delete(0, tk.END)

    def eliminar_usuario(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            self.listbox.delete(seleccion)


    #Funciones para mostrar los messagebox
    def guardar_lista(self):
        messagebox.showinfo("Guardar Lista", "Se han guardado los cambios")

    def cargar_lista(self):
        messagebox.showinfo("Cargar Lista", "Lista cargada")

    #Funcion de "Salir"
    def salir(self):
        root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()
