from tkinter import Tk, Canvas, mainloop
from tkinter import messagebox, simpledialog
import mapa as m


def mostrarMapaTkinter(mapaJuego, pasos, laberinto_resuelto=False):
    # Crear una ventana principal
    root = Tk()
    canvas = Canvas(root, width=600, height=600)
    canvas.pack()
    root.geometry("500x400")  # Establecer el tamaño de la ventana principal

    # Canvas para el mapa original
    canvas_original = Canvas(root, width=600, height=600)
    canvas_original.pack(side="left")

    # Canvas para el mapa con el recorrido
    canvas_recorrido = Canvas(root, width=600, height=600)
    canvas_recorrido.pack(side="right")

    # Creamos un conjunto para las coordenadas especiales
    coordenadas_especiales = set()
    coordenadas_especiales.add(tuple(mapaJuego._posicionInicial))
    coordenadas_especiales.add(tuple(mapaJuego._salida))
    for portal in mapaJuego._cordenadasPortal:
        coordenadas_especiales.add(tuple(portal))

    # Iterar sobre cada celda del mapa
    for i in range(mapaJuego._tamanio):
        for j in range(mapaJuego._tamanio):
            x1, y1 = j * 30, i * 30
            x2, y2 = x1 + 30, y1 + 30
            # Colorear ubicaciones especiales primero
            if (i, j) in coordenadas_especiales:  
                if (i, j) == tuple(mapaJuego._posicionInicial):
                    canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
                elif (i, j) == tuple(mapaJuego._salida):
                    canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                elif (i, j) == tuple(mapaJuego._cordenadasPortal[0]):
                    canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                elif (i, j) == tuple(mapaJuego._cordenadasPortal[1]):
                    canvas.create_rectangle(x1, y1, x2, y2, fill="red")
                elif (i, j) == (1, 1):  # Nueva casilla "trivia"
                    canvas.create_rectangle(x1, y1, x2, y2, fill="orange")
            # Colorear el recorrido
            elif [i, j] in pasos:
                if (i, j) not in coordenadas_especiales:  # Evitar colorear ubicaciones especiales
                    canvas.create_rectangle(x1, y1, x2, y2, fill="pink")
            # Colorear las celdas según su tipo
            elif mapaJuego._mapa[i][j] == 0:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            elif mapaJuego._mapa[i][j] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            elif mapaJuego._mapa[i][j] == 2:
                canvas.create_rectangle(x1, y1, x2, y2, fill="green")
            elif mapaJuego._mapa[i][j] == 111:  # Casilla "trivia"
                canvas.create_rectangle(x1, y1, x2, y2, fill="orange")

    # Mostrar mensaje si el laberinto ha sido resuelto
    if laberinto_resuelto:
        texto = "¡Laberinto resuelto! Se encontró una solución para el laberinto." 
        canvas.create_text(250, 380, text=texto, font=("Arial", 12), fill="blue")

    root.mainloop()

if __name__ == "__main__":
    # Crear la matriz de mapa con un tamaño de 10x10
    mapa = m.MapaJuego(10)
    mapa.dibujarMapa()
    mostrarMapaTkinter(mapa, [])  # Pasamos una lista vacía para que al principio no haya pasos
    resuelto = False
    pasos = []
    contador = 0
    # Intenta resolver el laberinto hasta 5 intentos
    while (not resuelto) and (contador <= 5):
        contador += 1
        try:
            pasos = mapa.resolverMapa(mapa._posicionInicial)
            resuelto = True
        except Exception as e:
            print(e)
    print(pasos)
    # Mostrar el laberinto con la solución si se encontró una
    if resuelto:
        mostrarMapaTkinter(mapa, pasos, laberinto_resuelto=True)
    else:
        messagebox.showerror("Laberinto no resuelto", "No se pudo encontrar un camino en el laberinto.")
