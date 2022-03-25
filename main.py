# IMPORTS
import random as r
import copy as c

# CARACTERISTICAS DE DIBUJO
SEPARADOR = "="
CANTIDAD_SEPARADOR = 7

# ITEMS
FANTASMA = " @ "
PREMIO = " O "

# BLOQUE
PARED = " X "

# PERSONAJE
PACMAN_DERECHA = " > "
PACMAN_IZQUIERDA = " < "
PACMAN_ARRIBA = " ^ "
PACMAN_ABAJO = " v "

posicionX = 1
posicionY = 1

# CARACTERÍSTICAS DEL TABLERO
BORDES_HORIZONTALES = " - "
BORDES_VERTICALES = "|"
nFilas = 7
nColumnas = 8
tablero = [["   "] * nColumnas for i in range(nFilas)]

# REGLAS
VIDAS = 1
PUNTAJE = 0
cantidadPremios = 0
cantidadFantasmas = 0
cantidadParedes = 0

# TECLAS
ARRIBA = "W"
ABAJO = "S"
DERECHA = "A"
IZQUIERDA = "D"
TERMINAR = "F"


# Atributos del jugador
nombreJugador = input("Ingrese su nombre: ")


def inicio():
    print(SEPARADOR * CANTIDAD_SEPARADOR, "MENÚ DE INICIO",
          SEPARADOR * CANTIDAD_SEPARADOR, "\n")
    print("Bienvenido", (nombreJugador.capitalize()), "seleccione una opción\n")
    print("1. Iniciar Juego")
    print("2. Salir")


def marcoTablero():
    for j in range(nColumnas):
        tablero[0][j] = BORDES_HORIZONTALES
        tablero[nFilas-1][j] = BORDES_HORIZONTALES

    for i in range(nFilas):
        tablero[i][0] = BORDES_VERTICALES
        tablero[i][nColumnas-1] = BORDES_VERTICALES


def paredesTablero():
    global cantidadParedes
    while(True):
        cantidadParedes = int(input("Ingrese la cantidad de paredes [5-12]: "))
        if (cantidadParedes >= 5) and (cantidadParedes <= 12):
            break
    fantasmasTablero()


def fantasmasTablero():
    global cantidadFantasmas
    while(True):
        cantidadFantasmas = int(
            input("Ingrese la cantidad de fantasmas [1-6]: "))
        if (cantidadFantasmas >= 3) and (cantidadFantasmas <= 6):
            break
    premiosTablero()


def premiosTablero():
    global cantidadPremios
    while(True):
        cantidadPremios = int(input("Ingrese la cantidad de premios [3-6]: "))
        if (cantidadPremios >= 3) and (cantidadPremios <= 6):
            break
    rellenarTablero()


def rellenarTablero():
    cPremios = c.copy(cantidadPremios)
    while(cPremios > 0):
        numRanX = r.randint(1, 5)
        numRanY = r.randint(1, 6)

        if(tablero[numRanX][numRanY] == "   "):
            tablero[numRanX][numRanY] = PREMIO
            cPremios -= 1

    cFantasmas = c.copy(cantidadFantasmas)
    while(cFantasmas > 0):
        numRanX = r.randint(1, 6)
        numRanY = r.randint(1, 6)
        if(tablero[numRanX][numRanY] == "   "):
            tablero[numRanX][numRanY] = FANTASMA
            cFantasmas -= 1

    cParedes = c.copy(cantidadParedes)
    while(cParedes > 0):
        numRanX = r.randint(1, 6)
        numRanY = r.randint(1, 6)
        if(tablero[numRanX][numRanY] == "   "):
            tablero[numRanX][numRanY] = PARED
            cParedes -= 1
    imprimirTablero()
    posicionPacman()


def posicionPacman():
    global posicionX
    global posicionY

    while(True):
        posicionX = int(input("\nIniciar en la fila: "))
        posicionY = int(input("Iniciar en la columna: "))
        if(tablero[posicionX][posicionY] == "   "):
            tablero[posicionX][posicionY] = PACMAN_ABAJO
            break
        else: 
            print("\nLa posición ya está ocupada\n")
            imprimirTablero()
    imprimirTablero()


def movimientosPacman():
    print()


def opciones():
    opcion = input("")
    if(opcion == "1"):
        paredesTablero()
    else:
        print("Hasta pronto")


def imprimirTablero():
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" ")
        print()


inicio()
marcoTablero()
opciones()
