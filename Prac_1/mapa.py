import pandas as pd
import pygame
import tkinter as tk
import sys

nombre_archivo = input("Ingrese el nombre del archivo (CSV o TXT): ")

try:
    if nombre_archivo.endswith('.csv'):
        df = pd.read_csv(nombre_archivo)
    elif nombre_archivo.endswith('.txt'):
        # Utiliza '\n' como el delimitador para separar las filas
        df = pd.read_csv(nombre_archivo, delimiter=',', header=None)
    else:
        print("Formato de archivo no compatible.")
        sys.exit(1)
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró.")
    sys.exit(1)
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {str(e)}")
    sys.exit(1)

# Imprimiendo el contenido del archivo correctamente
print(df.to_string(index=False, header=False))

# Definir el mapa de tipos de terreno
terreno_mapa = {
    0: "Montaña",
    1: "Tierra",
    2: "Agua",
    3: "Arena",
    4: "Bosque"
}

def observar_mapa(colores_terreno):
    pygame.init()

    # Construyendo la ventana del juego
    Ventana_ancho = 800
    Ventana_alto = 600
    Celda_ancho = 80
    Celda_alto = 80
    ventana = pygame.display.set_mode((Ventana_ancho, Ventana_alto))
    pygame.display.set_caption("Mapa")

    reloj = pygame.time.Clock()
    ejecutando = True

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
        ventana.fill((255, 255, 255))

        # Dibujar el mapa
        for fila in range(len(df + 1 )):
            for columna in range(len(df[fila] + 1)):
                tipo_terreno = df.iloc[fila, columna]
                color = colores_terreno.get (tipo_terreno)
                pygame.draw.rect(ventana,color, (columna * Celda_ancho, fila * Celda_alto, Celda_ancho, Celda_alto))


        pygame.display.flip()
        reloj.tick(10)

    pygame.quit()

#def Controles():





def consultar_tipo_terreno():
    # Esta es una función de ejemplo, debes personalizarla para que consulte el tipo de terreno
    # en función de las coordenadas ingresadas por el usuario.
    coordenada_x = int(input("Ingrese la coordenada X: "))
    coordenada_y = int(input("Ingrese la coordenada Y: "))

    tipo_terreno = df.iloc[coordenada_y, coordenada_x]
    nombre_terreno = terreno_mapa.get(tipo_terreno, "Desconocido")

    print(f"El tipo de terreno en ({coordenada_x}, {coordenada_y}) es: {nombre_terreno}")

def jugar():
    # Función para iniciar el juego
    pass

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menu principal")

# Crear etiqueta de título
titulo = tk.Label(ventana, text="Bienvenido al juego de los exploradores", font=("Arial", 16))
titulo.pack(pady=20)

# Botones para las opciones del menú
btn_observar_mapa = tk.Button(ventana, text="Observar mapa", command=lambda: observar_mapa({
    0: (0, 0, 0),
    1: (255, 255, 255),
    2: (0, 0, 255),
    3: (255, 255, 0),
    4: (0, 255, 0)
}))
btn_observar_mapa.pack()


btn_consultar_tipo_terreno = tk.Button(ventana, text="Consultar tipo de terreno", command=consultar_tipo_terreno)
btn_consultar_tipo_terreno.pack()

btn_jugar = tk.Button(ventana, text="Jugar", command=jugar)
btn_jugar.pack()

# Iniciar la aplicación
ventana.mainloop()
