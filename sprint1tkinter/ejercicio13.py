import tkinter as tk

#Funcion para dibujar un circulo donde el usuario hace clic
def dibujar_circulo(event):
    x, y = event.x, event.y
    radio = 20  #Tamaño del circulo
    canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="blue") #Crea el circulo en la ubicacion indicada

#Funcion para limpiar el canvas si se presiona la tecla "c"
def limpiar_canvas(event):
    if event.char == "c":
        canvas.delete("all")

#Creamos la ventana principal
root = tk.Tk()
root.title("Ejercicio 13: Eventos de teclado y ratón")
root.geometry("500x400")

#Canvas
canvas = tk.Canvas(root, bg="white", width=500, height=500)
canvas.pack(fill="both", expand=True)

#Asociar eventos
canvas.bind("<Button-1>", dibujar_circulo) #"Button-1" es el codigo que representa al click izquierdo del raton
root.bind("<Key>", limpiar_canvas) #Key indica cualquier tecla, asi que todas las teclas hacen que se ejecute la funcion "limpiar_canvas"

#Indicamos que recibirá instrucciones del teclado
canvas.focus_set()


root.mainloop()