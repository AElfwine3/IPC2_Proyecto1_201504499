import os
import MuestraSingleton
import OrganismoSingleton

lista_muestra = MuestraSingleton.MuestraSingleton.getInstance().listaMuestra
lista_organismo = OrganismoSingleton.OrganismoSingleton.getInstance().listaOrganismo

def generar_grafica(codigo):
    muestra = lista_muestra.obtener_muestra(codigo)
    celdas_vivas = muestra.listado_celda_viva
    with open(f'Tablero_{codigo}.dot',mode="w") as grafica:
        grafica.write('digraph Peliculas{\n')
        grafica.write('\tfontname="Helvetica,Arial,sans-serif"\n')
        grafica.write('\tnode [fontname="Helvetica,Arial,sans-serif"]\n')
        grafica.write('\tedge [fontname="Helvetica,Arial,sans-serif"]\n')
        grafica.write('\ta0 [shape=none label=<\n')
        grafica.write('\t<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="8" CELLPADDING="8">\n')
        for i in range(int(muestra.filas)):
            grafica.write('\t\t<TR>\n')
            if not celdas_vivas.existe_fila(i):
                grafica.write(f'\t\t\t<TD bgcolor="#F7F7FF:#B9C0DA" gradientangle="90" colspan="{muestra.columnas}"> ... </TD>\n')
            else:
                contador_columnas_vacias = 0
                for j in range(int(muestra.columnas)):
                    if not celdas_vivas.is_celda_viva(i, j):
                        contador_columnas_vacias += 1
                    else:
                        if contador_columnas_vacias > 0:
                            grafica.write(f'\t\t\t<TD bgcolor="#F7F7FF:#B9C0DA" gradientangle="90" colspan="{contador_columnas_vacias}"> ... </TD>\n')
                        contador_columnas_vacias = 0
                        organismo = lista_organismo.obtener_organismo(celdas_vivas.codigo_organismo(i, j))
                        if organismo == None:
                            grafica.write(f'\t\t\t<TD style="radial" bgcolor="#F7F7FF:#B9C0DA"> {i}{j} </TD>\n')
                        else:
                            grafica.write(f'\t\t\t<TD style="radial" bgcolor="{organismo.color}"> {i}{j} </TD>\n')
                    if j+1 == int(muestra.columnas) and contador_columnas_vacias > 0:
                        grafica.write(f'\t\t\t<TD bgcolor="#F7F7FF:#B9C0DA" gradientangle="90" colspan="{contador_columnas_vacias}"> ... </TD>\n')
            grafica.write('\t\t</TR>\n')
        grafica.write('\t</TABLE>>];\n')
        grafica.write('}\n')
        grafica.close()
    
    os.system(f'dot -Tpng Tablero_{codigo}.dot -o Grafica_{codigo}.png')
    os.system(f'start Grafica_{codigo}.png')