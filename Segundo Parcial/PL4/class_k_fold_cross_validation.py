
class KFoldCrossValidation:
    def __init__(self, model, k=5):
        self.model = model
        self.k = k

    def split_data(self, data):
        fold_size = len(data) // self.k
        folds = [data[i:i+fold_size] for i in range(0, len(data), fold_size)]
        return folds

    def calculate_accuracy(self, predictions, actual_labels):
        correct_predictions = sum(1 for p, a in zip(predictions, actual_labels) if p == a)
        total_predictions = len(predictions)
        accuracy = correct_predictions / total_predictions
        return accuracy

    def cross_validate(self, data):
        folds = self.split_data(data)
        accuracies = []

        for i in range(self.k):
            test_set = folds[i]
            train_set = [data[j] for j in range(self.k) if j != i for data in folds[j]]

            self.model.fit(train_set)
            predictions = self.model.predict(test_set)

            actual_labels = [data[0][0][0] for data in test_set]
            accuracy = self.calculate_accuracy(predictions, actual_labels)
            accuracies.append(accuracy)

        average_accuracy = sum(accuracies) / self.k
        print(f'Precisión promedio de K-Fold Cross Validation (K={self.k}): {average_accuracy}')