import tkinter as tk
from tkinter import filedialog
from Controllers import leer_xml, graficar_muestra, agregar_celula

import OrganismoSingleton
import MuestraSingleton


lista_organismo = OrganismoSingleton.OrganismoSingleton.getInstance().listaOrganismo
lista_muestra = MuestraSingleton.MuestraSingleton.getInstance().listaMuestra


def cargar_archivo():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if not file_path.endswith('.xml'):
        print('El archivo no es un xml')
    else:
        leer_xml.leer_xml(file_path)

def gestionar_muestras():
    while True:
        print()
        print("1. Ver Muestras ")
        print("2. Graficar Muestra")
        print('3. Agregar Celula')
        print("4. Regresar")
        print()
        
        subopcion = input("Ingresa una opcion: ")
        print()

        if subopcion == "1":
            print("Muestras:")
            print()
            for objeto in lista_muestra.mostrar():
                for key, value in objeto.items():
                    print(key, ':', value)
            print()
        elif subopcion == "2":
            print()
            muestra = input("Codigo de muestra: ")
            print()
            graficar_muestra.generar_grafica(muestra)
        elif subopcion == "3":
            print()
            muestra = input("Codigo de muestra: ")
            print()
            for objeto in lista_organismo.mostrar():
                for key, value in objeto.items():
                    print(key, ':', value)
            print()
            organismo = input("Codigo de organismo: ")
            print()
            agregar_celula.agregar_celula(muestra, organismo)
        elif subopcion == "4":
            print("Regresando al menu principal")
            break
        else:
            print("Por favor elige una opcion del menu.")


while True:
    print()
    print("Elige una opcion por favor:")
    print()
    print("1. Cargar archivo de entrada: ")
    print("2. Gestionar peliculas")
    print("3. Filtrado")
    print("4. Grafica")
    print("5. Salir")
    print()

    opcion = input("Ingresa una opcion: ")
    print()

    if opcion == "1":
        print("Cargando archivo de entrada: ")
        print()
        cargar_archivo()
    elif opcion == "2":
        print("Gestiona Muestras:")
        gestionar_muestras()
    elif opcion == "3":
        print("Filtros:")
    elif opcion == "4":
        print("Crear Grafica")
    elif opcion == "5":
        print("Adios!")
        break
    else:
        print("Por favor elige una opcion del menu.")
