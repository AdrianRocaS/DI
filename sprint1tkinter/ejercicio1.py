import tkinter as tk

def cambiar_texto():
    label03.config(text="Nuevo texto")

root = tk.Tk()
root.title("Ejercicio 1: Label")
root.geometry("300x150")

label01 = tk.Label(root, text="Bienvenido a Tkinter")
label01.pack(pady=5)

label02 = tk.Label(root, text="Adrián Roca Santiago")
label02.pack(pady=5)

label03 = tk.Label(root, text="Texto original")
label03.pack(pady=5)


button01 = tk.Button(root, text="Cambiar texto", command=cambiar_texto)
button01.pack(pady=10)

label01.pack()
label02.pack()
label03.pack()
button01.pack()

root.mainloop()
