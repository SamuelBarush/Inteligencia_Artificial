import math

class KNN:
    def __init__(self, k=3):
        self.k = k
        self.data = []  # Aquí se almacenarán los datos de entrenamiento
        self.labels = []  # Aquí se almacenarán las etiquetas correspondientes

    def fit(self, X_train):
        self.data = [self.parse_vector(x[1:]) for x in X_train]  # Almacena los vectores de características
        self.labels = [x[0][0] for x in X_train]  # Almacena las etiquetas

    def predict(self, X_test):
        predictions = []
        for x in X_test:
            x_values = self.parse_vector(x)
            distances = []
            for i, data_point in enumerate(self.data):
                dist = self.euclidean_distance(x_values, data_point)
                distances.append((dist, self.labels[i]))  # Tupla de (distancia, etiqueta)
            distances.sort(key=lambda x: x[0])  # Ordenar distancias de menor a mayor
            k_nearest = distances[:self.k]  # Obtener los k vecinos más cercanos
            k_labels = [label for (_, label) in k_nearest]
            prediction = max(set(k_labels), key=k_labels.count)  # Votación para determinar la etiqueta
            predictions.append(prediction)
        return predictions

    def euclidean_distance(self, x1, x2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(x1, x2)))

    def parse_vector(self, vector):
        parsed_values = []
        for value, data_type, _ in vector:
            if data_type == 'int':
                parsed_values.append(int(value))
            elif data_type == 'float':
                parsed_values.append(float(value))
        return parsed_values
