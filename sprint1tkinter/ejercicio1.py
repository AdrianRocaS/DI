import tkinter as tk

#Función para reemplazar el contenido de "Etiqueta 03"
def cambiar_texto():
    label03.config(text="Nuevo texto")

#Creación de la ventana
root = tk.Tk()
root.title("Ejercicio 1: Label")
root.geometry("300x150")

#Etiquetas
label01 = tk.Label(root, text="Bienvenido a Tkinter")
label01.pack(pady=5)

label02 = tk.Label(root, text="Adrián Roca Santiago")
label02.pack(pady=5)

label03 = tk.Label(root, text="Texto original")
label03.pack(pady=5)

#Activa la función
button01 = tk.Button(root, text="Cambiar texto", command=cambiar_texto)
button01.pack(pady=10)


#Ejecutar el bucle principal
root.mainloop()
