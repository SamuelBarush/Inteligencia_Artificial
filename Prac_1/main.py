import pygame
from class_Map import Board
from class_Agent import Monkey
from class_Game import Rend

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana y celda
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMANO_CELDA = 30

# Crear una instancia de la clase Board con el archivo deseado
archivo_tablero = "/home/ed/Documents/GitHub/Inteligencia_Artificial/Prac_1/board1.txt"
tablero = Board(archivo_tablero, (1, 1), (3, 3))

# Crear una instancia de la clase Agent con el tablero y el tipo Monkey
agente = Monkey(tablero)

# Crear una instancia de la clase Rend con el tablero y el agente
rend = Rend(tablero, agente, TAMANO_CELDA)

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Dibujando Tablero")

player_imagen = pygame.image.load("/home/ed/Documents/GitHub/Inteligencia_Artificial/monkey.jpeg")  # Carga la imagen 
nueva_ancho = 25  # Ancho de la celda
nueva_alto = 25  # Alto de la celda
player_imagen = pygame.transform.scale(player_imagen, (nueva_ancho, nueva_alto))


# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                agente.mover_izq()
            elif evento.key == pygame.K_RIGHT:
                agente.mover_der()
            elif evento.key == pygame.K_UP:
                agente.mover_arriba()
            elif evento.key == pygame.K_DOWN:
                agente.mover_abajo()

    ventana.fill((0, 0, 0))  # Llenar la ventana con color negro
    rend.dibujar_mapa(ventana)

    # Dibujar la bola en la posición actual del agente
    ventana.blit(player_imagen, (agente.pos_actual[0] * TAMANO_CELDA, agente.pos_actual[1] * TAMANO_CELDA))

    pygame.display.update()  # Agregar esta línea para actualizar la ventana

pygame.quit()
