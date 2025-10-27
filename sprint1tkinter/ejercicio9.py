import tkinter as tk
from idlelib.mainmenu import menudefs
from tkinter import messagebox

def nueva_ventana():
    messagebox.showinfo("Ventana Nueva", "Esta es una ventana nueva")

def salir_aplicacion():
    root.quit()

#Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 9: Menu")
root.geometry("300x200")

#Crear la barra de menu
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

#Crear un submenu "Archivo"
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir", command=nueva_ventana)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir_aplicacion)

#Crear submenu "Ayuda"
def mostrar_ayuda():
    messagebox.showinfo("Acerca de", "Aplicacion de ayuda")

menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=mostrar_ayuda)

#Ejecutar el bucle principal
root.mainloop()