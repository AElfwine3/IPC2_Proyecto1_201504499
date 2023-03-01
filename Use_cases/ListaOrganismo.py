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
    
    def obtener_organismo(self, codigo):
        nodo_actual = self.inicio
        while nodo_actual is not None:
            if nodo_actual.codigo == codigo:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        return None

    def mostrar(self):
        nodo_actual = self.inicio
        lista = []
        while nodo_actual is not None:
            orga = {
                'Codigo': nodo_actual.codigo,
                'Nombre': nodo_actual.nombre,
                'Color': nodo_actual.color
            }
            lista.append(orga)
            nodo_actual = nodo_actual.siguiente
        return lista