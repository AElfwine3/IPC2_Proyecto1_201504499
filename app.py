import tkinter as tk
from tkinter import filedialog
from Controllers import leer_xml, graficar_muestra

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
    for objeto in lista_organismo.mostrar():
        for key, value in objeto.items():
            print(key, ':', value)
    for objeto in lista_muestra.mostrar():
        for key, value in objeto.items():
            print(key, ':', value)
    graficar_muestra.generar_grafica('A03')