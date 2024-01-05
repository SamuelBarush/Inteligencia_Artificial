from class_data import Data
from class_file import File
from class_knn import KNN
from class_min import MIN
from class_erros import ERROR
from class_train_test import TrainTest

ARCHIVO = './wine.data'
ARCHIVO1 = 'new.txt'
ARCHIVO2 = 'new2.txt'
ARCHIVO3 = 'new3.txt'
DELIMITADOR = ','
ATRIBUTOS = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color Intensity', 'Hue', 'ODS280/ODS315 of diluted wines', 'Proline']

SUBCONJUNTO = 50
INICIO = 1
FIN = 10


def print_matrix(matrix):
    for sublist in matrix:
        for item in sublist:
            print(item, end=', \n')
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

#print_matrix(error.normalizar())

#print(error.desviacion_estandar(1))
#print(error.media(1))

#print_matrix(error.data)
#error.eliminar_columna(1)
#print_matrix(error.data)

#error.vacios(3)
#print(error.contar(3))
TT = TrainTest(base_datos.data, 80)
print_matrix(TT.conjunto_aprendizaje())
#data = error.data_to_list()
#data2 = error.detect_outliers_Zscore(data)