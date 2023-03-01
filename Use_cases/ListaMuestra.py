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
    
    def verificar_celda_viva(self, fila, columna):
        nodo_actual = self.inicio
        while nodo_actual is not None:
            nodo_celda_viva = nodo_actual.listado_celda_viva.inicio
            while nodo_celda_viva is not None:
                if nodo_celda_viva.fila == fila and nodo_celda_viva.columna == columna:
                    return True
                nodo_celda_viva = nodo_celda_viva.siguiente
            nodo_actual = nodo_actual.siguiente
        return False

    def obtener_muestra(self, codigo):
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
            objeto = {
                'Codigo': nodo_actual.codigo,
                'Descripcion': nodo_actual.descripcion,
                'Filas': nodo_actual.filas,
                'Columnas': nodo_actual.columnas,
                'Celdas Vivas': nodo_actual.listado_celda_viva.mostrar()
            }
            lista.append(objeto)
            nodo_actual = nodo_actual.siguiente
        return lista