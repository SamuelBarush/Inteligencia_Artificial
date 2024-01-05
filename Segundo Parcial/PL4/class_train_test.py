from class_erros import ERROR
import numpy as np

class TrainTest:

    def __init__(self, data, porcentaje_aprendizaje) -> None:
        self.data = data
        self.porcentaje_aprendizaje = porcentaje_aprendizaje
        self.contador_clases = ERROR(data,3)

    def conjunto_aprendizaje(self):
        #OBtener las clases y la cantidad de muestras para cada clase:
        clases = len(self.contador_clases.clases)
        muestras = self.contador_clases.clases
        
        muestras_entrenamiento = [] * clases
        muestras_prueba = [] * clases

        #OBtener el numero de muestras para el conjunto de aprendizaje:
        for i in range(clases):
            muestras_entrenamiento.append(int((muestras[i] * self.porcentaje_aprendizaje)/100))
            muestras_prueba.append(muestras[i] - muestras_entrenamiento[i])
            #print(f"Clase {i+1}: {muestras_entrenamiento[i]} muestras para aprendizaje y {muestras_prueba[i]} muestras para prueba")

        #Obtener los subconjuntos de aprendizaje y prueba por clase:
        conjunto_aprendizaje = []
        conjunto_prueba = []

        for i in range(clases):
            conjunto_aprendizaje.append([] * muestras_entrenamiento[i])
            conjunto_prueba.append([] * muestras_prueba[i])
            for j in range(len(self.data)):
                if (int(self.data[j][0][0]) == i+1):
                    if (len(conjunto_aprendizaje[i]) < muestras_entrenamiento[i]):
                        conjunto_aprendizaje[i].append(self.data[j])
                    else:
                        conjunto_prueba[i].append(self.data[j])

        return conjunto_prueba
    

