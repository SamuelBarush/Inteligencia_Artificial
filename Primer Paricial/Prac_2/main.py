from class_Agent import *
from class_Algorithms import *
import pygame
from class_Map import Board
from class_Game import Rend
import time 


"""
GLOBAL SETTINGS
"""

# Metrics
START = (1,1)
GOAL = (14,14)

# priority
RIGHT = (0, -1)
LEFT = (0, 1)
DOWN = (1, 0)
UP = (-1, 0)

PRIORITY = [RIGHT,LEFT,UP,DOWN ]

#DepthFirstSearch = 1
#BreathFirtSearch = 0

USING_ALGORITHM = 0


# Window size and cell size
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMANO_CELDA = 30

# Movement
SPEED = 5

# Board file
archivo_tablero = "./board1.txt"

# player file
player_file = "./monkey.jpeg"

# graph path
graph_path = "search_graph.pdf"

"""
--- END SETTINGS
"""


# Initialize Pygame
pygame.init()

tablero = Board(archivo_tablero, START, GOAL)

# Create an instance of the Agent class with the board and Octopus type
agente = Octopus(tablero)

# Create an instance of the Rend class with the board and agent
rend = Rend(tablero, agente, TAMANO_CELDA)

# Create the window
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Dibujando Tablero")

# Load the player image and scale it
player_imagen = pygame.image.load(player_file)
nueva_ancho = 25
nueva_alto = 25
player_imagen = pygame.transform.scale(player_imagen, (nueva_ancho, nueva_alto))

# Define the start and goal positions
start = tablero.board_init
goal = tablero.board_end



if USING_ALGORITHM == 0:
    bfs = BreadthFirstSearch(tablero, agente,PRIORITY)
    path = bfs.bfs_search(start, goal)
    graph = bfs.visualize_graph(graph_path)
    
else:
    dfs = DepthFirstSearch(tablero, PRIORITY)
    path = dfs.dfs_search(start, goal)
    graph = dfs.visualize_graph(graph_path)


if path is None:
    print("No path found.")
else:
    path, decisions = path
    print(path)
    print(decisions)

    # Bucle principal
    ejecutando = True
    path_index = 0  # Initialize the index for the path

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    show_info = True

        ventana.fill((0, 0, 0))

        if path_index < len(path):
            next_position = path[path_index]
            agente.set_pos_actual(next_position)
            path_index += 1

            if isinstance(decisions, list) and path_index < len(decisions):
                decision = decisions[path_index - 1]
                print(f"Decision for {next_position}: {decision}")
            elif isinstance(decisions, dict) and next_position in decisions:
                decision = decisions[next_position]
                print(f"Decision for {next_position}: {decision}")

        else:
            print("Reached the goal!")
            time.sleep(10000)

        rend.dibujar_mapa(ventana)

        # Draw the agent at its current position
        ventana.blit(player_imagen, (agente.pos_actual[0] * TAMANO_CELDA, agente.pos_actual[1] * TAMANO_CELDA))

        pygame.display.update()
        pygame.time.delay(SPEED)  # Adjust the delay as needed

# Ensure that you call pygame.quit() at the end of the script.
pygame.quit()