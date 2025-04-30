import tkinter as tk

def limpiarVentana():
    for widget in ventana.winfo_children():
        widget.destroy()

def volver():
    limpiarVentana()
    mostrarMenu()

def sumaDosNumeros():
    limpiarVentana()
    
    botonvolver = tk.Button(ventana, text = "Volver", font = ("Comic Sans MS", 14, "bold"), bg=("white"), fg=("green"), activebackground=("yellow"), width = 10, command=volver)
    botonvolver.pack(pady=20)
    
    label = tk.Label(ventana, text = "Suma", font = ("Comic Sans MS", 18), bg=("lightgreen"), fg=("green"))
    label.pack(pady = 10)

def restaDosNumeros():
    limpiarVentana()
    
    botonvolver = tk.Button(ventana, text = "Volver", font = ("Comic Sans MS", 14, "bold"), bg=("white"), fg=("green"), activebackground=("yellow"), width = 10, command=volver)
    botonvolver.pack(pady=20)
    
    label = tk.Label(ventana, text = "Resta", font = ("Comic Sans MS", 18), bg=("lightgreen"), fg=("green"))
    label.pack(pady = 10)


def multiplicacionDosNumeros():
    limpiarVentana()
    
    botonvolver = tk.Button(ventana, text = "Volver", font = ("Comic Sans MS", 14, "bold"), bg=("white"), fg=("green"), activebackground=("yellow"), width = 10, command=volver)
    botonvolver.pack(pady=20)
    
    label = tk.Label(ventana, text = "Multiplicar", font = ("Comic Sans MS", 18), bg=("lightgreen"), fg=("green"))
    label.pack(pady = 10) 


def dividirDosNumeros():
    limpiarVentana()
    
    botonvolver = tk.Button(ventana, text = "Volver", font = ("Comic Sans MS", 14, "bold"), bg=("white"), fg=("green"), activebackground=("yellow"), width = 10, command=volver)
    botonvolver.pack(pady=20)
    
    label = tk.Label(ventana, text = "Dividir", font = ("Comic Sans MS", 18), bg=("lightgreen"), fg=("green"))
    label.pack(pady = 10)

def mostrarMenu():
    limpiarVentana()
    
    label = tk.Label(ventana, text = "Menú Principal", font = ("Georgia", 18, "bold"), bg=("lightgreen"), fg=("green"))
    label.pack(pady = 20)

    boton1 = tk.Button(ventana, text = "Sumar", font = ("Comic Sans MS", 14), bg=("white"), fg=("green"), activebackground=("yellow"), relief=("raised"), width = 50, command=sumaDosNumeros)
    boton1.pack(pady=10)
    
    boton2 = tk.Button(ventana, text = "Restar", font = ("Comic Sans MS", 14), bg=("white"), fg=("green"), activebackground=("yellow"), relief=("raised"), width = 50, command=restaDosNumeros)
    boton2.pack(pady=10)
    
    boton3 = tk.Button(ventana, text = "Multiplicar", font = ("Comic Sans MS", 14), bg=("white"), fg=("green"), activebackground=("yellow"), relief=("raised"), width = 50, command=multiplicacionDosNumeros)
    boton3.pack(pady=10)
    
    boton4 = tk.Button(ventana, text = "Dividir", font = ("Comic Sans MS", 14), bg=("white"), fg=("green"), activebackground=("yellow"), relief=("raised"), width = 50, command=dividirDosNumeros)
    boton4.pack(pady=10)


def main():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("600x600")
    ventana.title("Ejercicio 5")
    ventana.configure(bg="lightgreen")
    mostrarMenu()
    ventana.mainloop()

if __name__=="__main__":
    main()
