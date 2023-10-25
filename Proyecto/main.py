from class_Map import Board
from class_Agent import *
import pygame

pygame.init()

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMANO_CELDA = 30

# Create an instance of the Board class with the desired file
archivo_tablero = "../Prac_1/board1.txt"
tablero = Board(archivo_tablero, (1, 1), (14, 14), (7, 7), (7, 7), (7, 7))

