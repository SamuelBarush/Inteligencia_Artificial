from class_Agent import *
import pygame

from class_Map import Board
from class_Game import Rend
from class_Astar import AStar 


"""
GLOBAL SETTINGS
"""
# Select AGENT_TYPE
# Monkey 0
# Octopus 1
AGENT_TYPE = 0

# Metrics
START = (0,5)
GOAL = (7,5)

# Window size and cell size
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMANO_CELDA = 30

# Movement
SPEED = 500

# Board file
archivo_tablero = "./board1.txt"

"""
--- END SETTINGS
"""


# Initialize Pygame
pygame.init()

# Create an instance of the Board class with the desired file

tablero = Board(archivo_tablero, START, GOAL)

# Create an instance of the Agent class with the board and Monkey type
if AGENT_TYPE == 0:
    agente = Monkey(tablero)
    player_imagen = pygame.image.load("./monkey.jpeg")
else:
    agente = Octopus(tablero)
    player_imagen = pygame.image.load("./octopus.png")

# Create an instance of the Rend class with the board and agent
rend = Rend(tablero, agente, TAMANO_CELDA)

# Create the window
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Dibujando Tablero")

# Load the player image and scale it

nueva_ancho = 25
nueva_alto = 25
player_imagen = pygame.transform.scale(player_imagen, (nueva_ancho, nueva_alto))

# Create an AStar instance with the board and agent
astar = AStar(tablero, agente)

# Define the start and goal positions
start = tablero.board_init
goal = tablero.board_end

# Find the path using A*
path = astar.astar_search(start, goal)


# Bucle principal
ejecutando = True
flag = True
path_index = 0  # Initialize the index for the path

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:  # Check for the spacebar key (you can change this to any key you prefer)
                show_info = True

    ventana.fill((0, 0, 0))

    if path is not None:
        if path_index < len(path):
            next_position = path[path_index]
            agente.set_pos_actual(next_position)
            path_index += 1
        else:           
            print("Reached the goal!")
            flag = False
            
    rend.dibujar_mapa(ventana)

    # Draw the agent at its current position
    ventana.blit(player_imagen, (agente.pos_actual[0] * TAMANO_CELDA, agente.pos_actual[1] * TAMANO_CELDA))

    pygame.display.update()

    # Add a delay to slow down the movement (in milliseconds)
    pygame.time.delay(SPEED)  # Adjust the delay as needed
    
    if flag == False:
        ejecutando = False

#astar.render_decision_tree()
pygame.quit()
