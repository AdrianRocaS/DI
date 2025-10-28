import tkinter as tk

def actualizar_valor(valor):
    etiqueta.config(text=f"Valor seleccionado: {valor}")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 11: Scale")
root.geometry("300x200")

# Crear el Scale
barra = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar_valor)
barra.pack(pady=20)

# Etiqueta para mostrar el valor seleccionado
etiqueta = tk.Label(root, text="Valor: 0", font=("Arial", 12))
etiqueta.pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()
