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
        # Get the cell to the left
        aux_poz_iz1 = self.tablero.get_cell_value((self.pos_actual[0] - 1, self.pos_actual[1]))

        # Check if the agent is at the leftmost boundary
        if self.pos_actual[0] == 0:
            print("No se puede mover a la izquierda")
            return

        # Check if the cell to the left is a valid path (value other than 0)
        if aux_poz_iz1 is not None and aux_poz_iz1[0] != 0:
            # Mark the current cell as visited
            value = self.tablero.get_cell_value(self.pos_actual)
            value[2] = "D"
            self.tablero.update_cel_values(self.pos_actual[0], self.pos_actual[1], value)

            # Update the agent's position
            self.pos_actual[0] -= 1
            self.draw_pos_actual()

            # Update the agent's knowledge
            self.sensor_knowledge()
        else:
            print("No se puede mover a la izquierda, no hay un camino válido")
            return
  
    def mover_der(self):
        # Get the cell to the right
        aux_poz_der = self.tablero.get_cell_value((self.pos_actual[0] + 1, self.pos_actual[1]))

        # Check if the agent is at the rightmost boundary
        if self.pos_actual[0] == 14:
            print("No se puede mover a la derecha")
            return

        # Check if the cell to the right is a valid path (value other than 0)
        if aux_poz_der is not None and aux_poz_der[0] != 0:
            # Mark the current cell as visited
            value = self.tablero.get_cell_value(self.pos_actual)
            value[2] = "D"
            self.tablero.update_cel_values(self.pos_actual[0], self.pos_actual[1], value)

            # Update the agent's position
            self.pos_actual[0] += 1
            self.draw_pos_actual()

            # Update the agent's knowledge
            self.sensor_knowledge()
        else:
            print("No se puede mover a la derecha, no hay un camino válido")
            return

    def mover_arriba(self):
        # Get the cell above
        aux_poz_arr = self.tablero.get_cell_value((self.pos_actual[0], self.pos_actual[1] - 1))

        # Check if the agent is at the topmost boundary
        if self.pos_actual[1] == 0:
            print("No se puede mover arriba")
            return

        # Check if the cell above is a valid path (value other than 0)
        if aux_poz_arr is not None and aux_poz_arr[0] != 0:
            # Mark the current cell as visited
            value = self.tablero.get_cell_value(self.pos_actual)
            value[2] = "D"
            self.tablero.update_cel_values(self.pos_actual[0], self.pos_actual[1], value)

            # Update the agent's position
            self.pos_actual[1] -= 1
            self.draw_pos_actual()

            # Update the agent's knowledge
            self.sensor_knowledge()
        else:
            print("No se puede mover arriba, no hay un camino válido")
            return

    def mover_abajo(self):
        # Get the cell below
        aux_poz_abj = self.tablero.get_cell_value((self.pos_actual[0], self.pos_actual[1] + 1))

        # Check if the agent is at the bottommost boundary
        if self.pos_actual[1] == 14:
            print("No se puede mover abajo")
            return

        # Check if the cell below is a valid path (value other than 0)
        if aux_poz_abj is not None and aux_poz_abj[0] != 0:
            # Mark the current cell as visited
            value = self.tablero.get_cell_value(self.pos_actual)
            value[2] = "D"
            self.tablero.update_cel_values(self.pos_actual[0], self.pos_actual[1], value)

            # Update the agent's position
            self.pos_actual[1] += 1
            self.draw_pos_actual()

            # Update the agent's knowledge
            self.sensor_knowledge()
        else:
            print("No se puede mover abajo, no hay un camino válido")
            return

    def sensor_knowledge(self):
        # Check the cell above
        mov_arriba = self.pos_actual[1] - 1
        aux = self.tablero.get_cell_value((self.pos_actual[0], mov_arriba))
        if aux is not None:
            if aux[2] != "D":
                aux[2] = "D"
                self.tablero.update_cel_values(self.pos_actual[0], mov_arriba, aux)

        # Check the cell below
        mov_abajo = self.pos_actual[1] + 1
        aux_b = self.tablero.get_cell_value((self.pos_actual[0], mov_abajo))
        if aux_b is not None:
            if aux_b[2] != "D":
                aux_b[2] = "D"
                self.tablero.update_cel_values(self.pos_actual[0], mov_abajo, aux_b)

        # Check the cell to the right
        mov_der = self.pos_actual[0] + 1
        aux_c = self.tablero.get_cell_value((mov_der, self.pos_actual[1]))
        if aux_c is not None:
            if aux_c[2] != "D":
                aux_c[2] = "D"
                self.tablero.update_cel_values(mov_der, self.pos_actual[1], aux_c)

        # Check the cell to the left
        mov_izq = self.pos_actual[0] - 1
        aux_d = self.tablero.get_cell_value((mov_izq, self.pos_actual[1]))
        if aux_d is not None:
            if aux_d[2] != "D":
                aux_d[2] = "D"
                self.tablero.update_cel_values(mov_izq, self.pos_actual[1], aux_d)

    def show_pos_actual(self):
        print(self.pos_actual)
        
    def pos_actual(self):
        return self.pos_actual
    
    def set_pos_actual(self,pos):
        
        self.pos_actual = pos
        self.sensor_knowledge()
        
    def draw_pos_actual(self):
        aux = self.tablero.get_cell_value(self.pos_actual)
        aux[2] = "X"
        self.tablero.update_cel_values(self.pos_actual[0],self.pos_actual[1],aux)

    def set_cost_value(self):
        for i in range(14):
            for j in range(14):
                aux = self.tablero.get_cell_value((i, j))

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
                    """
                    if aux[1] == 5:
                        aux[1] = self.swamp
                    if aux[1] == 6:
                        aux[1] = self.snow
                    """
                    #print(aux)
                    self.tablero.update_cel_values(i, j, aux)

                else:
                    # Handle the case where get_cell_value returns None for (i, j)
                    print(f"Cell ({i}, {j}) is None, skipping...")
    
    def show_current_cost(self):
        print("the current cost is: {}".format(self.cost_counter))

    def get_cost_values(self):
        # Define and return the cost values based on the agent's type
        cost_values = {
            0: self.mountain,
            1: self.forest,
            2: self.water,
            3: self.sand,
            4: self.earth,
            # Add more cost values as needed for your agent type
        }
        return cost_values

class Human(Agent):
    def __init__(self, tablero):
        super().__init__(tablero)
        self.mountain = 0
        self.earth = 1
        self.water = 2
        self.sand = 3
        self.forest = 4
        self.set_cost_value()


class Octopus (Agent):
    def __init__(self, tablero):
        super().__init__(tablero)
        self.mountain= 0
        self.earth= 4
        self.water=1
        self.sand= 0
        self.forest= 3
        self.set_cost_value()



"""
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

"""


