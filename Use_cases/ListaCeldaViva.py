from sys import path
from os import getcwd

path.append(getcwd()+'\\Marte')

import CeldaViva

class ListaCeldaViva:

    def __init__(self):
        self.inicio = None
    
    def agregar(self, nodo_celda_viva: CeldaViva.CeldaViva):
        if self.inicio == None:
            self.inicio = nodo_celda_viva
        else:
            nodo_celda_viva.siguiente = self.inicio
            self.inicio = nodo_celda_viva

    def mostrar(self):
        nodo_actual = self.inicio
        lista = {}
        while nodo_actual is not None:
            lista[nodo_actual.codigo_organismo] = f'fila: {nodo_actual.fila} - columna: {nodo_actual.columna}'
            nodo_actual = nodo_actual.siguiente
        return lista
