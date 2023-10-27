import pygame
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

print("Seleccione el algoritmo de busqueda")
print("1) Busqueda por profundidad")
print("2) Busqueda por anchura")
opcion = int(input())
print("Ingrese la prioridad de las acciones, ejemplo (Arriba,Abajo,Izquierda,Derecha)")
prio=input()

if opcion == 1:
    opcion1 = True
else:
    opcion1=False

def leer_lab(filename):
    with open(filename,'r') as f:
        content = f.read().splitlines()
    lab = []
    for line in content:
        row = [int(x)for x in line]
        lab.append(row)
    return lab

# Definir los colores que se utilizarán
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

# Definir el tamaño de los bloques que formarán el laberinto
BLOCK_WIDTH = 20
BLOCK_HEIGHT = 20

# Leer el laberinto desde un archivo de texto
filename = 'laberinto.txt'
maze = leer_lab(filename)

# Obtener el número de filas y columnas del laberinto
NUM_ROWS = len(maze)
NUM_COLS = len(maze[0])

# Calcular el tamaño de la pantalla en función del tamaño del laberinto
SCREEN_WIDTH = NUM_COLS * BLOCK_WIDTH
SCREEN_HEIGHT = NUM_ROWS * BLOCK_HEIGHT

# Inicializar Pygame
pygame.init()

# Crear la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Laberinto")


# Dibujar el laberinto
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        if maze[row][col] == 0:
            pygame.draw.rect(screen, WHITE, [col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT])
        else:
            pygame.draw.rect(screen, BLACK, [col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT])

# Actualizar la pantalla
pygame.display.flip()


# Esperar a que el usuario cierre la ventana
start_pos=None
end_pos = None
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Obtener la posición del clic del mouse
            pos = pygame.mouse.get_pos()
            # Convertir la posición en índices de fila y columna
            row = pos[1] // BLOCK_HEIGHT
            col = pos[0] // BLOCK_WIDTH
            if start_pos is None:
                start_pos = (row,col)
                # Resaltar la casilla seleccionada
                pygame.draw.rect(screen, GREEN, [col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT])
            elif end_pos is None and (row,col) != start_pos:
                end_pos = (row,col)
                # Resaltar la casilla seleccionada
                pygame.draw.rect(screen, RED, [col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT])
                done = True
    pygame.display.flip()

# Salir de Pygame

print("El punto inicial es:",start_pos)
print("La meta es:",end_pos)

def plot_graph(prodecessors):
    G = nx.DiGraph()
    for child, parent in prodecessors.items():
        G.add_edge(parent,child)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.show


def get_neighbors(maze,point,priority):
    #Devuelve una lista de los vecinos válidos de un punto en el laberinto
    my_string=priority
    my_list = my_string.split(",")
    neighbors=[]
    row,col = point
    for prio in my_list:
        if prio == "Arriba":
            if row >0 and not maze[row-1][col]:
                neighbors.append((row-1,col))  #Arriba
        if prio == "Izquierda":
            if col >0 and not maze[row][col-1]:
                neighbors.append((row,col-1)) #Izquierda
        if prio == "Abajo":
            if row <len(maze)-1 and not maze[row+1][col]:
                neighbors.append((row+1,col)) #Abajo
        if prio == "Derecha":
            if col <len(maze[0])-1 and not maze[row][col+1]:
                neighbors.append((row,col+1)) #Derecha
    return neighbors


#Anchura
def bfs(maze, start, end,prio):
    #visited = {start: 0}  # Almacena los padres de cada posición visitada.
    #queue = deque([start])  # Almacena las posiciones a visitar en orden de BFS.
    queue= [start,]
    visited = set()
    prodecessors = {} #Diccionario para almacenar los prodecesores de cada nodo
    while queue:
        current = queue.pop(0) #Obtiene el primer nodo de la cola
        visited.add(current)    
        if current == end:
            # Se llegó al destino, se reconstruye el camino desde el inicio.
            path = []
            while current != start:
                path.append(current)
                current = prodecessors[current]
            path.append(start)
            return prodecessors,path[::-1]#,visited,queue,prodecessors#Encuentra el camino encontrado
        for neighbor in get_neighbors(maze, current,priority=prio):
            if neighbor not in visited:
                #visited[neighbor] = current
                queue.append(neighbor)
                prodecessors[neighbor] = current
        # Si no se encuentra ningún camino, devuelve una lista vacía.
    return None

