class KNN:
    def __init__(self, k, data_base, data_to_classify, type):
        self.k = k
        self.data = data_base
        self.data_to_classify = data_to_classify
        self.type_distance = type
        self.distance = self.calculate_distance()

    def euclidean_distance(self, value1, value2):
        distance = 0.0
        for i in range(len(value1)):
            distance += (value1[i] - value2[i]) ** 2
        return distance ** 0.5

    def calculate_distance(self):
        distance = []
        for row in self.data_to_classify:
            row_distance = []
            for row2 in self.data:
                if self.type_distance == 'euclidean':
                    row_distance.append(self.euclidean_distance(row[0], row2[0]))
                else:
                    row_distance.append(self.manhattan_distance(row[0], row2[0]))
            distance.append(row_distance)
        return distance

    def manhattan_distance(self, value1, value2):
        distance = 0.0
        for i in range(len(value1)):
            distance += abs(value1[i] - value2[i])
        return distance