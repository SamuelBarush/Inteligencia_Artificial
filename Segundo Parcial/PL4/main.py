from class_data import Data
from class_file import File
from class_knn import KNN
from class_min import MIN
from class_erros import ERROR
from class_k_fold_cross_validation import KFoldCrossValidation

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

modelo = KNN(k=10, distance_metric='manhattan')

error = ERROR(base_datos.data,3)
clasificar = KFoldCrossValidation(modelo, 5)
clasificar.cross_validate(base_datos.data)
