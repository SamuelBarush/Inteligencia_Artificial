from class_Map import Board

class Agent:
    def __init__(self,tablero):
        self.tablero = tablero
        self.pos_actual = list(getattr(tablero , "board_init"))
        self.value = self.tablero.get_cell_value(self.pos_actual)
        self.value[2] = "X"
        tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],self.value)

    def mover_izq(self):
      
        aux_poz_iz1 = self.tablero.get_cell_value ((self.pos_actual[0]-1,self.pos_actual[1]) )
        if (self.pos_actual[0] ) == 0:
            print("No se puede mover a la izquierda")
            return
        elif (aux_poz_iz1[0] == 1): # hay muro
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
            self.pos_actual[0] += -1  
            self.set_pos_actual() 
        else:
            print("No se puede mover a la izquierda, hay obstaculo")
            return 
        
    def mover_der(self):      
        aux_poz_der = self.tablero.get_cell_value ((self.pos_actual[0]+1,self.pos_actual[1]) )

        if (self.pos_actual[0] ) == 14:
            print("No se puede mover a la derecha")
            return
        elif (aux_poz_der[0] == 1): # hay muro
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
            self.pos_actual[0] += 1
            self.set_pos_actual() 
        else:
            print("No se puede mover a la derecha, hay obstaculo")
            return 

    def mover_arriba(self):   
        aux_poz_arr = self.tablero.get_cell_value ((self.pos_actual[0],self.pos_actual[1]-1) )

        if (self.pos_actual[1] ) == 0:
            print("No se puede mover arriba")
            return
        elif (aux_poz_arr[0] == 1): # hay muro
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
            self.pos_actual[1] += -1
            self.set_pos_actual() 
        else:
            print("No se puede mover a la arriba, hay obstaculo")
            return 

        
    def mover_abajo(self):
        aux_poz_abj = self.tablero.get_cell_value ((self.pos_actual[0],self.pos_actual[1]+1) )

        if (self.pos_actual[1] ) == 14:
            print("No se puede mover abajo")
            return
        elif (aux_poz_abj[0] == 1): # hay muro
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
            self.pos_actual[1] += 1
            self.set_pos_actual()
        else:
            print("No se puede mover a la abajo, hay obstaculo")
            return 
            
    def sensor_knowledge(self):
        aux = self.pos_actual
        mov_arriba = self.pos_actual [1] - 1
        aux = self.tablero.get_cell_value((self.pos_actual[0],mov_arriba)) 
        if(aux [2] == 1):
            print("Camino anteriormente descubierto")
        else :
            aux[2] = "D"
            self.tablero.update_cel_values(self.pos_actual[0], mov_arriba,aux)
        

        aux_b = self.pos_actual
        mov_abajo = self.pos_actual [1] + 1
        aux_b = self.tablero.get_cell_value((self.pos_actual[0],mov_abajo))
        if(aux_b [2] == 1):
            print("Camino anteriormente descubierto")
        else :
            aux_b[2] = "D"
            self.tablero.update_cel_values(self.pos_actual[0], mov_abajo,aux_b)

        aux_c = self.pos_actual
        mov_der = self.pos_actual [0] + 1
        aux_c = self.tablero.get_cell_value((mov_der, self.pos_actual[1]))
        if(aux_c [2] == 1):
            print("Camino anteriormente descubierto")
        else :
            aux_c[2] = "D"
            self.tablero.update_cel_values( mov_der,self.pos_actual[1],aux_c)

        aux_d = self.pos_actual
        mov_izq = self.pos_actual [0] - 1
        aux_d = self.tablero.get_cell_value((mov_izq, self.pos_actual[1]))
        if(aux_d [2] == 1):
            print("Camino anteriormente descubierto")
        else :
            aux_d[2] = "D"
            self.tablero.update_cel_values( mov_izq,self.pos_actual[1],aux_d)

    def show_pos_actual(self):
        print(self.pos_actual)
        
    def pos_actual(self):
        return self.pos_actual
    
    def set_pos_actual(self):
        aux = self.tablero.get_cell_value(self.pos_actual)
        aux[2] = "X"
        self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],aux)


    