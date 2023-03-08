import tkinter as tk
from tkinter import filedialog
from Controllers import leer_xml, graficar_muestra, agregar_celula, escribir_xml
from List_access import OrganismoSingleton, MuestraSingleton

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
    if lista_muestra.tamano() == 0 and lista_organismo.tamano() == 0:
        print('No hay muestras cargadas')
        return
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
            agregar_celula.prosperar_celula(muestra, organismo)
            print()
            agregar = input('Desea Agregar esta celula? (S/N)')
            print()
            if agregar == 'S':
                fila = input('Fila: ')
                columna = input('Columna: ')
                agregar_celula.agregar_celula(muestra, organismo, fila, columna)
            else:
                print('No se agrego la celula')
            print()
        elif subopcion == "4":
            print("Regresando al menu principal")
            break
        else:
            print("Por favor elige una opcion del menu.")

def guardar_xml():
    escribir_xml.escribir_xml(lista_organismo, lista_muestra)


while True:
    print()
    print("Elige una opcion por favor:")
    print()
    print("1. Cargar archivo de entrada")
    print("2. Gestionar Muestras")
    print("3. Guardar cambios")
    print("4. Salir")
    print()
    opcion = input("Ingresa una opcion: ")
    print()
    if opcion == "1":
        print("Cargando archivo de entrada: ")
        print()
        cargar_archivo()
    elif opcion == "2":
        print("Gestionando Muestras:")
        gestionar_muestras()
    elif opcion == "3":
        print("Guardando XML:")
        guardar_xml()
    elif opcion == "4":
        print("Adios!")
        break
    else:
        print("Por favor elige una opcion del menu.")
