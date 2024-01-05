from class_erros import ERROR
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score, precision_score

class TrainTest:

    def __init__(self, archivo , porcentaje_aprendizaje, model, neighbors) -> None:
        self.data = pd.read_csv(archivo)
        self.porcentaje_aprendizaje = porcentaje_aprendizaje
        
        self.model_name = model.lower()
        self.neighbors = neighbors
        
        self.model = self.__get_model()
        
        #self.contador_clases = ERROR(data,3)
        #self.conjunto_aprendizaje, self.conjunto_prueba = self.conjuntos_aprendizaje()

    def __get_model(self):
        if self.model_name == 'knn':
            return KNeighborsClassifier(n_neighbors=self.neighbors)
        elif self.model_name == 'random_forest':
            return RandomForestClassifier()
        else:
            raise ValueError("Modelo no válido")

    def conjuntos_aprendizaje(self):
        #OBtener las clases y la cantidad de muestras para cada clase:
        clases = len(self.contador_clases.clases)
        muestras = self.contador_clases.clases
        
        muestras_entrenamiento = [] * clases
        muestras_prueba = [] * clases

        #OBtener el numero de muestras para el conjunto de aprendizaje:
        for i in range(clases):
            muestras_entrenamiento.append(int((muestras[i] * self.porcentaje_aprendizaje)/100))
            muestras_prueba.append(muestras[i] - muestras_entrenamiento[i])
            print(f"Clase {i+1}: {muestras_entrenamiento[i]} muestras para aprendizaje y {muestras_prueba[i]} muestras para prueba")

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

        return conjunto_prueba, conjunto_aprendizaje
    
    
    def evaluar(self, Atributo, Clase):
        X = self.data[Atributo].values
        Y = self.data[Clase].values

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=self.porcentaje_aprendizaje, random_state=10)

        model_TT = self.model
        model_TT.fit(X_train, Y_train)

        y_pred = model_TT.predict(X_test)

        accuracy = accuracy_score(Y_test, y_pred)
        error = 1 - accuracy

        efficiency = accuracy * 100
        error_percentage = error * 100

        print(f"Efficiencia: {efficiency}%")
        print(f"Error: {error_percentage}%")

        print("Precision por clase")
        precision_score_per_class = precision_score(Y_test, y_pred, average=None)
        for i in range(len(precision_score_per_class)):
            print(f"Clase {i+1}: {precision_score_per_class[i] * 100:.2f}")

        std_deviation = np.std(precision_score_per_class)
        print(f"Desviacion estandar: {std_deviation * 100:.2f}")
        
