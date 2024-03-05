import numpy as np
from math import copysign as cs, ceil as ce
from random import randint as ri, shuffle as sf


class MapaJuego: 
    def __init__(self, tamanio = 6, posicionInicial =[0,0]):
        self._tamanio = tamanio
        self._mapa = np.zeros((tamanio,tamanio), dtype=int)
        self._posicionInicial = posicionInicial
        self._posicionJugador = posicionInicial
        self._salida = [ri(0,tamanio-1),tamanio-1]
        self._cordenadasPortal = []

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


def mostrarMapaConsola(mapaJuego):
    caracteres ={
        0: ' ',
        1: '#',
        8: '*',
        2: '>',
        111: '?',
        3: '3',
        4: '4'
    }
    for fila in mapaJuego._mapa:
        for valor in fila:
            print(caracteres[valor], end=' ')
        print()


def resolverMapa(mapaJuego):
    pass


if __name__ == "__main__":
    mapa = MapaJuego(10)
    mapa.dibujarMapa()
    #print(mapa._mapa)
    #print(mapa._cordenadasPortal)
    mostrarMapaConsola(mapa)