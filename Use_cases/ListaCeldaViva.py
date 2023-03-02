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
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.encontrar_celda_viva(fila+i, columna+j):
                    return True
        return False
    
    def encontrar_celda_viva(self, fila, columna):
        nodo_actual = self.inicio
        while nodo_actual is not None:
            if int(nodo_actual.fila) == fila and int(nodo_actual.columna) == columna:
                return True
            nodo_actual = nodo_actual.siguiente
        return False
    
    def vecinos_celda_viva(self, fila, columna, codigo):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                code = self.codigo_organismo(fila+i, columna+j)
                if self.encontrar_celda_viva(fila+i, columna+j):
                    if code != codigo:
                        return True

    def horizontal_celda_viva(self, fila, columna, codigo):
        if self.encontrar_celda_viva(fila, columna+1) and self.codigo_organismo(fila, columna+1) != codigo:
            contador = 1
            while True:
                if self.encontrar_celda_viva(fila, columna+contador):
                    if self.codigo_organismo(fila, columna+contador) == codigo:
                        return True
                    else:
                        contador += 1
                else:
                    break
        elif self.encontrar_celda_viva(fila, columna-1) and self.codigo_organismo(fila, columna-1) != codigo:
            contador = 1
            while True:
                if self.encontrar_celda_viva(fila, columna-contador):
                    if self.codigo_organismo(fila, columna-contador) == codigo:
                        return True
                    else:
                        contador += 1
                else:
                    break
        elif self.encontrar_celda_viva(fila+1, columna) and self.codigo_organismo(fila+1, columna) != codigo:
            contador = 1
            while True:
                if self.encontrar_celda_viva(fila+contador, columna):
                    if self.codigo_organismo(fila+contador, columna) == codigo:
                        return True
                    else:
                        contador += 1
                else:
                    break
        elif self.encontrar_celda_viva(fila-1, columna) and self.codigo_organismo(fila-1, columna) != codigo:
            contador = 1
            while True:
                if self.encontrar_celda_viva(fila-contador, columna):
                    if self.codigo_organismo(fila-contador, columna) == codigo:
                        return True
                    else:
                        contador += 1
                else:
                    break
        elif self.encontrar_celda_viva(fila+1, columna+1) and self.codigo_organismo(fila+1, columna+1) != codigo:
            contador = 1
            while True:
                if self.encontrar_celda_viva(fila+contador, columna+contador):
                    if self.codigo_organismo(fila+contador, columna+contador) == codigo:
                        return True
                    else:
                        contador += 1
                else:
                    break
        elif self.encontrar_celda_viva(fila+1, columna-1) and self.codigo_organismo(fila+1, columna-1) != codigo:
            contador = 1
            while True:
                if self.encontrar_celda_viva(fila+contador, columna-contador):
                    if self.codigo_organismo(fila+contador, columna-contador) == codigo:
                        return True
                    else:
                        contador += 1
                else:
                    break
        elif self.encontrar_celda_viva(fila-1, columna+1) and self.codigo_organismo(fila-1, columna+1) != codigo:
            contador = 1
            while True:
                if self.encontrar_celda_viva(fila-contador, columna+contador):
                    if self.codigo_organismo(fila-contador, columna+contador) == codigo:
                        return True
                    else:
                        contador += 1
                else:
                    break
        elif self.encontrar_celda_viva(fila-1, columna-1) and self.codigo_organismo(fila-1, columna-1) != codigo:
            contador = 1
            while True:
                if self.encontrar_celda_viva(fila-contador, columna-contador):
                    if self.codigo_organismo(fila-contador, columna-contador) == codigo:
                        return True
                    else:
                        contador += 1
                else:
                    break
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

    # si me sirve
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
