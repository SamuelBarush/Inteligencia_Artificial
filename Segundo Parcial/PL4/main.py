from class_data import Data
from class_file import File
from class_knn import KNN
from class_min import MIN
from class_erros import ERROR

ARCHIVO = 'Segundo Parcial\PL4\wine.data'
ARCHIVO1 = 'new.txt'
ARCHIVO2 = 'new2.txt'
ARCHIVO3 = 'new3.txt'
DELIMITADOR = ','
ATRIBUTOS = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color Intensity', 'Hue', 'ODS280/ODS315 of diluted wines', 'Proline']



import random

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

Matriz = base_datos.get_rows_range(base_datos.data,1,178)

# normalización
data_n = ERROR(Matriz,clases=3)
Matriz = data_n.normalizar()

# división de entrenamiento y prueba
ENTRENAMIENTO, PRUEBA = dividir_entrenamiento_prueba(Matriz,porcentaje_prueba=0.10)


# Instancia del modelo k-NN 
knn = KNN(k=3, distance_metric='manhattan')

# Instancia del modelo min distancia
min = MIN(distance_metric='euclidean')




#entrenamiento
knn.fit(ENTRENAMIENTO)
min.fit(ENTRENAMIENTO)



results_knn = knn.bootstrap_(PRUEBA, num_samples=2)
results_min = min.bootstrap_(PRUEBA,num_samples=2)


#print(knn.efic_x_class(results))
eficiencia_error_knn = knn.efic_x_group(results_knn)
eficiencia_error_min = min.efic_x_group(results_min)

resultados_generales_knn = knn.calcular_eficiencia_error_general(eficiencia_error_knn)
resultados_generales_min = min.calcular_eficiencia_error_general(eficiencia_error_min)

print(resultados_generales_knn)
print(resultados_generales_min)