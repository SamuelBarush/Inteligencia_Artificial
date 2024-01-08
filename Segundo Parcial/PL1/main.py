from class_data import Data
from class_file import File

ARCHIVO = './wine.data'
ARCHIVO1 = 'new.txt'
ARCHIVO2 = 'new2.txt'
ARCHIVO3 = 'new3.txt'
DELIMITADOR = ','
ATRIBUTOS = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color Intensity', 'Hue', 'ODS280/ODS315 of diluted wines', 'Proline']
SUBCONJUNTO = 50
INICIO = 51
FIN = 100

base_datos = Data(ARCHIVO, DELIMITADOR, ATRIBUTOS)
archivo_1 = File(ARCHIVO1, DELIMITADOR)
archivo_2 = File(ARCHIVO2, DELIMITADOR)
archivo_3 = File(ARCHIVO3, DELIMITADOR)

Matriz = base_datos.get_attribute(['Alcohol','Malic acid','Magnesium'])
base_datos.show_data(Matriz)
print("Matriz 1")
Matriz2 = base_datos.get_rows(SUBCONJUNTO)
base_datos.show_class(Matriz2)
print("Matriz 2")
Matriz3 = base_datos.get_rows_range(Matriz,INICIO,FIN)
base_datos.show_class(Matriz3)
print("Matriz 3")
#archivo_1.write_data(Matriz)
#archivo_2.write_data(Matriz2)
#archivo3.write_data(Matriz3)
