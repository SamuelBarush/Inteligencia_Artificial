from class_data import Data
from class_file import File
from class_knn import KNN
from class_min import MIN
from class_erros import ERROR

ARCHIVO = './wine.data'
ARCHIVO1 = 'new.txt'
ARCHIVO2 = 'new2.txt'
ARCHIVO3 = 'new3.txt'
DELIMITADOR = ','
#ATRIBUTOS = ['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color Intensity', 'Hue', 'ODS280/ODS315 of diluted wines', 'Proline']
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
print_matrix(Matriz0)


Matriz1 = base_datos.get_attribute(['Class','Alcohol','Malic acid','Magnesium'])
Matriz01 = base_datos.get_rows_range(Matriz1,1,10)
print_matrix(Matriz01)


#Detectar el porcentaje de muestras

error = ERROR(base_datos.data)
class1,class2,class3 = error.contar()
print(f"El numero de muestras de la clase 1 es: {class1}")
print(f"El numero de muestras de la clase 2 es: {class2}")  
print(f"El numero de muestras de la clase 3 es: {class3}")

porcentaje1,porcentaje2,porcentaje3 = error.porcentaje(class1,class2,class3)
print(f"El porcentaje de muestras de la clase 1 es: {porcentaje1}") 
print(f"El porcentaje de muestras de la clase 2 es: {porcentaje2}") 
print(f"El porcentaje de muestras de la clase 3 es: {porcentaje3}") 

vacios = error.vacios()
#print(f"El numero de muestras vacias es: {vacios}")

print(f"El numero de muestras vacias de la clase 1 es: {vacios[1]}")    
print(f"El numero de muestras vacias de la clase 2 es: {vacios[2]}")
print(f"El numero de muestras vacias de la clase 3 es: {vacios[3]}")