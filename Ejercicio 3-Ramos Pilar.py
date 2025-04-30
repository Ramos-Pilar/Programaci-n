import tkinter as tk



def main():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("500x400")
    ventana.configure(bg="lightblue")
    ventana.title("Ejercicio 3")

    label = tk.Label(ventana, text = "Ingresa tu nombre", font = ("Comic Sans MS", 14), bg=("lightblue"), fg=("black"))
    label.pack(pady=20)
    campo1 = tk.Entry(ventana)
    campo1.pack(pady = 10)

    def saludar():
        nombre=str(campo1.get())
        label = tk.Label(ventana, text = (f"¡Hola, ",[nombre],"! Te saluda Pilar Ramos"), font = ("Comic Sans MS", 14), bg=("lightblue"), fg=("black"))
        label.pack(pady=20)
    
    boton = tk.Button(ventana, text = "Saludar", font = ("Comic Sans MS", 14, "bold"), bg=("white"), fg=("green"), activebackground=("yellow"), width = 20, command=saludar)
    boton.pack(pady=10)

    


if __name__=="__main__":
    main()
