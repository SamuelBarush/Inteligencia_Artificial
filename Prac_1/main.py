from class_Map import Board
from class_Agent import Agent
"""
tablero = Board("Prac_1/board1.txt")
tablero.show_board()

tablero.update_cel_values(1, 2, [5, 0, 0]) #pos row, pos col, values
print("UPDATED")
tablero.show_board()

"""
tablero = Board("Prac_1/board1.txt")

agente = Agent([0,0],tablero)
tablero.show_board()
print()
agente.mover_izq()
print()
tablero.show_board()
agente.mover_abajo()
print()
tablero.show_board()


