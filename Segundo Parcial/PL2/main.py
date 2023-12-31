from class_data import Data
from class_file import File
from class_knn import KNN

ARCHIVO = 'Segundo Parcial\PL2\wine.data'
ARCHIVO1 = 'new.txt'
ARCHIVO2 = 'new2.txt'
ARCHIVO3 = 'new3.txt'
DELIMITADOR = ','
#ATRIBUTOS = ['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color Intensity', 'Hue', 'ODS280/ODS315 of diluted wines', 'Proline']
ATRIBUTOS = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color Intensity', 'Hue', 'ODS280/ODS315 of diluted wines', 'Proline']

SUBCONJUNTO = 50
INICIO = 1
FIN = 10

base_datos = Data(ARCHIVO, DELIMITADOR, ATRIBUTOS)

Matriz = base_datos.get_attribute(['Class','Alcohol','Malic acid','Magnesium'])
Matriz0 = base_datos.get_rows_range(Matriz,0,160)
print(Matriz0)

#base_datos.show_data(Matriz)
Matriz1 = base_datos.get_attribute(['Class','Alcohol','Malic acid','Magnesium'])
Matriz01 = base_datos.get_rows_range(Matriz1,150,160)
print(Matriz1)

# Instancia del modelo k-NN y entrenamiento
knn = KNN(k=5)
training_data = Matriz0
test_data = Matriz01
knn.fit(training_data)

# Predicciones para los datos de prueba
predictions = knn.predict(test_data)
print(f"Predicciones:{predictions}")

