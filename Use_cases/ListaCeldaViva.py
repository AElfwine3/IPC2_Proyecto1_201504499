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

    def is_celda_viva(self, fila, columna):
        nodo_actual = self.inicio
        while nodo_actual is not None:
            if int(nodo_actual.fila) == fila and int(nodo_actual.columna) == columna:
                return True
            if int(nodo_actual.fila)-1 == fila and int(nodo_actual.columna)-1 == columna:
                return True
            if int(nodo_actual.fila)-1 == fila and int(nodo_actual.columna) == columna:
                return True
            if int(nodo_actual.fila)-1 == fila and int(nodo_actual.columna)+1 == columna:
                return True
            if int(nodo_actual.fila) == fila and int(nodo_actual.columna)-1 == columna:
                return True
            if int(nodo_actual.fila) == fila and int(nodo_actual.columna)+1 == columna:
                return True
            if int(nodo_actual.fila)+1 == fila and int(nodo_actual.columna)-1 == columna:
                return True
            if int(nodo_actual.fila)+1 == fila and int(nodo_actual.columna) == columna:
                return True
            if int(nodo_actual.fila)+1 == fila and int(nodo_actual.columna)+1 == columna:
                return True
            nodo_actual = nodo_actual.siguiente
        return False
    
    def existe_fila(self, fila):
        nodo_actual = self.inicio
        while nodo_actual is not None:
            if int(nodo_actual.fila) == fila:
                return True
            if int(nodo_actual.fila)-1 == fila:
                return True
            if int(nodo_actual.fila)+1 == fila:
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def codigo_organismo(self, fila, columna):
        nodo_actual = self.inicio
        while nodo_actual is not None:
            if int(nodo_actual.fila) == fila and int(nodo_actual.columna) == columna:
                return nodo_actual.codigo_organismo
            nodo_actual = nodo_actual.siguiente
        return None

    def mostrar(self):
        nodo_actual = self.inicio
        lista = []
        objeto = {}
        while nodo_actual is not None:
            objeto[nodo_actual.codigo_organismo] = f'fila: {nodo_actual.fila} - columna: {nodo_actual.columna}'
            lista.append(objeto)
            nodo_actual = nodo_actual.siguiente
        return lista
