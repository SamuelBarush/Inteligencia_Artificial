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

    def bootstrap_(self, X, num_samples):
        predictions = []
        eficiencias_por_grupo = {}
        errores_por_grupo = {}

        for _ in range(num_samples):
            # Muestreo con reemplazo para crear una muestra bootstrap
            indices = [random.randint(0, len(X) - 1) for _ in range(len(X))]
            X_bootstrap = [X[i] for i in indices]
            
            # Entrenar el modelo con la muestra bootstrap
            self.fit(X_bootstrap)

            # Hacer predicciones con el modelo ajustado utilizando nuevas muestras de prueba
            y_true_bootstrap = [item[0] for item in X_bootstrap]  # Suponiendo que el primer elemento es la clase verdadera
            y_pred_bootstrap = self.predict(X_bootstrap)

            # Agrupar predicciones y valores reales por clase/grupo
            for true, pred in zip(y_true_bootstrap, y_pred_bootstrap):
                if true not in eficiencias_por_grupo:
                    eficiencias_por_grupo[true] = []
                    errores_por_grupo[true] = []
                
                eficiencia = self.calcular_eficiencia([true], [pred])
                error = self.calcular_error([true], [pred])

                eficiencias_por_grupo[true].append(eficiencia)
                errores_por_grupo[true].append(error)
            
            # Guardar las predicciones para este bootstrap
            predictions.append(y_pred_bootstrap)

        # Calcular eficiencia y error generales y sus desviaciones estándar
        predictions = np.array(predictions).astype(int)
        eficiencia_general = self.calcular_eficiencia(y_true_bootstrap, np.mean(predictions, axis=0))
        error_general = self.calcular_error(y_true_bootstrap, np.mean(predictions, axis=0))

        desviacion_eficiencia = np.std([self.calcular_eficiencia([true]*len(eficiencias_por_grupo[true]), eficiencias_por_grupo[true]) for true in eficiencias_por_grupo])
        desviacion_error = np.std([self.calcular_error([true]*len(errores_por_grupo[true]), errores_por_grupo[true]) for true in errores_por_grupo])

        return eficiencia_general, error_general, desviacion_eficiencia, desviacion_error
