import csv

class File:
    def __init__(self, archivo_texto, archivo_csv, nombres_columna=None):
        self.archivo_texto = archivo_texto
        self.archivo_csv = archivo_csv
        self.nombres_columna = nombres_columna

    def convertir(self):
        with open(self.archivo_texto, 'r') as archivo_texto:
            lineas = archivo_texto.readlines()

        with open(self.archivo_csv, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)

            # Escribir los nombres de columna como la primera fila si están definidos
            if self.nombres_columna:
                escritor_csv.writerow(self.nombres_columna)

            for linea in lineas:
                campos = linea.strip().split()
                escritor_csv.writerow(campos)
