import tkinter as tk

#Devolverá un saludo al nombre indicado después de pulsar el botón
def saludar():
    name01 = entry01.get()
    label01.config(text=f"Hola, {name01}")

#Creación de la ventana
root = tk.Tk()
root.title("Ejercicio 3: Entry")
root.geometry("300x150")

#Entrada
entry01 = tk.Entry(root)
entry01.pack(pady=20)

#Botón
button01 = tk.Button(root, text="Saludar", command=saludar)
button01.pack(pady=5)

#Etiqueta
label01 = tk.Label(root, text="")
label01.pack(pady=5)


#Ejecutar el bucle principal
root.mainloop()
