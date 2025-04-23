import tkinter as tk

def limpiarVentana():
    for widget in ventana.winfo_children():
        widget.destroy()

def sumaDosNumeros():
    limpiarVentana()
    
    label = tk.Label(ventana, text = "Ingrese el primer número", font = ("Comic Sans MS", 18), bg=("lightgreen"), fg=("green"))
    label.pack(pady = 20)
    campo1 = tk.Entry(ventana)
    campo1.pack(pady = 10)
    num1=float(campo1.get())
    #Sigo sin poder pasar string a float
    
    campo1.bind("<Return>", lambda event: campo2.focus_set())
    
    
    label = tk.Label(ventana, text = "Ingrese el segundo número", font = ("Comic Sans MS", 18), bg=("lightgreen"), fg=("green"))
    label.pack(pady = 20)
    campo2 = tk.Entry(ventana)
    campo2.pack(pady = 10)

    def suma():
        res=num1+num2

    botonsuma = tk.Button(ventana, text = "Sumar", font = ("Comic Sans MS", 14, "bold"), bg=("white"), fg=("green"), activebackground=("yellow"), width = 20, command=suma)
    botonsuma.pack(pady=10)


def mostrarMenu():
    limpiarVentana()
    
    label = tk.Label(ventana, text = "Menú Principal", font = ("Georgia", 18, "bold"), bg=("lightgreen"), fg=("green"))
    label.pack(pady = 20)

    boton1 = tk.Button(ventana, text = "Sumar", font = ("Comic Sans MS", 14), bg=("white"), fg=("green"), activebackground=("yellow"), relief=("raised"), width = 50, command=sumaDosNumeros)
    boton1.pack(pady=10)
    
    boton2 = tk.Button(ventana, text = "Restar", font = ("Comic Sans MS", 14), bg=("white"), fg=("green"), activebackground=("yellow"), relief=("raised"), width = 50, command="accion")
    boton2.pack(pady=10)
    
    boton3 = tk.Button(ventana, text = "Multiplicar", font = ("Comic Sans MS", 14), bg=("white"), fg=("green"), activebackground=("yellow"), relief=("raised"), width = 50, command="accion")
    boton3.pack(pady=10)
    
    boton4 = tk.Button(ventana, text = "Dividir", font = ("Comic Sans MS", 14), bg=("white"), fg=("green"), activebackground=("yellow"), relief=("raised"), width = 50, command="accion")
    boton4.pack(pady=10)

        

def main():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("600x600")
    ventana.configure(bg="lightgreen")
    mostrarMenu()
    ventana.mainloop()

if __name__=="__main__":
    main()
