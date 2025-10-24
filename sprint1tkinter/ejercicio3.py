import tkinter as tk

def saludar():
    name01 = entry01.get()
    label01.config(text=f"Hola, {name01}")

root = tk.Tk()
root.title("Ejercicio 3: Entry")
root.geometry("300x150")

entry01 = tk.Entry(root)
entry01.pack(pady=20)

button01 = tk.Button(root, text="Saludar", command=saludar)
button01.pack(pady=5)

label01 = tk.Label(root, text="")
label01.pack(pady=5)

entry01.pack()
button01.pack()
label01.pack()

root.mainloop()
