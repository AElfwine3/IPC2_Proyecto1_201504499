from sys import path
from os import getcwd

path.append(getcwd()+'\\Marte')

import Muestra

class ListaMuestra:

    def __init__(self):
        self.inicio = None
    
    def agregar(self, nodo_muestra: Muestra.Muestra):
        if self.inicio == None:
            self.inicio = nodo_muestra
        else:
            nodo_muestra.siguiente = self.inicio
            self.inicio = nodo_muestra
    
    def mostrar(self):
        nodo_actual = self.inicio
        lista = {}
        while nodo_actual is not None:
            lista[nodo_actual.codigo] = nodo_actual.descripcion
            lista[nodo_actual.filas] = nodo_actual.columnas
            lista['Celdas Vivas'] = nodo_actual.listado_celda_viva.mostrar()
            nodo_actual = nodo_actual.siguiente
        return lista