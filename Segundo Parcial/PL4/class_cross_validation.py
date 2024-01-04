import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix, accuracy_score

class KFoldCrossValidation:
    def __init__(self, data, k):
        self.data = pd.read_csv(data)
        self.k = k
        self.model = RandomForestClassifier()
    
    def train_and_evaluate(self,Atributos):
        features = Atributos
        
        X = self.data[features].values
        y = self.data["Class"].values
        
        self.model.fit(X, y)
        
        # Predicciones usando validación cruzada
        y_pred = cross_val_predict(self.model, X, y, cv=self.k)
        
        # Calcular y mostrar la matriz de confusión
        confusion_mat = confusion_matrix(y, y_pred)
        print("Matriz de Confusión:")
        print(confusion_mat)
        
        # Calcular y mostrar el porcentaje de eficiencia
        accuracy = accuracy_score(y, y_pred)
        print(f"Precisión (Accuracy): {accuracy * 100:.2f}%")
        
        # Mostrar el número de muestras clasificadas por cada clase
        for i in range(confusion_mat.shape[0]):
            print(f"Clase {i + 1}: {confusion_mat[i, i]} muestras clasificadas correctamente")