import tkinter as tk
from tkinter import filedialog
from sys import path
from os import getcwd

path.append(getcwd()+'\\Controllers')
path.append(getcwd()+'\\List_access')

import leer_xml
import OrganismoSingleton
import MuestraSingleton

lista_organismo = OrganismoSingleton.OrganismoSingleton.getInstance().listaOrganismo
lista_muestra = MuestraSingleton.MuestraSingleton.getInstance().listaMuestra

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

if not file_path.endswith('.xml'):
    print('El archivo no es un xml')
else:
    leer_xml.leer_xml(file_path)
    for key, value in lista_organismo.mostrar().items():
        print(key, ':', value)
    for key, value in lista_muestra.mostrar().items():
        print(key, ':', value)