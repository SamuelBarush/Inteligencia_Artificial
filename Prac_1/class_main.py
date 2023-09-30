import tkinter as tk
from tkinter import filedialog
import pandas as pd
import sys

#Manejando mis otras clases
from class_Map import Map

class Main:

    def __init__(self):
        self.archive = None
        self.matriz = None
        self.archivo_cargado = False #Para saber si se ha cargado un archivo y no permitir cargar otro o multiples

    def load_archive(self):
        if self.archivo_cargado:
            # Si ya se cargó un archivo, no permitir cargar otro
            print("Ya se ha cargado un archivo durante esta sesión.")
            return

        #Cuadro para seleccionar el archivo
        self.archive = filedialog.askopenfilename(filetypes = [("Archivos CSV o TXT", "*.csv *.txt")])
        if not self.archive:
            #No se seleccionó ningún archivo
            return False
        else:
            #Se seleccionó un archivo
            try:
                if self.archive.endswith('.csv'):
                    self.matriz = pd.read_csv(self.archive, header=None).values.tolist() #pd ya que hago el uso de pandas para el tratamiento de datos
                elif self.archive.endswith('.txt'):
                    #Se utilizara un delimitador
                    self.matriz = [list(map(int , line.strip().split(',')))for line in open(self.archive, 'r')]
                else:
                    #El archivo no es compatible
                    print("El formato del archivo no es compatible")
                    sys.exit(1)
            except FileNotFoundError:
                print(f"El archivo :  {self.archive}  no se pudo encontrar")
                sys.exit(1)
            except Exception as e:
                print(f"Ocurrio un error al leer el archivo{str(e)}")

            #Se ha cargado el archivo
            self.archivo_cargado = True

            #Crear instancia de la clase Map y pasar los datos del archivo
            mapa = Map(self.matriz)

#Creando la ventana principal / Menú con Tkinter

ventana = tk.Tk()
ventana.title("Menú principal")

# Obtener el tamaño de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcular el tamaño deseado (por ejemplo, 80% del tamaño de la pantalla)
ancho_deseado = int(ancho_pantalla * 0.45)
alto_deseado = int(alto_pantalla * 0.45)

ventana.geometry(f"{ancho_deseado}x{alto_deseado}")

titulo = tk.Label(ventana, text="Menú principal", font=("Arial Bold", 20))
titulo.pack(pady=20)

#Creando los botones

#Creando instancia de la clase Main
main_instance = Main()

# Cargar un mapa
btn_cargar_mapa = tk.Button(ventana, text="Cargar un mapa", width=20, height=2, command=main_instance.load_archive)
btn_cargar_mapa.pack(pady=20)

#Observar un mapa
btn_observar_mapa = tk.Button(ventana, text="Observar mapa", command=lambda: rend_mapa.observar_mapa({
    0: (0, 0, 0),
    1: (255, 255, 255),
    2: (0, 0, 255),
    3: (255, 255, 0),
    4: (0, 255, 0)
}))
btn_observar_mapa.pack(pady=20)

btn_consultar_tipo_terreno = tk.Button(ventana, text="Consultar tipo de terreno")
btn_consultar_tipo_terreno.pack(pady=20)

ventana.mainloop()

