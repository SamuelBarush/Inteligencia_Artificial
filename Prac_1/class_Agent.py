from class_Map import Board

class Agent:
    def __init__(self,pos_inicial,tablero):
        self.tablero = tablero
        self.pos_actual = pos_inicial
        self.value = self.tablero.get_cell_value(self.pos_actual)
        self.value[2] = "X"
        tablero.update_cel_values(self.pos_actual[1],self.pos_actual[0],self.value)

    def mover_izq(self):
        
        if (self.pos_actual[0] ) == 0:
            print("No se puede mover a la izquierda")
            return
        else:
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.tablero.update_cel_values(self.pos_actual[1],self.pos_actual[0],value)
            self.pos_actual[0] += -1  
            self.set_pos_actual()    
        
    def mover_der(self):
        
        if (self.pos_actual[0] ) == 14:
            print("No se puede mover a la derecha")
            return
        else:
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.tablero.update_cel_values(self.pos_actual[1],self.pos_actual[0],value)
            self.pos_actual[0] += 1
            self.set_pos_actual() 
        
    def mover_arriba(self):
        if (self.pos_actual[1] ) == 0:
            print("No se puede mover arriba")
            return
        else:
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.tablero.update_cel_values(self.pos_actual[1],self.pos_actual[0],value)
            self.pos_actual[1] += -1
            self.set_pos_actual() 
        
    def mover_abajo(self):
        if (self.pos_actual[1] ) == 14:
            print("No se puede mover abajo")
            return
        else:
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.tablero.update_cel_values(self.pos_actual[1],self.pos_actual[0],value)
            self.pos_actual[1] += 1
            self.set_pos_actual() 

    def show_pos_actual(self):
        print(self.pos_actual)
        
    def pos_actual(self):
        return self.pos_actual
    
    def set_pos_actual(self):
        aux = self.tablero.get_cell_value(self.pos_actual)
        aux[2] = "X"
        self.tablero.update_cel_values(self.pos_actual[1],self.pos_actual[0],aux)
    