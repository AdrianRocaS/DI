import tkinter as tk

#Cambia el color de fondo dependiendo del color seleccionado
def cambiar_color():
    root.config(bg=var.get())

#Creación de la ventana
root = tk.Tk()
root.title("Ejercicio 5: Radiobutton")
root.geometry("300x150")

#Variable del color
var = tk.StringVar()

#Botones
tk.Radiobutton(root, text="Rojo", variable=var, value="red", command=cambiar_color).pack()

tk.Radiobutton(root, text="Verde", variable=var, value="green", command=cambiar_color).pack()

tk.Radiobutton(root, text="Azul", variable=var, value="blue", command=cambiar_color).pack()


#Ejecutar el bucle principal
root.mainloop()
