from class_data import Data
from class_file import File

ARCHIVO = './wine.data'
ARCHIVO1 = 'new.txt'
ARCHIVO2 = 'new2.txt'
DELIMITADOR = ','
ATRIBUTOS = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color Intensity', 'Hue', 'ODS280/ODS315 of diluted wines', 'Proline']
CLASE = '1'

base_datos = Data(ARCHIVO, DELIMITADOR, ATRIBUTOS)
archivo_1 = File(ARCHIVO1, DELIMITADOR)
archivo_2 = File(ARCHIVO2, DELIMITADOR)

#base_datos.show_database()
#base_datos.show_column(0)
#base_datos.show_row(1)
#print(base_datos.get_number_of_rows(),'Elementos')
#print(base_datos.get_number_of_columns(),'Atributos')
Matriz = base_datos.get_attribute(['Alcohol','Malic acid','Magnesium'])
#base_datos.show_data(Matriz)
Matriz2 = base_datos.get_class(CLASE)
#base_datos.show_class(Matriz2)

archivo_1.write_data(Matriz)
archivo_2.write_data(Matriz2)