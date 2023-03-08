from Marte import CeldaViva

class ListaCeldaViva:

    def __init__(self):
        self.inicio = None

    def agregar(self, fila, columna, codigo_organismo):
        nodo_celda_viva = CeldaViva.CeldaViva(fila, columna, codigo_organismo)
        if self.inicio == None:
            self.inicio = nodo_celda_viva
        else:
            nodo_actual = self.inicio
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_celda_viva

    def modificar(self, fila, columna, codigo_organismo):
        nodo_actual = self.inicio
        while nodo_actual is not None:
            if int(nodo_actual.fila) == fila and int(nodo_actual.columna) == columna:
                nodo_actual.codigo_organismo = codigo_organismo
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def recorrer(self, indice: int):
        nodo_actual = self.inicio
        contador = 0
        while nodo_actual is not None:
            if contador == indice:
                return nodo_actual
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return None

    def tamano(self):
        nodo_actual = self.inicio
        contador = 0
        while nodo_actual is not None:
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador

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
                if self.encontrar_celda_viva(fila+i, columna+j):
                    if codigo != self.codigo_organismo(fila+i, columna+j):
                        return True

    def prosperar_celda_viva(self, fila, columna, codigo, agregar=False):
        retornar = False
        if self.encontrar_celda_viva(fila, columna+1) and self.codigo_organismo(fila, columna+1) != codigo:
            contador = 1
            celdas_a_modificar = ListaCeldaViva()
            while True:
                if self.encontrar_celda_viva(fila, columna+contador):
                    if self.codigo_organismo(fila, columna+contador) == codigo:
                        if agregar:
                            self.agregar(fila, columna, codigo)
                            for i in range(celdas_a_modificar.tamano()):
                                self.modificar(celdas_a_modificar.recorrer(i).fila, celdas_a_modificar.recorrer(i).columna, codigo)
                            retornar = True
                            break
                        return True
                    else:
                        celdas_a_modificar.agregar(fila, columna+contador, codigo)
                        contador += 1
                else:
                    break
        if self.encontrar_celda_viva(fila, columna-1) and self.codigo_organismo(fila, columna-1) != codigo:
            contador = 1
            celdas_a_modificar = ListaCeldaViva()
            while True:
                if self.encontrar_celda_viva(fila, columna-contador):
                    if self.codigo_organismo(fila, columna-contador) == codigo:
                        if agregar:
                            self.agregar(fila, columna, codigo)
                            for i in range(celdas_a_modificar.tamano()):
                                self.modificar(celdas_a_modificar.recorrer(i).fila, celdas_a_modificar.recorrer(i).columna, codigo)
                            retornar = True
                            break
                        return True
                    else:
                        celdas_a_modificar.agregar(fila, columna-contador, codigo)
                        contador += 1
                else:
                    break
        if self.encontrar_celda_viva(fila+1, columna) and self.codigo_organismo(fila+1, columna) != codigo:
            contador = 1
            celdas_a_modificar = ListaCeldaViva()
            while True:
                if self.encontrar_celda_viva(fila+contador, columna):
                    if self.codigo_organismo(fila+contador, columna) == codigo:
                        if agregar:
                            self.agregar(fila, columna, codigo)
                            for i in range(celdas_a_modificar.tamano()):
                                self.modificar(celdas_a_modificar.recorrer(i).fila, celdas_a_modificar.recorrer(i).columna, codigo)
                            retornar = True
                            break
                        return True
                    else:
                        celdas_a_modificar.agregar(fila+contador, columna, codigo)
                        contador += 1
                else:
                    break
        if self.encontrar_celda_viva(fila-1, columna) and self.codigo_organismo(fila-1, columna) != codigo:
            contador = 1
            celdas_a_modificar = ListaCeldaViva()
            while True:
                if self.encontrar_celda_viva(fila-contador, columna):
                    if self.codigo_organismo(fila-contador, columna) == codigo:
                        if agregar:
                            self.agregar(fila, columna, codigo)
                            for i in range(celdas_a_modificar.tamano()):
                                self.modificar(celdas_a_modificar.recorrer(i).fila, celdas_a_modificar.recorrer(i).columna, codigo)
                            retornar = True
                            break
                        return True
                    else:
                        celdas_a_modificar.agregar(fila-contador, columna, codigo)
                        contador += 1
                else:
                    break
        if self.encontrar_celda_viva(fila+1, columna+1) and self.codigo_organismo(fila+1, columna+1) != codigo:
            contador = 1
            celdas_a_modificar = ListaCeldaViva()
            while True:
                if self.encontrar_celda_viva(fila+contador, columna+contador):
                    if self.codigo_organismo(fila+contador, columna+contador) == codigo:
                        if agregar:
                            self.agregar(fila, columna, codigo)
                            for i in range(celdas_a_modificar.tamano()):
                                self.modificar(celdas_a_modificar.recorrer(i).fila, celdas_a_modificar.recorrer(i).columna, codigo)
                            retornar = True
                            break
                        return True
                    else:
                        celdas_a_modificar.agregar(fila+contador, columna+contador, codigo)
                        contador += 1
                else:
                    break
        if self.encontrar_celda_viva(fila+1, columna-1) and self.codigo_organismo(fila+1, columna-1) != codigo:
            contador = 1
            celdas_a_modificar = ListaCeldaViva()
            while True:
                if self.encontrar_celda_viva(fila+contador, columna-contador):
                    if self.codigo_organismo(fila+contador, columna-contador) == codigo:
                        if agregar:
                            self.agregar(fila, columna, codigo)
                            for i in range(celdas_a_modificar.tamano()):
                                self.modificar(celdas_a_modificar.recorrer(i).fila, celdas_a_modificar.recorrer(i).columna, codigo)
                            retornar = True
                            break
                        return True
                    else:
                        celdas_a_modificar.agregar(fila+contador, columna-contador, codigo)
                        contador += 1
                else:
                    break
        if self.encontrar_celda_viva(fila-1, columna+1) and self.codigo_organismo(fila-1, columna+1) != codigo:
            contador = 1
            celdas_a_modificar = ListaCeldaViva()
            while True:
                if self.encontrar_celda_viva(fila-contador, columna+contador):
                    if self.codigo_organismo(fila-contador, columna+contador) == codigo:
                        if agregar:
                            self.agregar(fila, columna, codigo)
                            for i in range(celdas_a_modificar.tamano()):
                                self.modificar(celdas_a_modificar.recorrer(i).fila, celdas_a_modificar.recorrer(i).columna, codigo)
                            retornar = True
                            break
                        return True
                    else:
                        celdas_a_modificar.agregar(fila-contador, columna+contador, codigo)
                        contador += 1
                else:
                    break
        if self.encontrar_celda_viva(fila-1, columna-1) and self.codigo_organismo(fila-1, columna-1) != codigo:
            contador = 1
            celdas_a_modificar = ListaCeldaViva()
            while True:
                if self.encontrar_celda_viva(fila-contador, columna-contador):
                    if self.codigo_organismo(fila-contador, columna-contador) == codigo:
                        if agregar:
                            self.agregar(fila, columna, codigo)
                            for i in range(celdas_a_modificar.tamano()):
                                self.modificar(celdas_a_modificar.recorrer(i).fila, celdas_a_modificar.recorrer(i).columna, codigo)
                            retornar = True
                            break
                        return True
                    else:
                        celdas_a_modificar.agregar(fila-contador, columna-contador, codigo)
                        contador += 1
                else:
                    break
        
        return retornar

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
