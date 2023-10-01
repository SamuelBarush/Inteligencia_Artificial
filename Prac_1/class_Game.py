import pygame
from class_Map import Map
from class_Agent import Agente

# Tamaño de la ventana y celda
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMANO_CELDA = 30

class Rend:

    def __init__(self, tablero, agente):
        self.tablero = list(getattr(tablero , "board_data"))
        self.agente = agente



    def dibujar_mapa(self, ventana, tipo_terreno):  # Asegúrate de pasar la ventana como argumento
        self.tipo_terreno = tipo_terreno
        colores = {
            0: (0 , 0 , 0),  # Black
            1: (255 , 255 , 255),  # White
        }
        for fila, fila_valores in enumerate(self.tablero):
            for columna, celda in enumerate(fila_valores):
                # Calcular la posición de la celda en la ventana
                x = columna * TAMANO_CELDA
                y = fila * TAMANO_CELDA
                if celda == 0:
                    color = colores[0]
                else:
                    color = colores[1]
                pygame.draw.rect(ventana, color, (x, y, TAMANO_CELDA, TAMANO_CELDA))
               
