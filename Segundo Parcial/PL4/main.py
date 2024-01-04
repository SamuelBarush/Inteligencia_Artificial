from class_data import Data
from class_file import File
from class_knn import KNN
from class_min import MIN
from class_erros import ERROR
from class_k_fold_cross_validation import KFoldCrossValidation
from class_cross_validation import KFoldCrossValidation

ARCHIVO = './wine.data'
ARCHIVO1 = 'new.txt'
ARCHIVO2 = 'new2.txt'
ARCHIVO3 = 'new3.txt'
ARCHIVO4 = 'wine.csv'
DELIMITADOR = ','
ATRIBUTOS = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color Intensity', 'Hue', 'ODS280/ODS315 of diluted wines', 'Proline']
ATRIBUTO = ['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color Intensity', 'Hue', 'ODS280/ODS315 of diluted wines', 'Proline']
CLASE = "Class"
SUBCONJUNTO = 50
INICIO = 1
FIN = 10


def print_matrix(matrix):
    for sublist in matrix:
        for item in sublist:
            print(item, end=", ")
        print()  # Salto de línea después de cada lista interior
    print()  

base_datos = Data(ARCHIVO, DELIMITADOR, ATRIBUTOS)

Matriz = base_datos.get_attribute(['Class','Alcohol','Malic acid','Magnesium'])
Matriz0 = base_datos.get_rows_range(Matriz,50,60)
#print_matrix(Matriz0)


Matriz1 = base_datos.get_attribute(['Class','Alcohol','Malic acid','Magnesium'])
Matriz01 = base_datos.get_rows_range(Matriz1,1,10)
#print_matrix(Matriz01)


#Detectar el porcentaje de muestras

error = ERROR(base_datos.data,3)
clasificar = KFoldCrossValidation(ARCHIVO4,4)
clasificar.train_and_evaluate(ATRIBUTO,CLASE)
#archivo = File(ARCHIVO, ARCHIVO4, ATRIBUTOS)
#archivo.convertir()

#kfold = KFoldCrossValidation(base_datos.data, base_datos.attributes, k=14, random_state=42)
#model = RandomForestClassifier()
#average_score = kfold.train_and_evaluate(model)

#print_matrix(error.normalizar())

#print(error.desviacion_estandar(1))
#print(error.media(1))

#print_matrix(error.data)
#error.eliminar_columna(1)
#print_matrix(error.data)

#error.vacios(3)

#data = error.data_to_list()
#data2 = error.detect_outliers_Zscore(data)