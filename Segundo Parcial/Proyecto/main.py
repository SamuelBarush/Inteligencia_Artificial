from class_data import Data
from class_file import File
from class_knn import KNN
from class_min import MIN
from class_erros import ERROR
from class_k_fold_cross_validation import KFoldCrossValidation
from class_traintest_bootstraping import KNN2
import random

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

def dividir_entrenamiento_prueba(data, porcentaje_prueba=0.1):
    # Diccionario para almacenar datos por clase
    datos_por_clase = {}
    conjunto_entrenamiento = []
    conjunto_prueba = []

    # Agrupar los datos por clases
    for entry in data:
        clase = entry[0][0]  # Obtener la clase de cada entrada
        if clase not in datos_por_clase:
            datos_por_clase[clase] = []
        datos_por_clase[clase].append(entry)

    # Recorrer cada clase para dividir los datos
    for clase, datos_clase in datos_por_clase.items():
        # Obtener el número de muestras para prueba según el porcentaje
        cantidad_muestras_prueba = int(len(datos_clase) * porcentaje_prueba)

        # Mezclar aleatoriamente las muestras
        random.shuffle(datos_clase)

        # Dividir el conjunto de datos de la clase en entrenamiento y prueba
        conjunto_prueba.extend(datos_clase[:cantidad_muestras_prueba])
        conjunto_entrenamiento.extend(datos_clase[cantidad_muestras_prueba:])

    # Mezclar aleatoriamente los conjuntos finales
    random.shuffle(conjunto_entrenamiento)
    random.shuffle(conjunto_prueba)

    return conjunto_entrenamiento, conjunto_prueba

def print_matrix(matrix):
    for sublist in matrix:
        for item in sublist:
            print(item, end=", ")
        print()  # Salto de línea después de cada lista interior
    print()  

base_datos = Data(ARCHIVO, DELIMITADOR, ATRIBUTOS)

Matriz = base_datos.get_attribute(['Class','Alcohol','Malic acid','Magnesium'])

#Modelo K Fold Cross Validation
#print("Modelo K Fold Cross Validation")
#modelo = KNN(k=10, distance_metric='manhattan')
#clasificar = KFoldCrossValidation(modelo, 5)
#clasificar.cross_validate(base_datos.data)

# Modelo Train Test
#print("Modelo Train & Test")
#ENTRENAMIENTO, PRUEBA = dividir_entrenamiento_prueba(Matriz,porcentaje_prueba=0.10)
#knn = KNN2(k=5, distance_metric='manhattan')
#min = MIN(distance_metric='euclidean')
#knn.fit(ENTRENAMIENTO)
#min.fit(ENTRENAMIENTO)
#resultados_tt_knn = knn.Train_Test(PRUEBA, 80)
#resultados_tt_min = min.Train_Test(PRUEBA, 80)
#eficiencia_error_knn = knn.efic_x_group(resultados_tt_knn)
#eficiencia_error_min = min.efic_x_group(resultados_tt_min)
#resultados_tt_knn = knn.calcular_eficiencia_error_general(eficiencia_error_knn)
#resultados_tt_min = min.calcular_eficiencia_error_general(eficiencia_error_min)
#print(resultados_tt_knn)
#print(resultados_tt_min)

#Modelo Bootstraping

#print("Modelo Bootstraping")
#results_knn = knn.bootstrap_(PRUEBA, num_samples=2)
#results_min = min.bootstrap_(PRUEBA,num_samples=2)
#print(knn.efic_x_class(results))
#eficiencia_error_knn = knn.efic_x_group(results_knn)
#eficiencia_error_min = min.efic_x_group(results_min)
#resultados_generales_knn = knn.calcular_eficiencia_error_general(eficiencia_error_knn)
#resultados_generales_min = min.calcular_eficiencia_error_general(eficiencia_error_min)
#print(resultados_generales_knn)
#print(resultados_generales_min)