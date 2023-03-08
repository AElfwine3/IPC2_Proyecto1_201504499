from Marte import Muestra

class ListaMuestra:

    def __init__(self):
        self.inicio = None
    
    def agregar(self, codigo, descripcion, filas, columnas, listado_celda_viva):
        nodo_muestra = Muestra.Muestra(codigo, descripcion, filas, columnas, listado_celda_viva)
        if self.inicio == None:
            self.inicio = nodo_muestra
        else:
            nodo_actual = self.inicio
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_muestra

    def tamano(self):
        nodo_actual = self.inicio
        contador = 0
        while nodo_actual is not None:
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador

    def recorrer(self, indice):
        nodo_actual = self.inicio
        contador = 0
        while nodo_actual is not None:
            if contador == indice:
                return nodo_actual
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return None

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
            }
            lista.append(objeto)
            nodo_actual = nodo_actual.siguiente
        return lista