from class_data import Data
from class_file import File
from class_knn import KNN
from class_min import MIN
from class_erros import ERROR

ARCHIVO = '/home/ed/Documents/GitHub/Inteligencia_Artificial/Segundo Parcial/PL4/wine.data'
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



# Instancia del modelo k-NN y entrenamiento
knn = KNN(k=10, distance_metric='manhattan')
training_data = base_datos.data
test_data = Matriz01
knn.fit(training_data)


#print("labels:")
#knn.get_labels()

#---------------------------------------------

# Predicciones para los datos de prueba
#predictions = knn.predict(test_data)
#print(f"Predicciones:{predictions}")



#bootstrap_predictions = knn.bootstrap(base_datos.data, num_samples=2)
#print(bootstrap_predictions)

data = base_datos.data
data_n = ERROR(data,clases=3)
normalized = data_n.normalizar()



results = knn.bootstrap_(normalized, num_samples=1)

print(knn.efic_x_class(results,num_clases=3))




#eficiencia,error,des_efi,des_err = knn.bootstrap_(base_datos.data, num_samples=2)

#print(eficiencia,error,des_efi,des_err)