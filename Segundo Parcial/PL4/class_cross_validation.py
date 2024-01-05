import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score
import numpy as np

class KFoldCrossValidation:
    def __init__(self, data, k, model='knn', neighbors=1):
        self.data = pd.read_csv(data)
        self.k = k
        self.model_name = model.lower()
        self.neighbors = neighbors
        self.model = self._get_model()
    
    def _get_model(self):
        if self.model_name == 'knn':
            return KNeighborsClassifier(n_neighbors=self.neighbors)
        elif self.model_name == 'randomforest':
            return RandomForestClassifier()
        else:
            raise ValueError("Model not supported. Please choose 'knn' or 'randomforest'.")
    
    def train_and_evaluate(self, ATRIBUTO, CLASE):
        features = ATRIBUTO
        
        X = self.data[features].values
        y = self.data[CLASE].values
        
        self.model.fit(X, y)
        
        # Predicciones usando validación cruzada
        y_pred = cross_val_predict(self.model, X, y, cv=self.k)
        
        # Calcular y mostrar la matriz de confusión
        confusion_mat = confusion_matrix(y, y_pred)
        print("Matriz de Confusión:")
        print(confusion_mat)
        
        # Calcular y mostrar el porcentaje de eficiencia por clase
        precision_per_class = precision_score(y, y_pred, average=None)
        print("Precisión por Clase:")
        for i in range(len(precision_per_class)):
            print(f"Clase {i + 1}: {precision_per_class[i] * 100:.2f}% - Muestras correctas: {confusion_mat[i, i]}")
        
        # Calcular y mostrar la desviación estándar de la precisión por clase
        std_precision_per_class = np.std(precision_per_class)
        print(f"Desviación Estándar de la Precisión: {std_precision_per_class * 100:.2f}%")
