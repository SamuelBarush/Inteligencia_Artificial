import pygame


from class_Map import Board
from class_Agent import Monkey
from class_Game import Rend
from class_Astar import AStar 

# Initialize Pygame
pygame.init()

# Window size and cell size
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMANO_CELDA = 30

# Create an instance of the Board class with the desired file
archivo_tablero = "/home/ed/Documents/GitHub/Inteligencia_Artificial/Prac_1/board1.txt"
tablero = Board(archivo_tablero, (1, 1), (5, 3))

# Create an instance of the Agent class with the board and Monkey type
agente = Monkey(tablero)

# Create an instance of the Rend class with the board and agent
rend = Rend(tablero, agente, TAMANO_CELDA)

# Create the window
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Dibujando Tablero")

# Load the player image and scale it
player_imagen = pygame.image.load("/home/ed/Documents/GitHub/Inteligencia_Artificial/monkey.jpeg")
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
path_index = 0  # Initialize the index for the path
show_info = False  # Flag to show info

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:  # Check for the spacebar key (you can change this to any key you prefer)
                show_info = True

    ventana.fill((0, 0, 0))

    if path is not None and not show_info:
        if path_index < len(path):
            next_position = path[path_index]
            agente.set_pos_actual(next_position)
            path_index += 1
        else:
            show_info = True  # Show info after reaching the goal
            print("Reached the goal!")

    rend.dibujar_mapa(ventana)

    # Draw the agent at its current position
    ventana.blit(player_imagen, (agente.pos_actual[0] * TAMANO_CELDA, agente.pos_actual[1] * TAMANO_CELDA))


    if show_info:
        # Get the explored nodes and path
        explored_nodes = astar.get_explored_nodes()
        path_to_node = astar.get_path_to_node(goal)

        # Save explored nodes and path to a text file
        with open("exploration_data.txt", "w") as file:
            file.write("Nodos explorados:\n")
            for node in explored_nodes:
                file.write(str(node) + "\n")

            file.write("\nCamino seguido:\n")
            for node in path_to_node:
                file.write(str(node) + "\n")

    pygame.display.update()

    # Add a delay to slow down the movement (in milliseconds)
    pygame.time.delay(500)  # Adjust the delay as needed

astar.render_decision_tree()

pygame.quit()
