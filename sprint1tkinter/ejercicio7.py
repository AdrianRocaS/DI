import tkinter as tk


def valores_variables():
    #Variables (coordenadas)
    x1 = int(entry_x1.get())
    y1 = int(entry_y1.get())
    x2 = int(entry_x2.get())
    y2 = int(entry_x2.get())
    # Formas
    canvas.create_rectangle(x1, y1, x2, y2, fill="aquamarine")
    canvas.create_oval(x1, y1, x2, y2, fill="grey")

#Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio7: Canvas")


#Entradas
tk.Label(root, text="Valor de 'x1':").pack()
entry_x1 = tk.Entry(root)
entry_x1.pack()

tk.Label(root, text="Valor de 'y1':").pack()
entry_y1 = tk.Entry(root)
entry_y1.pack()

tk.Label(root, text="Valor de 'x2':").pack()
entry_x2 = tk.Entry(root)
entry_x2.pack()

tk.Label(root, text="Valor de 'y2':").pack()
entry_y2 = tk.Entry(root)
entry_y2.pack()

#Boton
tk.Button(root, text="Dibujar", command=valores_variables).pack(pady=10)

#Canvas
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

#Ejecutar el bucle principal
root.mainloop()