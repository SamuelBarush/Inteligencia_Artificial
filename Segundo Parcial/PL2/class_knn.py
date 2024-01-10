import math

class KNN:
    def __init__(self, k=3, distance_metric='euclidean'):
        self.k = k
        self.data = []  # Aquí se almacenarán los datos de entrenamiento
        self.labels = []  # Aquí se almacenarán las etiquetas correspondientes
        self.distance_metric = distance_metric  # Tipo de métrica de distancia

    def fit(self, X_train):
        self.data = [self.parse_vector(x[1:]) for x in X_train]  # Almacena los vectores de características
        self.labels = [x[0][0][0] for x in X_train]  # Corregir para acceder al valor correcto de la etiqueta

    def predict(self, X_test):
            """
            Realiza la predicción de las etiquetas para un conjunto de datos de prueba utilizando el algoritmo K-Nearest Neighbors (KNN).

            Parámetros:
            - X_test: Una lista de vectores de características de los datos de prueba.

            Retorna:
            - predictions: Una lista de las etiquetas predichas para cada vector de características en X_test.
            """
            predictions = []
            for x in X_test:
                x_values = self.parse_vector(x)
                distances = []
                for i, data_point in enumerate(self.data):
                    dist = self.calculate_distance(x_values, data_point)
                    distances.append((dist, self.labels[i]))  # Tupla de (distancia, etiqueta)
                print(distances)    
                distances.sort(key=lambda x: x[0]) #Esta función se utiliza para determinar el valor que se debe utilizar para ordenar los elementos de la lista. 
                k_nearest = distances[:self.k]  # Obtener los k vecinos más cercanos
                k_labels = [label for (_, label) in k_nearest]

                # Votación para determinar la etiqueta
                prediction = max(set(k_labels), key=k_labels.count)# ordenará la lista distances en función del primer elemento de cada tupla. Esto es útil en este contexto porque distances contiene tuplas de distancias y etiquetas, y queremos ordenar las tuplas por distancia.

                # Mostrar la votación
                print(f"Para el punto, la votación fue: {k_labels}")

                predictions.append(prediction)
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
        for value, data_type, _ in vector:
            if data_type == 'int':
                parsed_values.append(int(value))
            elif data_type == 'float':
                parsed_values.append(float(value))
        return parsed_values

    def get_labels(self):
        print(self.labels)