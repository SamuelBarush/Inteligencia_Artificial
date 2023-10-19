import pygame

class Rend:
    def __init__(self, tablero, agente, TAMANO_CELDA):
        self.tablero = tablero
        self.agente = agente
        self.TAMANO_CELDA = TAMANO_CELDA
        self.colores = {
            0: (128, 128, 128),  # Mountain (Grey)
            1: (139, 69, 19),    # Earth (Brown)
            2: (0, 0, 255),      # Water (Blue)
            3: (255, 223, 186),  # Sand (Light Brown)
            4: (0, 128, 0),      # Forest (Green)
            5: (0, 128, 128),    # Swamp (Teal)
            6: (255, 255, 255),  # Snow (White)
        }

    def dibujar_mapa(self, ventana):
        for fila, fila_valores in enumerate(self.tablero.board_data):
            for columna, celda in enumerate(fila_valores):
                x = columna * self.TAMANO_CELDA
                y = fila * self.TAMANO_CELDA

                # Determine the color based on the cell's value
                value = celda[0]  # Assuming that the value is the first element of the cell's data
                discovered = celda[2]  # Assuming that the discovery status is the third element of the cell's data

                if discovered == "D":
                    color = self.colores.get(value, (255, 255, 255))  # Use the color associated with the value
                else:
                    color = (0, 0, 0)  # Set the color to black for undiscovered cells

                pygame.draw.rect(ventana, color, (x, y, self.TAMANO_CELDA, self.TAMANO_CELDA))
