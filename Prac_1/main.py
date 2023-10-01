import pygame
<<<<<<< Updated upstream
import sys

# Construyendo la ventana del juego

Ventana_ancho = 800
Ventana_alto = 600
Celda_ancho = 40
Celda_alto = 40

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Definir una matriz para representar el mapa
mapa = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

class Usuario:

    def __init__(self, name, visited_cells, decision_places, initial_position, real_position):
        self.name = name
        self.visited_cells = visited_cells
        self.decision_places = decision_places
        self.initial_position = initial_position
        self.real_position = real_position

    def move(self, direction):
        # Actualiza la posición actual del usuario
        self.real_position = direction

    def make_decision(self, decision):
        # Registra el lugar donde se tomó una decisión
        self.decision_places.append(decision)

    def visit_road(self, road):
        # Registra una celda de camino visitada
        self.visited_cells.append(road)

def dibujar_mapa(ventana):  # Asegúrate de pasar la ventana como argumento
    for fila in range(len(mapa)):
        for columna in range(len(mapa[fila])):
            if mapa[fila][columna] == 1:
                pygame.draw.rect(ventana, NEGRO, (columna * Celda_ancho, fila * Celda_alto, Celda_ancho, Celda_alto))
            else:
                pygame.draw.rect(ventana, BLANCO, (columna * Celda_ancho, fila * Celda_alto, Celda_ancho, Celda_alto))

def main():
    pygame.init()
    ventana = pygame.display.set_mode((Ventana_ancho, Ventana_alto))
    pygame.display.set_caption("Mapa con Pygame")

    reloj = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ventana.fill(ROJO)
        dibujar_mapa(ventana)  # Pasa la ventana como argumento
        pygame.display.update()
        reloj.tick(10)

if __name__ == "__main__":
    main()
=======
from class_Map import Board
from class_Agent import Agent
from class_Game import Rend

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana y celda
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMANO_CELDA = 30

# Crear una instancia de la clase Board con el archivo deseado
archivo_tablero = "Prac_1/board1.txt"
tablero = Board(archivo_tablero, (1, 1), (3, 3))

# Crear una instancia de la clase Agent
agente = Agent(tablero)

# Crear una instancia de la clase Rend
rend = Rend(tablero, agente, TAMANO_CELDA)

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Dibujando Tablero")

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((0, 0, 0))  # Llenar la ventana con color negro
    rend.dibujar_mapa(ventana)
    pygame.display.update()

pygame.quit()
>>>>>>> Stashed changes