#Profundidad
""""
def dfs(maze, start, end,prio):
    visited = set()
    prodecessors = {}
    stack = [start]
    while stack:
        state = stack.pop()
        visited.add(state)
        if state == end:
            path = []
            while state != start:
                path.append(state)
                state = prodecessors[state]
            path.append(start)
            return prodecessors,path[::-1]
        for neighbor in get_neighbors(maze,state,priority=prio):
            if neighbor not in visited:
                stack.append(neighbor)
                prodecessors[neighbor]= state
    return None
"""
def dfs(maze,start,end,prio):
    nodo_raiz=start
    prodecessors={}
    if end == nodo_raiz:
        return nodo_raiz
    frontera = [nodo_raiz,]
    explorados = set()
    while frontera:
        nodo = frontera.pop()
        explorados.add(nodo)
        if nodo == end:
            # Se llegó al destino, se reconstruye el camino desde el inicio.
            path = []
            while nodo != start:
                path.append(nodo)
                nodo = prodecessors[nodo]
            path.append(start)
            return prodecessors,path[::-1]#Encuentra el camino encontrado
        for neighbor in get_neighbors(maze, nodo ,prio):
            if neighbor not in explorados:
                #visited[neighbor] = current
                frontera.append(neighbor)
                prodecessors[neighbor] = nodo
        # Si no se encuentra ningún camino, devuelve una lista vacía.
    return None

pygame.display.flip()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Laberinto resuelto")


if opcion == 2:
    prodecessors,path=bfs(maze,start_pos,end_pos,prio)
    long=len(path)
    print("El costo es de:",long-1)
    #print("Nodos visitados:",visited)
    #print("Frontera:",queue)
    print("Predecesores",prodecessors)
    print("El camino por medio de busqueda por anchura es",path)
    
    #Imprimir el camino del laberinto resuelto
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            else:
                for row in range(NUM_ROWS):
                    for col in range(NUM_COLS):
                        if maze[row][col] == 0:
                            pygame.draw.rect(screen, WHITE, [col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT])
                        else:
                            pygame.draw.rect(screen, BLACK, [col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT])
    
                for square in path:
                    x,y=square
                    pygame.draw.rect(screen, BLUE, [y * BLOCK_WIDTH, x * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT])

                for node, parent in prodecessors.items():
                    if parent is not None:
                        x1,y1=parent
                        x2,y2=node
                        pygame.draw.line(screen, GREEN, [y1 * BLOCK_WIDTH + BLOCK_WIDTH//2, x1 * BLOCK_HEIGHT + BLOCK_HEIGHT//2], [y2 * BLOCK_WIDTH + BLOCK_WIDTH//2, x2 * BLOCK_HEIGHT + BLOCK_HEIGHT//2], 2)
        pygame.display.flip()
       

else:
    print("Ingresa la prioridad de las acciones considerando")
    prodecessors,path=dfs(maze,start_pos,end_pos,prio)
    long=len(path)
    print("El costo es de:",long-1)
    #print("Nodos visitados:",visited)
    #print("Frontera:",queue)
    print("Predecesores",prodecessors)
    print("El camino por medio de busqueda por profundidad es",path)
   #Imprimir el camino del laberinto resuelto
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            else:
                for row in range(NUM_ROWS):
                    for col in range(NUM_COLS):
                        if maze[row][col] == 0:
                            pygame.draw.rect(screen, WHITE, [col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT])
                        else:
                            pygame.draw.rect(screen, BLACK, [col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT])
    
                for square in path:
                    x,y=square
                    pygame.draw.rect(screen, BLUE, [y * BLOCK_WIDTH, x * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT])

                for node, parent in prodecessors.items():
                    if parent is not None:
                        x1,y1=parent
                        x2,y2=node
                        pygame.draw.line(screen, GREEN, [y1 * BLOCK_WIDTH + BLOCK_WIDTH//2, x1 * BLOCK_HEIGHT + BLOCK_HEIGHT//2], [y2 * BLOCK_WIDTH + BLOCK_WIDTH//2, x2 * BLOCK_HEIGHT + BLOCK_HEIGHT//2], 2)
        pygame.display.flip() 

