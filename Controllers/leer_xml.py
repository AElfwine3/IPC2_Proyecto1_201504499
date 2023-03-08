import xml.etree.ElementTree as ET
from Use_cases import ListaCeldaViva
from List_access import OrganismoSingleton, MuestraSingleton

lista_organismo = OrganismoSingleton.OrganismoSingleton.getInstance().listaOrganismo
lista_muestra = MuestraSingleton.MuestraSingleton.getInstance().listaMuestra


def agregar_organismo(organismo):
    atributos = {}
    for atributo in organismo:
        atributos[atributo.tag] = atributo.text
    if atributos:
        lista_organismo.agregar(atributos['codigo'], atributos['nombre'])

def agregar_muestra(muestra):
    atributos = {}
    for atributo in muestra:
        atributos[atributo.tag] = atributo.text
        if atributo.tag == 'listadoCeldasVivas':
            atributos[atributo.tag] = agregar_celdaViva(atributo)
    if atributos:
        lista_muestra.agregar(atributos['codigo'], atributos['descripcion'], int(atributos['filas']), int(atributos['columnas']), atributos['listadoCeldasVivas'])

def agregar_celdaViva(listado_celda):
    lista_celdaViva = ListaCeldaViva.ListaCeldaViva()
    for celda in listado_celda:
        atributos = {}
        for attrib in celda:
            atributos[attrib.tag] = attrib.text
        if atributos:
            lista_celdaViva.agregar(int(atributos['fila']), int(atributos['columna']), atributos['codigoOrganismo'])
    return lista_celdaViva


def lectura(objeto_xml):
    if objeto_xml.tag == 'organismo':
        agregar_organismo(objeto_xml)
    elif objeto_xml.tag == 'muestra':
        agregar_muestra(objeto_xml)
    for objeto in objeto_xml:
        lectura(objeto)

def leer_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    if not root.tag == "datosMarte":
        print("El archivo no pertenece a datos sobre Marte")
        return
    lectura(root)
    