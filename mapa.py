import numpy as np
from random import randint as ri


class MapaJuego: 
    def __init__(self, tamanio = 6, posicionInicial =[0,0]):
        self._tamanio = tamanio
        self._mapa = np.ones((tamanio,tamanio), dtype=int)
        self._posicionInicial = posicionInicial
        self._posicionJugador = posicionInicial
        self._salida = [ri(0,tamanio-1),tamanio-1]


def calcularCordenadas(origen, orientacion, cardinalidad):
    if cardinalidad == 1:
        return [[origen[0]-1,origen[1]],[origen[0]-2,origen[1]]]
    elif cardinalidad ==2:
        return [[origen[0],origen[1]+1],[origen[0],origen[1]+2]]
    elif cardinalidad ==3:
        return [[origen[0]+1,origen[1]],[origen[0]+2,origen[1]]]
    elif cardinalidad ==4:
        return [[origen[0],origen[1]-1],[origen[0],origen[1]-2]]
    # if cardinalidad == 1:
    #     if orientacion == 1:
    #         return [[origen[0]-1,origen[1]],[origen[0]-2,origen[1]],[origen[0]-3,origen[1]],[origen[0]-3,origen[1]+1]]
    #     else:
    #         return [[origen[0]-1,origen[1]],[origen[0]-2,origen[1]],[origen[0]-2,origen[1]+1],[origen[0]-2,origen[1]+2]]
    # elif cardinalidad ==2:
    #     if orientacion == 1:
    #         return [[origen[0],origen[1]+1],[origen[0],origen[1]+2],[origen[0],origen[1]+3],[origen[0]+1,origen[1]+3]]
    #     else:
    #         return [[origen[0],origen[1]+1],[origen[0],origen[1]+2],[origen[0]+1,origen[1]+2],[origen[0]+2,origen[1]+2]]
    # elif cardinalidad ==3:
    #     if orientacion == 1:
    #         return [[origen[0]+1,origen[1]],[origen[0]+2,origen[1]],[origen[0]+3,origen[1]],[origen[0]+3,origen[1]-1]]
    #     else:
    #         return [[origen[0]+1,origen[1]],[origen[0]+2,origen[1]],[origen[0]+2,origen[1]-1],[origen[0]+2,origen[1]-2]]
    # elif cardinalidad ==4:
    #     if orientacion == 1:
    #         return [[origen[0],origen[1]-1],[origen[0],origen[1]-2],[origen[0],origen[1]-3],[origen[0]-1,origen[1]-3]]
    #     else:
    #         return [[origen[0],origen[1]-1],[origen[0],origen[1]-2],[origen[0]-1,origen[1]-2],[origen[0]-2,origen[1]-2]]


def crearCamino(mapaJuego,posicionInicial):
    ultimaPosicion = posicionInicial
    for i in calcularCordenadas(posicionInicial,ri(1,2),ri(1,4)):
        if not((i[0] < 0) or (i[0] >= mapaJuego._tamanio)):
            if not((i[1] < 0) or (i[1] >= mapaJuego._tamanio)):
                if not((i[0] == 0) and (i[1] == 0)):
                    mapaJuego._mapa[i[0]][i[1]] = 0
                    ultimaPosicion = i
                else:
                    break
            else:
                break
        else:
            break
    if not (mapaJuego._salida == ultimaPosicion):
        crearCamino(mapaJuego, ultimaPosicion)

    return


def dibujarMapa(mapaJuego):
    mapaJuego._mapa[mapaJuego._posicionInicial[0],mapaJuego._posicionInicial[1]]= 8
    crearCamino(mapaJuego,mapaJuego._posicionInicial)
    mapaJuego._mapa[mapaJuego._salida[0],mapaJuego._salida[1]]= 2
    return mapaJuego

def resolverMapa(mapaJuego):
    pass


if __name__ == "__main__":
    mapa = dibujarMapa(MapaJuego(15))

    print(mapa._mapa)