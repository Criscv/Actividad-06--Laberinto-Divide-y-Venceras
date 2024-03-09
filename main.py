import mapa as m
from tkinter import Tk, Canvas, mainloop
from tkinter import messagebox
import utilidades as d


def mostrarMapaTkinter(mapaJuego, pasos):
    root = Tk()
    canvas = Canvas(root, width=600, height=600)
    canvas.pack()
    root.geometry("1200x600")  # Establecer el tamaño de la ventana principal

    # Canvas para el mapa original
    canvas_original = Canvas(root, width=600, height=600)
    canvas_original.pack(side="left")

    # Canvas para el mapa con el recorrido
    canvas_recorrido = Canvas(root, width=600, height=600)
    canvas_recorrido.pack(side="right")
    
    for i in range(mapaJuego._tamanio):
        for j in range(mapaJuego._tamanio):
            x1, y1 = j * 30, i * 30
            x2, y2 = x1 + 30, y1 + 30
            if [i, j] in pasos:
                canvas.create_rectangle(x1, y1, x2, y2, fill="pink")
            elif mapaJuego._mapa[i][j] == 0:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            elif mapaJuego._mapa[i][j] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            elif mapaJuego._mapa[i][j] == 2:
                canvas.create_rectangle(x1, y1, x2, y2, fill="green")
            elif mapaJuego._mapa[i][j] == 3:
                canvas.create_rectangle(x1, y1, x2, y2, fill="red")
            elif mapaJuego._mapa[i][j] == 4:
                canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            elif mapaJuego._mapa[i][j] == 8:
                canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")

    root.mainloop()

if __name__ == "__main__":
    mapa = m.MapaJuego(10)
    mapa.dibujarMapa()
    mostrarMapaTkinter(mapa, []) # Pasamos una lista vacía para que al principio no haya pasos
    resuelto = False
    pasos = []
    contador = 0
    while (not resuelto) and (contador <= 5):
        contador += 1
        try:
            pasos = mapa.resolverMapa(mapa._posicionInicial)
            resuelto = True
        except Exception as e:
            print(e)
    print(pasos)
    if resuelto:
        messagebox.showinfo("¡Laberinto resuelto!", "Se encontró una solución para el laberinto.")
        mostrarMapaTkinter(mapa, pasos)
    else:
        messagebox.showerror("Laberinto no resuelto", "No se pudo encontrar un camino en el laberinto.")
