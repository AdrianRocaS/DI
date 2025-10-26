import tkinter as tk

#Imprime el nombre de la fruta seleccionada
def mostrar_fruta():
    seleccion = list.curselection()
    if seleccion:
        fruta = list.get(seleccion)
        label01.config(text=f"Fruta seleccionada: {fruta}")

#Creación de la ventana
root = tk.Tk()
root.title("Ejercicio 6: Listbox")
root.geometry("300x300")

#Lista de frutas
list = tk.Listbox(root)
for fruta in ["Manzana", "Banana", "Naranja"]:
    list.insert(tk.END, fruta)

#Boton
button01 = tk.Button(root, text="Mostrar fruta", command=mostrar_fruta)

#Etiqueta
label01 = tk.Label(root, text="")

#Ejecutar el bucle principal
list.pack()
button01.pack()
label01.pack()

root.mainloop()
