import os
from List_access import MuestraSingleton, OrganismoSingleton

lista_muestra = MuestraSingleton.MuestraSingleton.getInstance().listaMuestra
lista_organismo = OrganismoSingleton.OrganismoSingleton.getInstance().listaOrganismo

def generar_grafica(codigo):
    muestra = lista_muestra.obtener_muestra(codigo)
    if not muestra:
        print(f'No se encontro la muestra con el codigo {codigo}')
        return
    celdas_vivas = muestra.listado_celda_viva
    with open(f'Tablero_{codigo}.dot',mode="w") as grafica:
        grafica.write('digraph Peliculas{\n')
        grafica.write('\trankdir=LR;\n')
        grafica.write('\tfontname="Helvetica,Arial,sans-serif"\n')
        grafica.write('\tnode [fontname="Helvetica,Arial,sans-serif"]\n')
        grafica.write('\tedge [fontname="Helvetica,Arial,sans-serif"]\n')
        grafica.write('\ta0 [shape=none label=<\n')
        grafica.write('\t<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="8" CELLPADDING="8">\n')
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
                            grafica.write(f'\t\t\t<TD style="radial" bgcolor="#F7F7FF:#B9C0DA"> {i}, {j} </TD>\n')
                        else:
                            grafica.write(f'\t\t\t<TD style="radial" bgcolor="{organismo.color}"></TD>\n')
                    if j+1 == int(muestra.columnas) and contador_columnas_vacias > 0:
                        grafica.write(f'\t\t\t<TD bgcolor="#F7F7FF:#B9C0DA" gradientangle="90" colspan="{contador_columnas_vacias}"> ... </TD>\n')
            grafica.write('\t\t</TR>\n')
        grafica.write('\t</TABLE>>];\n')
        for i in range(lista_organismo.tamano()):
            organismo = lista_organismo.recorrer(i)
            grafica.write(f'\tsubgraph row_{i}{{\n')
            grafica.write(f'\t\tb{i} [shape=rectangle color="{organismo.color}" style=filled label=""];\n')
            grafica.write(f'\t\t{organismo.codigo} [shape=none label="{organismo.nombre}"]\n')
            grafica.write('\t}\n')
        for i in range(lista_organismo.tamano()):
            organismo = lista_organismo.recorrer(i)
            organismo2 = lista_organismo.recorrer(i+1)
            if i == 0:
                grafica.write('\ta0 -> b0 [style=invis]\n')
                grafica.write(f'\ta0 -> {organismo.codigo} [style=invis]\n')
                grafica.write('\tb0 -> b1 [style=invis]\n')
                grafica.write(f'\t{organismo.codigo} -> {organismo2.codigo} [style=invis]\n')
            else:
                if organismo2 != None:
                    grafica.write(f'\tb{i} -> b{i+1} [style=invis]\n')
                    grafica.write(f'\t{organismo.codigo} -> {organismo2.codigo} [style=invis]\n')
        grafica.write('}\n')
        grafica.close()
    
    os.system(f'dot -Tpng Tablero_{codigo}.dot -o Grafica_{codigo}.png')
    os.system(f'start Grafica_{codigo}.png')