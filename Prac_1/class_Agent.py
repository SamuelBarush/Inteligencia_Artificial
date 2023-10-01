from class_Map import Board

class Agent:
    def __init__(self,pos_inicial,tablero):
        self.tablero = tablero
        self.pos_actual = pos_inicial
        self.value = self.tablero.get_cell_value(self.pos_actual)
        self.value[2] = "X"
        tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],self.value)

    def mover_izq(self):
        
        if (self.pos_actual[0] ) == 0:
            print("No se puede mover a la izquierda")
            return
        else:
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
            self.pos_actual[0] += -1  
            self.set_pos_actual()    
        
    def mover_der(self):
        
        if (self.pos_actual[0] ) == 14:
            print("No se puede mover a la derecha")
            return
        else:
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
            self.pos_actual[0] += 1
            self.set_pos_actual() 
        
    def mover_arriba(self):
        if (self.pos_actual[1] ) == 0:
            print("No se puede mover arriba")
            return
        else:
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
            self.pos_actual[1] += -1
            self.set_pos_actual() 
        
    def mover_abajo(self):
        if (self.pos_actual[1] ) == 14:
            print("No se puede mover abajo")
            return
        else:
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
            self.pos_actual[1] += 1
            self.set_pos_actual()
            
    def sensor_knowledge(self):
        aux = self.pos_actual
        mov_arriba = self.pos_actual [1] - 1
        aux = self.tablero.get_cell_value((self.pos_actual[0],mov_arriba)) 
        aux[2] = 1
        sen_arr = self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],aux)
        if (sen_arr == 0):
            self.pos_actual[1] = mov_arriba
            self.set_pos_actual()
        return 0
        mov_abajo = self.pos_actual [1] + 1
        sen_abaj = self.tablero.update_cel_values(self.pos_actual[1],self.pos_actual[0],aux)

    def show_pos_actual(self):
        print(self.pos_actual)
        
    def pos_actual(self):
        return self.pos_actual
    
    def set_pos_actual(self):
        aux = self.tablero.get_cell_value(self.pos_actual)
        aux[2] = "X"
        self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],aux)
    