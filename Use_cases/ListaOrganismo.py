from sys import path
from os import getcwd

path.append(getcwd()+'\\Marte')

import Organismo

class ListaOrganismo:

    def __init__(self):
        self.inicio = None
    
    def agregar(self, nodo_organismo: Organismo.Organismo):
        if self.inicio is None:
            self.inicio = nodo_organismo
        else:
            nodo_actual = self.inicio
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_organismo
    
    def mostrar(self):
        nodo_actual = self.inicio
        lista = {}
        while nodo_actual is not None:
            lista[nodo_actual.codigo] = nodo_actual.nombre
            nodo_actual = nodo_actual.siguiente
        return lista