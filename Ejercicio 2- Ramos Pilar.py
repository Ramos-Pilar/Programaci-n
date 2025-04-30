import tkinter as tk

def main():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("700x700")
    ventana.configure(bg="lightblue")
    ventana.title("Ejercicio 2")

    label = tk.Label(ventana, text = "Ejercicio 2", font = ("Comic Sans MS", 16), bg=("lightblue"), fg=("black"))
    label.pack(pady=20)
    label = tk.Label(ventana, text = "Ramos Colonna María Pilar", font = ("Comic Sans MS", 14), bg=("lightblue"), fg=("black"))
    label.pack(pady=20)


if __name__=="__main__":
    main()
