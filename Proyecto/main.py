from class_Map import Board
from class_Game import Rend
from class_Agent import *
from class_Astar import AStar 
import pygame

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMANO_CELDA = 30

TEMPLE = (5,5)
KEY = (3,3)
PORTAL = (2,2)

archivo_tablero = "./board1.txt"

HUMAN = (1,1)
OCTOPUS = (5,7)

pygame.init()

mapa = Board(archivo_tablero, HUMAN , OCTOPUS , TEMPLE , KEY , PORTAL)

agent_human = Human(mapa)
human_image = pygame.image.load("./human.png")
agent_octopus = Octopus(mapa)
octupus_image = pygame.image.load("./octopus.png")

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Dibujando Tablero")

nueva_ancho = 25
nueva_alto = 25

human_image = pygame.transform.scale(human_image, (nueva_ancho, nueva_alto))
octupus_image = pygame.transform.scale(octupus_image, (nueva_ancho, nueva_alto))

portal = mapa.board_portal
key = mapa.board_key
temple = mapa.board_temple
startHuman = mapa.board_init_human
startOctopus = mapa.board_init_octu

astarHuman = AStar(mapa, agent_human)
astarOctopus = AStar(mapa, agent_octopus)

pathHumanKey = astarHuman.astar_search(startHuman, key)
pathHumanKeyTemple = astarHuman.astar_search(key, temple)
pathHumanKeyTemplePortal = astarHuman.astar_search(temple, portal)


pathOctopusKey = astarOctopus.astar_search(startOctopus, key)
pathOctopusKeyTemple = astarOctopus.astar_search(key, temple)
pathOctopusKeyTemplePortal = astarOctopus.astar_search(temple, portal)

ejecutar = True
path_index = 0

while ejecutar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False
            
    ventana.fill((0, 0, 0))
    
    #if (pathHumanKey is not None) and (pathOctopusKey is not None):
    #    if path_index



pygame.quit()