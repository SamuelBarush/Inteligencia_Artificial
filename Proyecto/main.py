from class_Map import Board
from class_Game import Rend
from class_Agent import *
from class_Astar import AStar 
import pygame

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMANO_CELDA = 30

TEMPLE = (5,4)
KEY = (3,3)
PORTAL = (3,14)

archivo_tablero = "./board1.txt"

HUMAN = (1,1)
OCTOPUS = (2,2)

pygame.init()


mapa = Board(archivo_tablero, HUMAN , OCTOPUS ,KEY, PORTAL , TEMPLE  )

agent_human = Human(mapa)
human_image = pygame.image.load("./human.png")
agent_octopus = Octopus(mapa)
octupus_image = pygame.image.load("./octopus.png")
temple_image = pygame.image.load("./temple.png")
portal_image = pygame.image.load("./portal.png")
key_image = pygame.image.load("./key.png")
temple_destroid_image = pygame.image.load("./temple_destroid.png")
two_keys_image = pygame.image.load("./two_keys.png")


rend = Rend(mapa, agent_human, agent_octopus, TAMANO_CELDA)

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Dibujando Tablero")


nueva_ancho = 25
nueva_alto = 25

human_image = pygame.transform.scale(human_image, (nueva_ancho, nueva_alto))
octupus_image = pygame.transform.scale(octupus_image, (nueva_ancho, nueva_alto))
temple_image = pygame.transform.scale(temple_image, (nueva_ancho, nueva_alto))
portal_image = pygame.transform.scale(portal_image, (nueva_ancho, nueva_alto))
key_image = pygame.transform.scale(key_image, (nueva_ancho, nueva_alto))
temple_destroid_image = pygame.transform.scale(temple_destroid_image, (nueva_ancho, nueva_alto))
two_keys_image = pygame.transform.scale(two_keys_image, (nueva_ancho, nueva_alto))

astarHuman = AStar(mapa, agent_human)
astarOctopus = AStar(mapa, agent_octopus)

portal = mapa.board_portal
key = mapa.board_key
temple = mapa.board_temple
startHuman = mapa.board_init_human
startOctopus = mapa.board_init_octu

pathHumanKey = astarHuman.astar_search(startHuman, key)
pathHumanKeyTemple = astarHuman.astar_search(key, temple)
pathHumanKeyTemplePortal = astarHuman.astar_search(temple, portal)


pathOctopusKey = astarOctopus.astar_search(startOctopus, key)
pathOctopusKeyTemple = astarOctopus.astar_search(key, temple)
pathOctopusKeyTemplePortal = astarOctopus.astar_search(temple, portal)

ejecutar = True
path_index_HK = 0
path_index_HKT = 0
path_index_HKTP = 0

path_index_OK = 0
path_index_OKT = 0
path_index_OKTP = 0

flag_HK = True
flag_HKT = True
flag_HKTP = True
flag_OK = True
flag_OKT = True
flag_OKTP = True

while ejecutar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:  # Check for the spacebar key (you can change this to any key you prefer)
                show_info = True    
            
    ventana.fill((0, 0, 0))

    if pathHumanKey is not None:
        if (path_index_HK < len(pathHumanKey)) and (flag_HK == True):
            next_position = pathHumanKey[path_index_HK]
            agent_human.set_pos_actual(next_position)
            path_index_HK += 1
            if next_position == KEY:
                flag_HK = False
                print("Human Reached the key!")
        elif pathHumanKeyTemple is not None:
            if (path_index_HKT < len(pathHumanKeyTemple)) and (flag_HKT == True):
                next_position = pathHumanKeyTemple[path_index_HKT]
                agent_human.set_pos_actual(next_position)
                path_index_HKT += 1
                if next_position == TEMPLE:
                    flag_HKT = False
                    print("Human Reached the temple!")
            elif pathHumanKeyTemplePortal is not None:
                if (path_index_HKTP < len(pathHumanKeyTemplePortal)) and (flag_HKTP == True):
                    next_position = pathHumanKeyTemplePortal[path_index_HKTP]
                    agent_human.set_pos_actual(next_position)
                    path_index_HKTP += 1
                    if next_position == PORTAL:
                        flag_HKTP = False
                        print("Human Reached the portal!")
            
    if pathOctopusKey is not None:
        if (path_index_HK < len(pathOctopusKey)) and (flag_OK == True):
            next_position = pathOctopusKey[path_index_OK]
            agent_octopus.set_pos_actual(next_position)
            path_index_OK += 1
            if next_position == KEY:
                flag_OK = False
                print("Octopus Reached the key!")
        elif pathOctopusKeyTemple is not None:
            if (path_index_OKT < len(pathOctopusKeyTemple)) and (flag_OKT == True):
                next_position = pathOctopusKeyTemple[path_index_OKT]
                agent_octopus.set_pos_actual(next_position)
                path_index_OKT += 1
                if next_position == TEMPLE:
                    flag_OKT = False
                    print("Octopus Reached the temple!")
            elif pathOctopusKeyTemplePortal is not None:
                if (path_index_OKTP < len(pathHumanKeyTemplePortal)) and (flag_OKTP == True):
                    next_position = pathOctopusKeyTemplePortal[path_index_OKTP]
                    agent_octopus.set_pos_actual(next_position)
                    path_index_OKTP += 1
                    if next_position == PORTAL:
                        flag_OKTP = False
                        print("Octopus Reached the portal!")
                        
    rend.dibujar_mapa(ventana)
    
    if flag_HK and flag_OK:
        ventana.blit(two_keys_image,(KEY[0] * TAMANO_CELDA, KEY[1] * TAMANO_CELDA))
    elif not flag_HK and not flag_OK:
        ventana.blit(key_image,(KEY[0] * TAMANO_CELDA, KEY[1] * TAMANO_CELDA))
  

        
    if flag_HKT and flag_OKT:
        ventana.blit(temple_image,(TEMPLE[0] * TAMANO_CELDA, TEMPLE[1] * TAMANO_CELDA))
    else:
        ventana.blit(temple_destroid_image,(TEMPLE[0] * TAMANO_CELDA, TEMPLE[1] * TAMANO_CELDA))
        
    ventana.blit(portal_image,(PORTAL[0] * TAMANO_CELDA, PORTAL[1] * TAMANO_CELDA))
    
    if flag_HKTP:
        ventana.blit(human_image, (agent_human.pos_actual[0] * TAMANO_CELDA, agent_human.pos_actual[1] * TAMANO_CELDA))
    if flag_OKTP:
        ventana.blit(octupus_image, (agent_octopus.pos_actual[0] * TAMANO_CELDA, agent_octopus.pos_actual[1] * TAMANO_CELDA))   
    
    pygame.display.update()
    pygame.time.delay(150)

astarHuman.render_decision_tree()
astarOctopus.render_decision_tree()
    
pygame.quit()