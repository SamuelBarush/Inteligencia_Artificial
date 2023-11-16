import pygame

class Rend:
    def __init__(self, board1 , board2, TAMANO_CELDA):
        self.board1 = board1
        self.board2 = board2
        self.TAMANO_CELDA = TAMANO_CELDA
        self.colores = {
            0: (128, 128, 128),  # Mountain (Grey)
            1: (139, 69, 19),    # Earth (Brown)
            2: (0, 0, 255),      # Water (Blue)
            3: (255, 223, 186),  # Sand (Light Brown)
            4: (0, 128, 0),      # Forest (Green)
        }

    def dibujar_mapa(self, ventana):
        combined_map = self.combine_maps()
        for fila, fila_valores in enumerate(combined_map):
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

                # Display x and y positions at the top left corner of each cell
                font = pygame.font.Font(None, 12)  # You can adjust the font size as needed
                text = font.render(f'{x//self.TAMANO_CELDA} {y//self.TAMANO_CELDA}', True, (0, 0, 0))  # Black text
                ventana.blit(text, (x, y))
                
    def combine_maps(self):
        combined_map = []
        rows1, rows2 = len(self.board1.board_data), len(self.board2.board_data)
        cols1, cols2 = len(self.board1.board_data[0]), len(self.board2.board_data[0])

        max_rows = max(rows1, rows2)
        max_cols = max(cols1, cols2)

        for row in range(max_rows):
            combined_row = []
            for col in range(max_cols):
                cell1 = self.get_cell_data(self.board1, row, col)
                cell2 = self.get_cell_data(self.board2, row, col)
                combined_cell = self.combine_cells(cell1, cell2)
                combined_row.append(combined_cell)
            combined_map.append(combined_row)

        return combined_map

    def get_cell_data(self, board, row, col):
        if 0 <= row < len(board.board_data) and 0 <= col < len(board.board_data[0]):
            return board.board_data[row][col]
        else:
            # Return a default cell data for out-of-bounds positions
            return [0, 0, 0, '']

    def combine_cells(self, cell1, cell2):
     
        if cell1[2] == 'D':
            return cell1
        else:
            return cell2