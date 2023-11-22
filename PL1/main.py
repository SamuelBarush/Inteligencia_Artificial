from class_data import Data

ARCHIVO = './wine.data'
DELIMITADOR = ','

base_datos = Data(ARCHIVO, DELIMITADOR)

base_datos.show_data()