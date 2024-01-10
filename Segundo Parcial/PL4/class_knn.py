import math
import random
import numpy as np

class KNN:
    def __init__(self, k=3, distance_metric='euclidean'):
        self.k = k
        self.data = []  # Aquí se almacenarán los datos de entrenamiento
        self.labels = []  # Aquí se almacenarán las etiquetas correspondientes
        self.distance_metric = distance_metric  # Tipo de métrica de distancia

    def fit(self, X_train):
        self.data = self.get_data_as_list(X_train)  # Almacena los vectores de características
        self.labels = self.get_labels(X_train)  # Corregir para acceder al valor correcto de la etiqueta

    def predict(self, X_test):
        predictions = []
        for x in X_test:
            x_values = self.parse_vector(x)
            distances = []
            for i, data_point in enumerate(self.data):
                dist = self.calculate_distance(x_values, data_point)
                distances.append((dist, self.labels[i]))  # Tupla de (distancia, etiqueta)
            #print(distances)    
            distances.sort(key=lambda x: x[0])  # Ordenar distancias de menor a mayor
            k_nearest = distances[:self.k]  # Obtener los k vecinos más cercanos
            k_labels = [label for (_, label) in k_nearest]

            # Votación para determinar la etiqueta
            prediction = max(set(k_labels), key=k_labels.count)

            # Mostrar la votación
            #print(f"Para el punto, la votación fue: {k_labels}")

            predictions.append(int(prediction))
        return predictions

    def calculate_distance(self, x1, x2):
        if self.distance_metric == 'manhattan':
            return self.manhattan_distance(x1, x2)
        elif self.distance_metric == 'euclidean':
            return self.euclidean_distance(x1, x2)
        else:
            raise ValueError("Métrica de distancia no reconocida.")

    def euclidean_distance(self, x1, x2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(x1, x2)))

    def manhattan_distance(self, x1, x2):
        return sum(abs(a - b) for a, b in zip(x1, x2))

    def parse_vector(self, vector):
        parsed_values = []
        #print(vector)
        for value, data_type, _ in vector:
            
            if data_type == 'int':
                parsed_values.append(int(value))
            elif data_type == 'float':
                parsed_values.append(float(value))

        return parsed_values

    def show_training_labels(self):
        print(self.labels)
    
    def get_labels(self,data):
        return [x[0][0][0] for x in data]
    
    def get_data_as_list(self,data):
        return [self.parse_vector(x[1:]) for x in data]

    def bootstrap(self, X, num_samples):
            predictions = []
            for _ in range(num_samples):
                # Muestreo con reemplazo para crear una muestra bootstrap
                indices = [random.randint(0, len(X) - 1) for _ in range(len(X))]
                X_bootstrap = [X[i] for i in indices]
               
                #print(X_bootstrap)
                #print(y_bootstrap)
                # Entrenar el modelo con la muestra bootstrap
                self.fit(X_bootstrap)

                # Hacer predicciones con el modelo ajustado utilizando nuevas muestras de prueba
                predictions.append(self.predict(X_bootstrap))

            return predictions




    def calcular_eficiencia(self,y_true, y_pred):
        # Función para calcular la eficiencia
        return np.mean(y_true == y_pred) * 100

    def calcular_error(self,y_true, y_pred):
        # Función para calcular el error
        return 100 - self.calcular_eficiencia(y_true, y_pred)
    
    def Train_Test(self, data, porcentaje_entrenamiento):
        """
        Realiza el entrenamiento y prueba del algoritmo KNN.

        Args:
            data (list): Lista de datos de entrenamiento y prueba.
            porcentaje_entrenamiento (int): Porcentaje de datos a utilizar para entrenamiento.

        Returns:
            list: Lista de resultados de entrenamiento y prueba.
        """
        train = list()  # Lista para almacenar los resultados de entrenamiento y prueba
        conjuntos = int((len(data)*porcentaje_entrenamiento)/100)  # Calcular el número de conjuntos de datos de entrenamiento
        for _ in range(conjuntos):
            # Seleccionar índices aleatorios para crear un conjunto de datos de entrenamiento
            # Crear una lista de índices aleatorios se hace para cada elemento que es una secuencia de 0 hasta el número de elementos del conjunto de datos
            indice = [random.randint(0, len(data) - 1) for _ in range(len(data))] 
            train_TT = [data[i] for i in indice]  # Crear el conjunto de datos de entrenamiento

            self.fit(train_TT)  # Realizar el entrenamiento del algoritmo KNN con el conjunto de datos de entrenamiento

            # Realizar predicciones
            y_true = [item[0][0] for item in train_TT]  # Obtener las etiquetas verdaderas del conjunto de datos de entrenamiento
            y_pred = self.predict(train_TT)  # Realizar predicciones con el conjunto de datos de entrenamiento

            class_prediction = list(zip(y_true, y_pred))  # Combina los elementos en las mismas posiciones de las listas y crea una lista de tuplas
            train.append(class_prediction)  # Agregar los resultados de entrenamiento y prueba a la lista

        return train  # Devolver la lista de resultados de entrenamiento y prueba

    def bootstrap_(self, X, num_samples):
        boostraps =  list()

        for _ in range(num_samples):
            # Muestreo con reemplazo para crear una muestra bootstrap
            indices = [random.randint(0, len(X) - 1) for _ in range(len(X))]
            X_bootstrap = [X[i] for i in indices]
            
            # Entrenar el modelo con la muestra bootstrap
            self.fit(X_bootstrap)

            # Hacer predicciones con el modelo ajustado utilizando nuevas muestras de prueba
            y_true_bootstrap = [item[0][0] for item in X_bootstrap]  # Suponiendo que el primer elemento es la clase verdadera
            y_pred_bootstrap = self.predict(X_bootstrap)

            class_prediction = list(zip(y_true_bootstrap,y_pred_bootstrap)) # [(clase real, predicción por el bootstrapp),(...)]
            boostraps.append(class_prediction)
        return boostraps


    def efic_x_group(self, resultados_bootstrap):
        eficiencia_por_grupo = []
        error_por_grupo = []

        for grupo_predicciones in resultados_bootstrap:
            predicciones_por_clase = {}
            total_predicciones = len(grupo_predicciones)
            
            for clase_real, prediccion in grupo_predicciones:
                clase_real = str(clase_real)
                
                if clase_real not in predicciones_por_clase:
                    predicciones_por_clase[clase_real] = {'correctas': 0, 'total': 0}
                
                predicciones_por_clase[clase_real]['total'] += 1
                
                if clase_real == str(prediccion):
                    predicciones_por_clase[clase_real]['correctas'] += 1

            # Calcular eficiencia y error para cada clase en el grupo
            eficiencia_grupo = {}
            error_grupo = {}
            
            for clase, valores in predicciones_por_clase.items():
                if valores['total'] > 0:
                    eficiencia = (valores['correctas'] / valores['total']) * 100
                    error = 100 - eficiencia
                else:
                    eficiencia = 0.0
                    error = 100.0
                
                eficiencia_grupo[clase] = eficiencia
                error_grupo[clase] = error

            eficiencia_por_grupo.append(eficiencia_grupo)
            error_por_grupo.append(error_grupo)

        return eficiencia_por_grupo, error_por_grupo



    def efic_x_class(self,resultados_bootstrap):
        clases = set()
        predicciones_por_clase = {}

        # Obtener la lista única de clases
        for muestra in resultados_bootstrap:
            for clase_real, _ in muestra:
                clases.add(clase_real)

        # Inicializar el contador de predicciones para cada clase
        for clase in clases:
            predicciones_por_clase[clase] = {'correctas': 0, 'total': 0}

        # Contar predicciones correctas para cada clase
        for muestra in resultados_bootstrap:
            for clase_real, prediccion in muestra:
                predicciones_por_clase[clase_real]['total'] += 1
                if str(clase_real) == str(prediccion):
                    predicciones_por_clase[clase_real]['correctas'] += 1

        # Calcular el porcentaje de eficiencia para cada clase
        eficiencia_por_clase = {}
        for clase, valores in predicciones_por_clase.items():
            if valores['total'] > 0:
                eficiencia = (valores['correctas'] / valores['total']) * 100
            else:
                eficiencia = 0.0
            eficiencia_por_clase[str(clase)] = eficiencia

        return eficiencia_por_clase



    def calcular_eficiencia_error_general(self,resultados):
        eficiencias, errores = resultados
        eficiencias_generales = []
        errores_generales = []

        for eficiencia_grupo, error_grupo in zip(eficiencias, errores):
            eficiencia_promedio = np.mean(list(eficiencia_grupo.values()))
            error_promedio = np.mean(list(error_grupo.values()))

            eficiencias_generales.append(eficiencia_promedio)
            errores_generales.append(error_promedio)

        eficiencia_promedio_general = np.mean(eficiencias_generales)
        error_promedio_general = np.mean(errores_generales)

        desviacion_eficiencia = np.std(eficiencias_generales)
        desviacion_error = np.std(errores_generales)

        return {
            'eficiencia_promedio_general': eficiencia_promedio_general,
            'error_promedio_general': error_promedio_general,
            'desviacion_eficiencia': desviacion_eficiencia,
            'desviacion_error': desviacion_error
        }