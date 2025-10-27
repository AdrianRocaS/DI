import tkinter as tk

#Funcion para mostrar el texto escrito en la etiqueta cuando se pulse el boton
def mostrar_texto():
    texto = entry01.get()
    label01.config(text=f"Texto introducido: {texto}")

#Funcion para borrar el texto mostrado y el escrito en la etiqueta
def borrar_texto():
    entry01.delete(0, tk.END)
    label01.config(text="Introduce texto")

#Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 8: Frame")

#Frame superior
frame01 = tk.Frame(root, pady=10)
frame01.pack()

#Texto
tk.Label(frame01, text="Introduce algo:").grid(row=0, column=0)
#Entrada de texto
entry01 = tk.Entry(frame01)
entry01.grid(row=0, column=1)
#Etiqueta
label01 = tk.Label(frame01, text="Introduce texto")
label01.grid(row=1, column=0, columnspan=2)

#Frame inferior
frame02 = tk.Frame(root, pady=10)
frame02.pack()
root.geometry("300x150")

#Texto de los botones
tk.Button(frame02, text="Mostrar",command=mostrar_texto).grid(row=0, column=0, padx=5)
tk.Button(frame02, text="Borrar", command=borrar_texto).grid(row=0, column=1, padx=5)

#Ejecutar el bucle principal
root.mainloop()
