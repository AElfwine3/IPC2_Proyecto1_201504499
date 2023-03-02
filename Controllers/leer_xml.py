import xml.etree.ElementTree as ET
from sys import path
from os import getcwd

path.append(getcwd()+'\\Marte')
path.append(getcwd()+'\\Use_cases')
path.append(getcwd()+'\\List_access')

import Organismo
import Muestra
import CeldaViva

import ListaCeldaViva
import OrganismoSingleton
import MuestraSingleton

lista_organismo = OrganismoSingleton.OrganismoSingleton.getInstance().listaOrganismo
lista_muestra = MuestraSingleton.MuestraSingleton.getInstance().listaMuestra


def agregar_organismo(organismo):
    atributos = {}
    for atributo in organismo:
        atributos[atributo.tag] = atributo.text
    if atributos:
        nodo_organismo = Organismo.Organismo(atributos['codigo'], atributos['nombre'])
        lista_organismo.agregar(nodo_organismo)

def agregar_muestra(muestra):
    atributos = {}
    for atributo in muestra:
        atributos[atributo.tag] = atributo.text
        if atributo.tag == 'listadoCeldasVivas':
            atributos[atributo.tag] = agregar_celdaViva(atributo)
    if atributos:
        nodo_muestra = Muestra.Muestra(atributos['codigo'], atributos['descripcion'], atributos['filas'], atributos['columnas'], atributos['listadoCeldasVivas'])
        lista_muestra.agregar(nodo_muestra)

def agregar_celdaViva(listado_celda):
    lista_celdaViva = ListaCeldaViva.ListaCeldaViva()
    for celda in listado_celda:
        atributos = {}
        for attrib in celda:
            atributos[attrib.tag] = attrib.text
        if atributos:
            nodo_celda_viva = CeldaViva.CeldaViva(atributos['fila'], atributos['columna'], atributos['codigoOrganismo'])
            lista_celdaViva.agregar(nodo_celda_viva)
    return lista_celdaViva
            

def for_recursivo(objeto_xml, tabulacion = ''):
    tabulacion += '\t'
    if objeto_xml.tag == 'organismo':
        agregar_organismo(objeto_xml)
    elif objeto_xml.tag == 'muestra':
        agregar_muestra(objeto_xml)
    for objeto in objeto_xml:
        for_recursivo(objeto, tabulacion)

def leer_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    if not root.tag == "datosMarte":
        print("El archivo no pertenece a datos sobre Marte")
        return
    for_recursivo(root)
    