import tkinter as tk

def mostrar_mensaje():
    label01.config(text="Mostrando mensaje")

root = tk.Tk()
root.title("Ejercicio 2: Button")
root.geometry("300x150")

label01 = tk.Label(root, text="")
label01.pack(pady=5)

button01 = tk.Button(root, text="Mostrar mensaje", command=mostrar_mensaje)
button01.pack(pady=10)

button02 = tk.Button(root, text="Salir", command=root.quit)
button02.pack(pady=15)

label01.pack()
button01.pack()
button02.pack()

root.mainloop()

