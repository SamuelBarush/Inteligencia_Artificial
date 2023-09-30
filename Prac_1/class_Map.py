import tkinter as tk
from tkinter import filedialog
import pandas as pd
import sys
import pygame

class Map:
    def __init__(self, archivo):
        self.archive = archivo
        self.archivo_cargado = True


    #def cargar_mapa(self):
