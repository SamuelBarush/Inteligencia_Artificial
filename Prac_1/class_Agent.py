from class_Map import Board

class Agent:
    def __init__(self,tablero):
        self.tablero = tablero
        self.pos_actual = list(getattr(tablero , "board_init"))
        self.value = self.tablero.get_cell_value(self.pos_actual)
        self.value[2] = "X"
        tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],self.value)
        self.cost_counter = int()
   


    def mover_izq(self):
        
        aux_poz_iz1 = self.tablero.get_cell_value ((self.pos_actual[0]-1,self.pos_actual[1]) )


        if (self.pos_actual[0] ) == 0:
            print("No se puede mover a la izquierda")
            return
        elif (aux_poz_iz1[0] == 1): # hay muro
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.cost_counter += aux_poz_iz1[1] 
            self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
            self.pos_actual[0] += -1  
            self.set_pos_actual() 
            self.sensor_knowledge()
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
            self.cost_counter += aux_poz_der[1] 
            self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
            self.pos_actual[0] += 1
            self.set_pos_actual() 
            self.sensor_knowledge()
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
            self.cost_counter += aux_poz_arr[1] 
            self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
            self.pos_actual[1] += -1
            self.set_pos_actual() 
            self.sensor_knowledge()
        else:
            print("No se puede mover a la arriba, hay obstaculo")
            return 

        
    def mover_abajo(self):


        aux_poz_abj = self.tablero.get_cell_value ((self.pos_actual[0],self.pos_actual[1]+1) )

        if (self.pos_actual[1] ) == 14:
            print("No se puede mover abajo")
            return
        elif (aux_poz_abj[0] == 1): #no hay muro
            value = self.tablero.get_cell_value(self.pos_actual) 
            value[2] = 1
            self.cost_counter += aux_poz_abj[1] 
            self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],value)
            self.pos_actual[1] += 1
            self.set_pos_actual()
            self.sensor_knowledge()
        else:
            print("No se puede mover a la abajo, hay obstaculo")
            return 

    def sensor_knowledge(self):
        count = 0

        # Check the cell above
        mov_arriba = self.pos_actual[1] - 1
        aux = self.tablero.get_cell_value((self.pos_actual[0], mov_arriba))
        if aux is not None:
            if aux[2] == 1:
                print("Camino anteriormente descubierto")
            else:
                aux[2] = "D"
                self.tablero.update_cel_values(self.pos_actual[0], mov_arriba, aux)

        # Check the cell below
        mov_abajo = self.pos_actual[1] + 1
        aux_b = self.tablero.get_cell_value((self.pos_actual[0], mov_abajo))
        if aux_b is not None:
            if aux_b[2] == 1:
                print("Camino anteriormente descubierto")
            else:
                aux_b[2] = "D"
                self.tablero.update_cel_values(self.pos_actual[0], mov_abajo, aux_b)

        # Check the cell to the right
        mov_der = self.pos_actual[0] + 1
        aux_c = self.tablero.get_cell_value((mov_der, self.pos_actual[1]))
        if aux_c is not None:
            if aux_c[2] == 1:
                print("Camino anteriormente descubierto")
            else:
                aux_c[2] = "D"
                self.tablero.update_cel_values(mov_der, self.pos_actual[1], aux_c)

        # Check the cell to the left
        mov_izq = self.pos_actual[0] - 1
        aux_d = self.tablero.get_cell_value((mov_izq, self.pos_actual[1]))
        if aux_d is not None:
            if aux_d[2] == 1:
                print("Camino anteriormente descubierto")
            else:
                aux_d[2] = "D"
                self.tablero.update_cel_values(mov_izq, self.pos_actual[1], aux_d)

    def show_pos_actual(self):
        print(self.pos_actual)
        
    def pos_actual(self):
        return self.pos_actual
    
    
    def set_pos_actual(self):
        aux = self.tablero.get_cell_value(self.pos_actual)
        aux[2] = "X"
        self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],aux)

    def set_cost_value(self):
        for i in range(14):
            for j in range(14):
                aux = self.tablero.get_cell_value((i, j))
                print(f"Current aux for ({i}, {j}): {aux}")
                if aux is not None:
                    if aux[0] == 0:
                        aux[1] = self.mountain
                    if aux[0] == 1:
                        aux[1] = self.earth
                    if aux[0] == 2:
                        aux[1] = self.water
                    if aux[1] == 3:
                        aux[1] = self.sand
                    if aux[0] == 4:
                        aux[1] = self.forest
                    if aux[1] == 5:
                        aux[1] = self.swamp
                    if aux[1] == 6:
                        aux[1] = self.snow
                    print(aux)
                    self.tablero.update_cel_values(i, j, aux)


                else:
                    # Handle the case where get_cell_value returns None for (i, j)
                    print(f"Cell ({i}, {j}) is None, skipping...")
    
    def show_current_cost(self):
        print("the current cost is: {}".format(self.cost_counter))

class Monkey(Agent):
    def __init__(self, tablero):

        super().__init__(tablero)
        self.mountain = 1
        self.earth = 2
        self.water = 4
        self.sand = 3
        self.forest = 1
        self.swamp = 5
        self.snow = 5
        self.set_cost_value()


class Human (Agent):
    def __init__(self, tablero):
        super().__init__(tablero)
        self.mountain= 0
        self.earth= 1
        self.water=2
        self.sand= 3
        self.forest= 4
        self.swamp = 5
        self.snow = 0
        self.set_cost_value()
    



class Octopus (Agent):
    def __init__(self, tablero):
        super().__init__(tablero)
        self.mountain= 0
        self.earth= 2
        self.water=4
        self.sand= 3
        self.forest= 1
        self.swamp = 5
        self.snow = 0
        self.set_cost_value()

class Sasquatch (Agent):
    def __init__(self, tablero):
        super().__init__(tablero)
        self.mountain= 15
        self.earth= 2
        self.water=0
        self.sand= 3
        self.forest= 1
        self.swamp = 5
        self.snow = 3
        self.set_cost_value()
