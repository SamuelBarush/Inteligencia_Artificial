from sklearn.model_selection import KFold
import numpy as np

class KFoldCrossValidation:
    def __init__(self, data, labels, k=5, random_state=None):
        self.data = self.convert_to_numpy(data)
        self.labels = np.array(labels)
        self.k = k
        self.random_state = random_state
        self.kfold = KFold(n_splits=k, shuffle=True, random_state=random_state)

    def convert_to_numpy(self, data):
        # Convierte los datos a un formato numpy adecuado para el uso de modelos de aprendizaje automático
        converted_data = []
        for row in data:
            converted_row = [float(value) if dtype == 'float' else int(value) for value, dtype, _ in row[1:]]
            converted_data.append(converted_row)
        return np.array(converted_data)

    def train_and_evaluate(self, model):
        scores = []
        for train_index, test_index in self.kfold.split(self.data):
            X_train, X_test = self.data[train_index], self.data[test_index]

            model.fit(X_train, )
            score = model.score(X_test,)
            scores.append(score)

        average_score = np.mean(scores)
        return average_score


