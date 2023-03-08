from List_access import MuestraSingleton, OrganismoSingleton

lista_muestra = MuestraSingleton.MuestraSingleton.getInstance().listaMuestra
lista_organismo = OrganismoSingleton.OrganismoSingleton.getInstance().listaOrganismo

def prosperar_celula(codigo_muestra, codigo_organismo):
    muestra = lista_muestra.obtener_muestra(codigo_muestra)
    if not muestra:
        print('La muestra no existe')
        return
    celdas_vivas = muestra.listado_celda_viva
    prospera = False
    for i in range(int(muestra.filas)):
        for j in range(int(muestra.columnas)):
            if not celdas_vivas.encontrar_celda_viva(i, j) and celdas_vivas.vecinos_celda_viva(i, j, codigo_organismo):
                if celdas_vivas.prosperar_celda_viva(i, j, codigo_organismo):
                    prospera = True
                    print(f'El organismo puede prosperar en la celda ({i},{j})')
    if not prospera:
        print('El organismo no puede prosperar en ninguna celda')

def agregar_celula(codigo_muestra, codigo_organismo, fila, columna):
    muestra = lista_muestra.obtener_muestra(codigo_muestra)
    if not muestra:
        print('La muestra no existe')
        return
    celdas_vivas = muestra.listado_celda_viva
    if celdas_vivas.prosperar_celda_viva(int(fila), int(columna), codigo_organismo, True):
        print(f'El organismo se agrego y logró prosperar exitosamente! en la celda ({fila},{columna})')
    else:
        print(f'El organismo no prospero en la celda ({fila},{columna})')