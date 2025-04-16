import tkinter as tk

def limpiarVentana():
    for widget in ventana.winfo_children():
        widget.destroy()

def sumaDosNumeros():
    limpiarVentana()
    
    label = tk.Label(ventana, text = "Ingrese el primer número", font = ("Comic Sans MS", 18))
    label.pack(pady = 20)
    campo1 = tk.Entry(ventana)
    campo1.pack(pady=10)
    
    #No pasa float a int :( triste moriré ayuda
    
    num1=float(campo1.get())
    
    
    
    label = tk.Label(ventana, text = "Ingrese el segundo número", font = ("Comic Sans MS", 18))
    label.pack(pady = 20)
    campo2 = tk.Entry(ventana)
    campo2.pack(pady=10)
    num2=float(campo2.get())

    def suma(num1,num2):
        suma=num1+num2
        label = tk.Label(ventana, text = suma, font = ("Comic Sans MS", 18, "bold"))
        label.pack(pady = 20)
        

    botonsuma = tk.Button(ventana, text = "Sumar", font = ("Comic Sans MS", 14, "bold"), bg=("white"), width = 50, command=suma)
    botonsuma.pack(pady=10)


def mostrarMenu():
    limpiarVentana()
    
    label = tk.Label(ventana, text = "Menú Principal", font = ("Georgia", 18, "bold"))
    label.pack(pady = 20)

    boton1 = tk.Button(ventana, text = "Sumar", font = ("Comic Sans MS", 14), bg=("white"), width = 50, command=sumaDosNumeros)
    boton1.pack(pady=10)
    
    boton2 = tk.Button(ventana, text = "Restar", font = ("Comic Sans MS", 14), bg=("white"), width = 50, command="accion")
    boton2.pack(pady=10)
    
    boton3 = tk.Button(ventana, text = "Multiplicar", font = ("Comic Sans MS", 14), bg=("white"), width = 50, command="accion")
    boton3.pack(pady=10)
    
    boton4 = tk.Button(ventana, text = "Dividir", font = ("Comic Sans MS", 14), bg=("white"), width = 50, command="accion")
    boton4.pack(pady=10)

        

def main():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("600x600")
    mostrarMenu()
    ventana.mainloop()

if __name__=="__main__":
    main()
