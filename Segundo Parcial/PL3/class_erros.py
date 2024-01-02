class ERROR:
    def __init__(self,data) ->None:
        self.data = data
        self.clase1,self.clase2,self.clase3 = self.contar()

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
        
        for i in range (1,len(datos_clase1)):
            porcentaje1 = (datos_clase1[i]/self.clase1)*100
            print(f"El porcentaje de datos vacios de la clase 1 en el atributo {i} es: {porcentaje1}")
        for i in range (1,len(datos_clase2)):
            porcentaje2 = (datos_clase2[i]/self.clase2)*100
            print(f"El porcentaje de datos vacios de la clase 2 en el atributo {i} es: {porcentaje2}")
        for i in range (1,len(datos_clase3)):
            porcentaje3 = (datos_clase3[i]/self.clase3)*100
            print(f"El porcentaje de datos vacios de la clase 3 en el atributo {i} es: {porcentaje3}")
        return count, datos_clase1, datos_clase2, datos_clase3
    
    def min(self):
        minimo = []
        for i in range (1,len(self.data[0])):
            #if (self.data[0][i][0] != '0'):
            minimo.append(self.data[0][i])
            #else:
            #    minimo.append(self.data[1][i])
            for j in range (len(self.data)):
                if (self.data[j][i] < minimo[i-1]):
                    if (self.data[j][i][0] != '0'):
                        minimo[i-1] = self.data[j][i]
        return minimo
    
    def max(self):
        maximo = []
        for i in range (1,len(self.data[0])):
            maximo.append(self.data[0][i])
            for j in range (len(self.data)):
                if (self.data[j][i] > maximo[i-1]):
                    maximo[i-1] = self.data[j][i]
        return maximo
    
    def normalizar(self):
        maximo = self.max()
        minimo = self.min()
        normal = []
        for i in range (len(self.data)):
            fila = []
            fila.append(self.data[i][0])
            for j in range (1,len(self.data[i])):
                aux = [0,0,0]
                nuevo = (float(self.data[i][j][0]) - float(minimo[j-1][0]))/(float(maximo[j-1][0]) - float(minimo[j-1][0]))
                aux[0] = nuevo
                aux[1] = self.data[i][j][1]
                aux[2] = self.data[i][j][2]
                fila.append(tuple(aux))
            normal.append(fila)
        return normal

    # ------------------------ 2 ------------------------
    
    def vacios_2(self):
        count = 0
        datos_clase1 = [0] * len(self.data[0])
        datos_clase2 = [0] * len(self.data[0])
        datos_clase3 = [0] * len(self.data[0])

        for i in range(len(self.data)):
            for j in range(1, len(self.data[i])):  # Comenzamos desde 1 para omitir la clase
                if self.data[i][j][0] == '0':
                    count += 1
                    if self.data[i][0][0] == '1':
                        datos_clase1[j] += 1
                    elif self.data[i][0][0] == '2':
                        datos_clase2[j] += 1
                    elif self.data[i][0][0] == '3':
                        datos_clase3[j] += 1

        for i in range(1, len(self.data[0])):
            print(f"Atributo {i}:")
            print(f"  De  faltan {datos_clase1[i]} ({(datos_clase1[i] / count) * 100}%)")
            print(f"  De  faltan {datos_clase2[i]} ({(datos_clase2[i] / count) * 100}%)")
            print(f"  De  faltan {datos_clase3[i]} ({(datos_clase3[i] / count) * 100}%)")

        return count, datos_clase1, datos_clase2, datos_clase3
    
    