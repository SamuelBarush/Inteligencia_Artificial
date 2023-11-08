from class_Map import Board
from class_Game import Rend
from class_Agent import *
from class_Astar import AStar 
import pygame

#Parametros de la ventana

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMANO_CELDA = 30

#Coordenadas de los elementos del mapa
TEMPLE = (10,2)
KEY = (13,14)
PORTAL = (10,9)
HUMAN = (7,2)
OCTOPUS = (13,11)

#Archivo del mapa
archivo_tablero = "./board1.txt"

pygame.init()

#Creacion de los mapas para los agentes
mapaH = Board(archivo_tablero, HUMAN ,KEY, PORTAL , TEMPLE  )
mapaO = Board(archivo_tablero, OCTOPUS ,KEY, PORTAL , TEMPLE  )

#Creacion de los agentes
agent_human = Human(mapaH)
agent_octopus = Octopus(mapaO)

#Cargar imagenes
human_image = pygame.image.load("./human.png")
octupus_image = pygame.image.load("./octopus.png")
temple_image = pygame.image.load("./temple.png")
portal_image = pygame.image.load("./portal.png")
key_image = pygame.image.load("./key.png")
temple_destroid_image = pygame.image.load("./temple_destroid.png")
two_keys_image = pygame.image.load("./two_keys.png")


rend = Rend(mapaH,mapaO, TAMANO_CELDA)

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

astarHuman = AStar(mapaH, agent_human, "Human")
astarOctopus = AStar(mapaO, agent_octopus, "Octopus")

portalH = mapaH.board_portal
keyH = mapaH.board_key
templeH = mapaH.board_temple
startHuman = mapaH.board_init
startOctopus = mapaO.board_init

portalO = mapaO.board_portal
keyO = mapaO.board_key
templeO = mapaO.board_temple

pathHumanKey = astarHuman.astar_search(startHuman, keyH)
pathHumanKeyTemple = astarHuman.astar_search(keyH, templeH)
pathHumanKeyTemplePortal = astarHuman.astar_search(templeH, portalH)


pathOctopusKey = astarOctopus.astar_search(startOctopus, keyH)
pathOctopusKeyTemple = astarOctopus.astar_search(keyH, templeH)
pathOctopusKeyTemplePortal = astarOctopus.astar_search(templeH, portalH)

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
        if (path_index_OK < len(pathOctopusKey)) and (flag_OK == True):
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
                if (path_index_OKTP < len(pathOctopusKeyTemplePortal)) and (flag_OKTP == True):
                    next_position = pathOctopusKeyTemplePortal[path_index_OKTP]
                    agent_octopus.set_pos_actual(next_position)
                    path_index_OKTP += 1
                    if next_position == PORTAL:
                        flag_OKTP = False
                        print("Octopus Reached the portal!")
                        
    rend.dibujar_mapa(ventana)
    
    if flag_HK and flag_OK:
        ventana.blit(two_keys_image,(KEY[0] * TAMANO_CELDA, KEY[1] * TAMANO_CELDA))
    elif flag_HK or flag_OK:
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
    
    if flag_HKTP == False and flag_OKTP == False:
        ejecutar = False

#astarHuman.render_decision_tree("human")
#astarOctopus.render_decision_tree("octopus")
    
pygame.quit()