import math
class MIN:
    def __init__(self, distance_metric='euclidean'):
        self.data = []  # Aquí se almacenarán los datos de entrenamiento
        self.labels = []  # Aquí se almacenarán las etiquetas correspondientes
        self.distance_metric = distance_metric  # Tipo de métrica de distancia

    def fit(self, X_train):
        self.data = [self.parse_vector(x[1:]) for x in X_train]  # Almacena los vectores de características
        self.labels = [x[0][0][0] for x in X_train]  # Corregir para acceder al valor correcto de la etiqueta

    def predict(self, X_test):
        predictions = []
        for x in X_test:
            x_values = self.parse_vector(x)
            distances = []
            for i, data_point in enumerate(self.data):
                dist = self.calculate_distance(x_values, data_point)
                distances.append((dist, self.labels[i]))  # Tupla de (distancia, etiqueta)
            distances.sort(key=lambda x: x[0])  # Ordenar distancias de menor a mayor
            
            # Encuentra la clase del centroide más cercano
            prediction = min(distances)[1]
            
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
