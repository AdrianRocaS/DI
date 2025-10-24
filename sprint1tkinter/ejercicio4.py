import tkinter as tk

#Mostrará como seleccionadas las opciones con el check activo
def actualizar():
    seleccion = []
    if var01.get(): seleccion.append("Leer")
    if var02.get(): seleccion.append("Deporte")
    if var03.get(): seleccion.append("Música")

    label01.config(text="Seleccionadas: " + ", ".join(seleccion))

#Creación de la ventana
root = tk.Tk()
root.title("Ejercicio 4: Checkbutton")
root.geometry("300x150")

#Definición de variables
var01 = tk.IntVar()
var02 = tk.IntVar()
var03 = tk.IntVar()

#Checks
check01 = tk.Checkbutton(root, text="Leer", variable=var01, command=actualizar)

check02 = tk.Checkbutton(root, text="Deporte", variable=var02, command=actualizar)

check03 = tk.Checkbutton(root, text="Música", variable=var03, command=actualizar)

#Etiqueta
label01 = tk.Label(root, text="Seleccionadas:")

#Ordena las opciones disponibles
check01.pack()
check02.pack()
check03.pack()
label01.pack()

#Ejecutar el bucle principal
root.mainloop()
