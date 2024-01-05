import statistics
import numpy as np
from math import sqrt

class ERROR:
    def __init__(self, data,clases) -> None:
        self.data = data
        self.clases = self.contar(clases)

    def contar(self,clases):
        counts = [0] * clases  # Inicializar una lista para contar las instancias de cada clase

        for i in range(len(self.data)):
            clase = int(self.data[i][0][0])
            counts[clase - 1] += 1

        return counts

    def porcentaje(self):
        total = sum(self.clases)
        porcentajes = [(count / total) * 100 for count in self.clases]
        return porcentajes
    
    def vacios(self,clases):
        count = 0
        num_atributos = len(self.data[0])  # Obtener el número de atributos
        
        # Crear listas dinámicas para almacenar los datos de cada clase
        datos_clase = [[0] * num_atributos for _ in range(clases)]
        
        for i in range(len(self.data)):
            for j in range(num_atributos):
                if self.data[i][j][0] == '0':
                    count += 1
                    print(f"El dato vacío es: {self.data[i][j]} de la fila {i} y columna {j}")
            
            clase = int(self.data[i][0][0])
            for k in range(1, num_atributos):
                if self.data[i][k][0] == '0':
                    datos_clase[clase - 1][k] += 1

        # Imprimir resultados de datos vacíos por clase
        for clase, datos in enumerate(datos_clase, 1):
            print(f"Datos vacíos en la clase {clase}: {datos}")

        return count
    
    def min(self):
        minimo = []
        for i in range (1,len(self.data[0])):   #No poner 0 en la fila 0
            minimo.append(self.data[0][i])      #Hay un bug
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
        normal = []
        for i in range(len(self.data)):
            vector = []
            sum_of_components = 0
            vector.append(self.data[i][0])
            for j in range(1 , len(self.data[i])):
                component = pow(float(self.data[i][j][0]), 2)  # You missed the exponent value here, so I added 2
                sum_of_components += component
            norm = sqrt(sum_of_components)

            for k in range(1 , len(self.data[i])):
                sub_vector = [0, 0, 0]
                new_component = float(self.data[i][k][0]) / norm
                sub_vector[0] = new_component
                sub_vector[1] = self.data[i][k][1]
                sub_vector[2] = self.data[i][k][2]
                vector.append(tuple(sub_vector))

            normal.append(vector)

        return normal
    

    def desviacion_estandar(self,clase):
        desviacion = []
        for i in range (1,len(self.data[0])):
            aux = []
            for j in range (len(self.data)):
                if (int(self.data[j][0][0]) == clase):
                    aux.append(float(self.data[j][i][0]))
            desviacion.append(statistics.stdev(aux))
        return desviacion
    
    def media(self,clase):
        media = []
        for i in range (1,len(self.data[0])):
            aux = []
            for j in range (len(self.data)):
                if (int(self.data[j][0][0]) == clase):
                    aux.append(float(self.data[j][i][0]))
            media.append(statistics.mean(aux))
        return media
    
    def atipicos(self):
        pass
            
    def eliminar_fila(self,fila):
        if (fila > len(self.data)):
            print("No existe esa fila")
            return self.data
        self.data.pop(fila)
        return self.data

    def eliminar_columna(self,columna):
        if (columna == 0):
            print("No se puede eliminar la columna CLASE")
            return self.data
        if (columna > len(self.data[0])):
            print("No existe esa columna")
            return self.data
        for i in range (len(self.data)):
            self.data[i].pop(columna)
        return self.data
    
    def detect_outliers_Zscore(self,data):
       # Transponer la lista para tener columnas en lugar de filas
        data_transposed = np.array(data).T.tolist()

        # Calcular la media y la desviación estándar por columna
        for col_num, column in enumerate(data_transposed):
            mean = np.mean(column)
            std_dev = np.std(column)
            outliers = []
            
            # Detectar valores atípicos utilizando Z-score
            for i, value in enumerate(column):
                z_score = (value - mean) / std_dev
                if abs(z_score) > 2.75:  # Umbral de 3 para detectar valores atípicos
                    outliers.append((i, value))
            print(f"Atributo {col_num + 1}: Media = {mean}, Desviación estándar = {std_dev}")
            print(f"Valores atípicos: {outliers}\n")

    def data_to_list(self):
        data = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[i])):
                row.append(float(self.data[i][j][0]))
            data.append(row)
        return data