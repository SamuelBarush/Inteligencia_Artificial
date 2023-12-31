class ERROR:
    def __init__(self,data) ->None:
        self.data = data

    def contar(self):
        count = 0
        count1 = 0
        count2 = 0

        for i in range(len(self.data)):
            if self.data[i][0][0] == '1':
                count += 1
            elif self.data[i][0][0] == '2':
                count1 += 1
            elif self.data[i][0][0] == '3':
                count2 += 1
        return count, count1, count2
    
    def porcentaje(self,class1,class2,class3):
        total = class1 + class2 + class3
        porcentaje1 = (class1/total)*100
        porcentaje2 = (class2/total)*100
        porcentaje3 = (class3/total)*100
        return porcentaje1,porcentaje2,porcentaje3
    
    def vacios(self):
        count = 0
        datos_clase1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        datos_clase2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        datos_clase3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j][0] == '0':
                    count += 1
                    print(f"El dato vacio es: {self.data[i][j]} de la fila {i} y columna {j}")
            if (self.data[i][0][0] == '1' ):
                if self.data[i][1][0] == '0':
                    datos_clase1 [1] += 1
                    
                elif self.data[i][2][0] == '0':
                    datos_clase1 [2] += 1
                elif self.data[i][3][0] == '0':
                    datos_clase1 [3] += 1
                elif self.data[i][4][0] == '0':
                    datos_clase1 [4] += 1
                elif self.data[i][5][0] == '0':
                    datos_clase1 [5] += 1
                elif self.data[i][6][0] == '0':
                    datos_clase1 [6] += 1
                elif self.data[i][7][0] == '0':
                    datos_clase1 [7] += 1
                elif self.data[i][8][0] == '0':
                    datos_clase1 [8] += 1
                elif self.data[i][9][0] == '0':
                    datos_clase1 [9] += 1
                elif self.data[i][10][0] == '0':
                    datos_clase1 [10] += 1
                elif self.data[i][11][0] == '0':
                    datos_clase1 [11] += 1
                elif self.data[i][12][0] == '0':
                    datos_clase1 [12] += 1
                elif self.data[i][13][0] == '0':
                    datos_clase1 [13] += 1
            elif (self.data[i][0][0] == '2' ):
                if self.data[i][1][0] == '0':
                    datos_clase2 [1] += 1
                elif self.data[i][2][0] == '0':
                    datos_clase2 [2] += 1
                elif self.data[i][3][0] == '0':
                    datos_clase2 [3] += 1
                elif self.data[i][4][0] == '0':
                    datos_clase2 [4] += 1
                elif self.data[i][5][0] == '0':
                    datos_clase2 [5] += 1
                elif self.data[i][6][0] == '0':
                    datos_clase2 [6] += 1
                elif self.data[i][7][0] == '0':
                    datos_clase2 [7] += 1
                elif self.data[i][8][0] == '0':
                    datos_clase2 [8] += 1
                elif self.data[i][9][0] == '0':
                    datos_clase2 [9] += 1
                elif self.data[i][10][0] == '0':
                    datos_clase2 [10] += 1
                elif self.data[i][11][0] == '0':
                    datos_clase2 [11] += 1
                elif self.data[i][12][0] == '0':
                    datos_clase2 [12] += 1
                elif self.data[i][13][0] == '0':
                    datos_clase2 [13] += 1
            elif (self.data[i][0][0] == '3' ):
                if self.data[i][1][0] == '0':
                    datos_clase3 [1] += 1
                elif self.data[i][2][0] == '0':
                    datos_clase3 [2] += 1
                elif self.data[i][3][0] == '0':
                    datos_clase3 [3] += 1
                elif self.data[i][4][0] == '0':
                    datos_clase3 [4] += 1
                elif self.data[i][5][0] == '0':
                    datos_clase3 [5] += 1
                elif self.data[i][6][0] == '0':
                    datos_clase3 [6] += 1
                elif self.data[i][7][0] == '0':
                    datos_clase3 [7] += 1
                elif self.data[i][8][0] == '0':
                    datos_clase3 [8] += 1
                elif self.data[i][9][0] == '0':
                    datos_clase3 [9] += 1
                elif self.data[i][10][0] == '0':
                    datos_clase3 [10] += 1
                elif self.data[i][11][0] == '0':
                    datos_clase3 [11] += 1
                elif self.data[i][12][0] == '0':
                    datos_clase3 [12] += 1
                elif self.data[i][13][0] == '0':
                    datos_clase3 [13] += 1
        
        return count, datos_clase1, datos_clase2, datos_clase3
    
    