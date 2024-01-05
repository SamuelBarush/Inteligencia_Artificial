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
        return class_prediction


    def efic_x_group(self, class_prediction):
        # Calcular eficiencia por grupo
        groups = {}  # Diccionario para almacenar resultados por grupo
        for true_class, pred_class in class_prediction:
            if true_class not in groups:
                groups[true_class] = {'correct': 0, 'total': 0}

            groups[true_class]['total'] += 1
            if true_class == pred_class:
                groups[true_class]['correct'] += 1

        # Calcular eficiencia para cada grupo
        efficiencies = {}
        for group, values in groups.items():
            efficiency = values['correct'] / values['total'] if values['total'] > 0 else 0
            efficiencies[group] = efficiency

        return efficiencies



    def efic_x_class(self, class_prediction, num_clases):
        # Calcular eficiencia por clase
        classes = {}  # Diccionario para almacenar resultados por clase

        for i in class_prediction:
            for j in class_prediction[i]:
                true_value = class_prediction[i][j][0]
                predict_value = class_prediction[i][j][1]


        for true_class, pred_class in class_prediction:
            if pred_class not in classes:
                classes[pred_class] = {'correct': 0, 'total': 0}

            classes[pred_class]['total'] += 1
            if true_class == pred_class:
                classes[pred_class]['correct'] += 1

        # Calcular eficiencia para cada clase
        efficiencies = {}
        for class_, values in classes.items():
            efficiency = values['correct'] / values['total'] if values['total'] > 0 else 0
            efficiencies[class_] = efficiency

        # Asegurar que se reporten todas las clases, incluso si no tienen predicciones
        for class_ in range(num_clases):
            if class_ not in efficiencies:
                efficiencies[class_] = 0.0  # Establecer eficiencia en 0 para clases sin predicciones

        return efficiencies
