import MuestraSingleton
import OrganismoSingleton

lista_muestra = MuestraSingleton.MuestraSingleton.getInstance().listaMuestra
lista_organismo = OrganismoSingleton.OrganismoSingleton.getInstance().listaOrganismo

def agregar_celula(codigo_muestra, codigo_organismo):
    muestra = lista_muestra.obtener_muestra(codigo_muestra)
    celdas_vivas = muestra.listado_celda_viva
    for i in range(int(muestra.filas)):
        for j in range(int(muestra.columnas)):
            if not celdas_vivas.encontrar_celda_viva(i, j) and celdas_vivas.vecinos_celda_viva(i, j, codigo_organismo):
                if celdas_vivas.horizontal_celda_viva(i, j, codigo_organismo):
                    print(f'El organismo puede prosperar en la celda ({i},{j})')