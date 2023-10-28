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


mapa = Board(archivo_tablero, HUMAN , OCTOPUS ,KEY, PORTAL , TEMPLE  )

agent_human = Human(mapa)
human_image = pygame.image.load("./human.png")
agent_octopus = Octopus(mapa)
octupus_image = pygame.image.load("./octopus.png")


rend = Rend(mapa, agent_human, agent_octopus, TAMANO_CELDA)

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Dibujando Tablero")


nueva_ancho = 25
nueva_alto = 25

human_image = pygame.transform.scale(human_image, (nueva_ancho, nueva_alto))
octupus_image = pygame.transform.scale(octupus_image, (nueva_ancho, nueva_alto))

astarHuman = AStar(mapa, agent_human)
astarOctopus = AStar(mapa, agent_octopus)

portal = mapa.board_portal
key = mapa.board_key
temple = mapa.board_temple
startHuman = mapa.board_init_human
startOctopus = mapa.board_init_octu

pathHumanKey = astarHuman.astar_search(startHuman, key)
#pathHumanKeyTemple = astarHuman.astar_search(key, temple)
#pathHumanKeyTemplePortal = astarHuman.astar_search(temple, portal)


pathOctopusKey = astarOctopus.astar_search(startOctopus, key)
#pathOctopusKeyTemple = astarOctopus.astar_search(key, temple)
#pathOctopusKeyTemplePortal = astarOctopus.astar_search(temple, portal)

ejecutar = True
path_index_HK = 0
path_index_HKT = 0
path_index_HKTP = 0
path_index_OK = 0
path_index_OKT = 0
path_index_OKTP = 0

while ejecutar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:  # Check for the spacebar key (you can change this to any key you prefer)
                show_info = True    
            
    ventana.fill((0, 0, 0))

    if pathHumanKey is not None:
        if path_index_HK < len(pathHumanKey):
            agent_human.pos_actual = pathHumanKey[path_index_HK]
            path_index_HK += 1
        else:
            print("Reached the key!")
            pathHumanKeyTemple = astarHuman.astar_search(key, temple)
            if path_index_HKT < len(pathHumanKeyTemple):
                agent_human.pos_actual = pathHumanKeyTemple[path_index_HKT]
                path_index_HKT += 1
            else:
                print("Reached the temple!")
                pathHumanKeyTemplePortal = astarHuman.astar_search(temple, portal)
                if path_index_HKTP < len(pathHumanKeyTemplePortal):
                    agent_human.pos_actual = pathHumanKeyTemplePortal[path_index_HKTP]
                    path_index_HKTP += 1
                else:
                    print("Reached the portal!")
                    
    if pathOctopusKey is not None:
        if path_index_OK < len(pathOctopusKey):
            agent_octopus.pos_actual = pathOctopusKey[path_index_OK]
            path_index_OK += 1
        else:
            print("Reached the key!")
            pathOctopusKeyTemple = astarOctopus.astar_search(key, temple)
            if path_index_OKT < len(pathOctopusKeyTemple):
                agent_octopus.pos_actual = pathOctopusKeyTemple[path_index_OKT]
                path_index_OKT += 1
            else:
                print("Reached the temple!")
                pathOctopusKeyTemplePortal = astarOctopus.astar_search(temple, portal)
                if path_index_OKTP < len(pathOctopusKeyTemplePortal):
                    agent_octopus.pos_actual = pathOctopusKeyTemplePortal[path_index_OKTP]
                    path_index_OKTP += 1
                else:
                    print("Reached the portal!")              
            
    rend.dibujar_mapa(ventana)

    ventana.blit(human_image, (agent_human.pos_actual[0] * TAMANO_CELDA, agent_human.pos_actual[1] * TAMANO_CELDA))
    ventana.blit(octupus_image, (agent_octopus.pos_actual[0] * TAMANO_CELDA, agent_octopus.pos_actual[1] * TAMANO_CELDA))   
    pygame.display.update()
    pygame.time.delay(500)

astarHuman.render_decision_tree()
astarOctopus.render_decision_tree()
    
pygame.quit()