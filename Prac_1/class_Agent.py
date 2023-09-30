from class_Map import Board

class Agent:
    def __init__(self,pos_actual,tablero):
        self.tablero = tablero
        self.pos_actual = pos_actual

    def mover_izq(self):
        print(self.tablero.get_cell_value(self.pos_actual))
        value = self.tablero.get_cell_value(self.pos_actual) 
        value[2] = 1
        self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
        self.pos_actual[0] += -1 
        
    def mover_der(self):
        print(self.tablero.get_cell_value(self.pos_actual))
        value = self.tablero.get_cell_value(self.pos_actual) 
        value[2] = 1
        self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
        self.pos_actual[0] += 1
        
    def mover_arriba(self):
        print(self.tablero.get_cell_value(self.pos_actual))
        value = self.tablero.get_cell_value(self.pos_actual) 
        value[2] = 1
        self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
        self.pos_actual[1] += -1
        
    def mover_abajo(self):
        print(self.tablero.get_cell_value(self.pos_actual))
        value = self.tablero.get_cell_value(self.pos_actual) 
        value[2] = 1
        self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
        self.pos_actual[1] += 1

    def show_pos_actual(self):
        print(self.pos_actual)