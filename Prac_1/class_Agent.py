from class_Map import Board

class Agent:
    def __init__(self, tablero):
        self.tablero = Board("Prac_1/board1.txt")
        self.pos_actual 


    def mover_izq(self,pos_actual):
        print(self.tablero.get_cell_value(pos_actual))
        value = self.tablero.get_cell_value(pos_actual) 
        value[2] = 1
        self.tablero.update_cel_values(value)
        pos_actual[0] += -1 
        

    def show_pos_actual(self):
        print(self.pos_actual)