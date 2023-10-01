import pygame

class Rend:

    def __init__(self, tablero, agente, TAMANO_CELDA):
        self.tablero = tablero
        self.agente = agente
        self.TAMANO_CELDA = TAMANO_CELDA
        self.colores = {
            0: (0, 0, 0),      # Black
            1: (255, 255, 255) # White
        }

    def dibujar_mapa(self, ventana):
        # Recorre las filas y columnas de la matriz de tablero
        for fila, fila_valores in enumerate(self.tablero.board_data):
            for columna, celda in enumerate(fila_valores):
                # Calcula la posición de la celda en la ventana
                x = columna * self.TAMANO_CELDA  # La posición horizontal se multiplica por el tamaño de la celda
                y = fila * self.TAMANO_CELDA     # La posición vertical se multiplica por el tamaño de la celda

                # Determina el color de la celda en función de su valor
                if celda[0] == 0:
                    color = self.colores[0]  # Si el valor es 0, el color es el primero de la lista (negro)
                else:
                    color = self.colores[1]  # Si el valor es 1, el color es el segundo de la lista (blanco)

        
                pygame.draw.rect(ventana, color, (x, y, self.TAMANO_CELDA, self.TAMANO_CELDA))