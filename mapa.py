import numpy as np
from math import copysign as cs, ceil as ce
from random import randint as ri, shuffle as sf
from time import sleep as sl
from math import sqrt
from tkinter import messagebox, simpledialog
import utilidades as ut

class MapaJuego:
    def __init__(self, tamanio=6, posicionInicial=[0, 0]):
        self._tamanio = tamanio
        self._mapa = np.zeros((tamanio, tamanio), dtype=int)
        self._posicionInicial = posicionInicial
        self._posicionJugador = posicionInicial
        self._salida = [ri(0, tamanio - 1), tamanio - 1]
        self._cordenadasPortal = []
        self.preguntas_respuestas = {
            "¿Cuál es el río más largo del mundo?": "Amazonas",
            #etc etc
        }

    def celdaValida(self,celda):
        if (celda[0] < -1) or (celda[1] < -1):
            return False
        if (celda[0] > self._tamanio) or (celda[1] > self._tamanio):
            return False
        if (celda == self._posicionInicial)or(celda == self._salida):
            return False
        return True

    def celdaVisitada(self, celda):
        if (self._mapa[celda[0],celda[1]]==1):
            return True
        else:
            return False
        
    def mostrarTrivia(self):
        pregunta = ri(0, len(self.preguntas_respuestas) - 1)
        pregunta_texto = list(self.preguntas_respuestas.keys())[pregunta]
        respuesta_correcta = self.preguntas_respuestas[pregunta_texto]

        respuesta_jugador = simpledialog.askstring("Trivia", pregunta_texto)

        if respuesta_jugador is not None and respuesta_jugador.lower() == respuesta_correcta.lower():
            messagebox.showinfo("Respuesta correcta", "¡Respuesta correcta! Puedes pasar por la puerta.")
            return True
        else:
            messagebox.showerror("Respuesta incorrecta", "Respuesta incorrecta. Debes responder correctamente para pasar.")
            return False
        
    def crearCamino(self, densidadParedes):
        densidadParedes = densidadParedes *(self._tamanio ** 2)//4
        direcciones = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        for i in range(0, densidadParedes):
            x = (ri(2,self._tamanio-3)//2)*2
            y = (ri(2,self._tamanio-3)//2)*2
            if(self.celdaValida([x,y]) and (not self.celdaVisitada([x,y]))):
                self._mapa[x][y]= 1
                for dx,dy in direcciones:
                    nx = x + dx
                    ny = y + dy
                    if(self.celdaValida([nx,ny])):
                        if self._mapa[nx][ny] == 0:
                            self._mapa[nx][ny] =1
                            if(x== nx):
                                ny += int((cs(1,(ny - y))*-1))
                            if(y == ny):
                                nx += int((cs(1,(nx - x))*-1))
                            self._mapa[nx][ny] =1 
        return
    
    def crearPuertas(self):
        for i in range(0, ce(self._tamanio/10)):
            puertaCreada = False
            while not puertaCreada:
                x = ri(1,self._tamanio-2)
                y = ri(1,self._tamanio-2)
                if (self._mapa[x][y] == 1):
                    if (((self._mapa[x-1][y] == 0) and  (self._mapa[x+1][y] == 0)) or 
                       ((self._mapa[x][y-1] == 0) and  (self._mapa[x][y+1] == 0))):
                        self._mapa[x][y] = 111
                        puertaCreada = True

    def crearPortal(self):
        entradaCreada = False
        salidaCreada = False
        while not entradaCreada:
            x = ri(0,self._tamanio-1)
            y = ri(0,self._tamanio-1)
            if (self._mapa[x][y] == 0):
                self._mapa[x][y] = 3
                entradaCreada = True
                self._cordenadasPortal.append([x,y])

        while not salidaCreada:
            x = ri(0,self._tamanio-1)
            y = ri(0,self._tamanio-1)
            if (self._mapa[x][y] == 0):
                self._mapa[x][y] = 4
                salidaCreada = True
                self._cordenadasPortal.append([x,y])

    def dibujarMapa(self):
        self._mapa[self._posicionInicial[0],self._posicionInicial[1]]= 8
        self._mapa[0][2]=1 
        self.crearCamino(500)
        self.crearPuertas()
        self.crearPortal()
        self._mapa[self._salida[0],self._salida[1]]= 2
        return self


    def resolverMapa(self, posicion, pasos=[[], []]):
        menorDistancia = self._tamanio ** 2
        print(pasos)
        if posicion == self._salida:
            return pasos[0]

        # Verificar si el jugador está en una casilla de trivia
        if self._mapa[posicion[0]][posicion[1]] == 111:
            if self.mostrarTrivia():  # Mientras la respuesta sea incorrecta, seguir mostrando la trivia
                pasos[0].append(posicion)
            else:
                return pasos[0]
            
        movimientos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        sf(movimientos)
        for dx, dy in movimientos:
            nx, ny = posicion[0] + dx, posicion[1] + dy
            if (not ((nx < 0) or (ny < 0) or (nx >= self._tamanio) or (ny >= self._tamanio))) and (
                    not ([nx, ny] in pasos[0]) and not ([nx, ny] in pasos[1])):
                if ((self._mapa[nx][ny] == 0) or (self._mapa[nx][ny] == 111) or ((self._mapa[nx][ny] == 2))):
                    if (ut.distancia([nx, ny], self._salida) <= menorDistancia):
                        siguientePaso = [nx, ny]
                        menorDistancia = ut.distancia([nx, ny], self._salida)

                elif (self._mapa[nx][ny] == 3):
                    if (ut.distancia([nx, ny], self._salida) <= menorDistancia):
                        pasos[0].append([nx, ny])
                        nx, ny = self._cordenadasPortal[1][0], self._cordenadasPortal[1][1]
                        siguientePaso = [nx, ny]
                        menorDistancia = ut.distancia([nx, ny], self._salida)

                elif (self._mapa[nx][ny] == 4):
                    if (ut.distancia([nx, ny], self._salida) <= menorDistancia):
                        pasos[0].append([nx, ny])
                        nx, ny = nx, ny = self._cordenadasPortal[0][0], self._cordenadasPortal[0][1]
                        siguientePaso = [nx, ny]
                        menorDistancia = ut.distancia([nx, ny], self._salida)

        try:
            pasos[0].append(siguientePaso)
            self.resolverMapa(siguientePaso, pasos)
        except Exception as er:
            pasos[1].append(pasos[0].pop())
            self.resolverMapa(pasos[0][-2], pasos)

        return pasos[0]