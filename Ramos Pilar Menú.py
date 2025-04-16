import tkinter as tk


def graficarFuncion():
    limpiarVentana()
    label = tk.Label(ventana, text="¿De qué grado es la función?", font=("Arial",16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial",12), command=mostrarMenu)
    boton_volver.pack(pady=10)


def limpiarVentana():
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrarMenu():
    limpiarVentana()
    label = tk.Label(ventana, text = "Menú Principal", font = ("Georgia", 18, "bold"))
    label.pack(pady = 20)

    boton1 = tk.Button(ventana, text = "Graficar la función", font = ("Comic Sans MS", 14), bg=("yellow"), width = 50, command=graficarFuncion)
    boton1.pack(pady=10)
    
    boton2 = tk.Button(ventana, text = "Graficar puntos específicos sobre la función", font = ("Comic Sans MS", 14), bg=("yellow"), width = 50, command="accion")
    boton2.pack(pady=10)
    
    boton3 = tk.Button(ventana, text = "Encontrar raíces aproximadas de la función", font = ("Comic Sans MS", 14), bg=("yellow"), width = 50, command="accion")
    boton3.pack(pady=10)

    
def main():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("600x300")
    ventana.title("Menú Centrado")

    mostrarMenu()

    ventana.mainloop()


if __name__=="__main__":
    main()
