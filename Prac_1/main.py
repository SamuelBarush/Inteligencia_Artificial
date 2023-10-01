from class_Map import Board
from class_Agent import Agent
from class_Game import Rend
"""
tablero = Board("Prac_1/board1.txt")
tablero.show_board()

tablero.update_cel_values(1, 2, [5, 0, 0]) #pos row, pos col, values
print("UPDATED")
tablero.show_board()

"""
tablero = Board("Prac_1/board1.txt", (1,1), (3,3))

agente = Agent(tablero, )

juego = Rend ( tablero , agente )



