#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy, sys, os
reload(sys)
sys.setdefaultencoding('utf-8')

# Carpeta donde se creara el GDB "Catastro Fiscal"
#*-*-*-*-*-*-*-*-*-*-
path_file=r"C:\Users\JULIO_CRUZ\Documents\ArcGIS\GDB_temporal"  # <<<<<<<<<
# *-*-*-*-*-*-*-*-*-*-

# Creación de GDB Principal <<<<<<<<<
GDB=arcpy.CreateFileGDB_management(path_file, "Catastro_Fiscal")

# Creacion de Dataset's
list_datasets=[("CARTO_FISCAL_17", 32717), ("CARTO_FISCAL_18", 32718), ("CARTO_FISCAL_19", 32719),
               ("CARTOGRAFIA_BASE", 4326), ("CARTOGRAFIA_TEMATICA", 4326)]
for i in list_datasets:
    print "Creating Dataset's... {}".format(i[0])
    arcpy.CreateFeatureDataset_management(str(GDB), "{}".format(i[0]), "{}".format(i[1]))

# Creacion de Capas, en cada dataset
lista_fc_tematica_INEI = [("CTF_ZONA_INEI", "POLYGON"), ("CTF_MANZANA_INEI", "POLYGON"), ("CTF_EJE_VIAL", "POLYLINE"), ("CTF_FRENTE_INEI", "POLYLINE"),
                          ("DIRECCION", "POINT")] #("CTF_PUERTA","POINT") #>> Capa CFT_PUERTA se va por redundar en informacion
lista_fc_base_INEI = [("TB_DEPARTAMENTO", "POLYGON"), ("TB_PROVINCIA", "POLYGON"), ("TB_DISTRITO", "POLYGON")]
lista_fc_carto_fiscal = [("CF_UNIDADES_URBANAS", "POLYGON"), ("CF_PARQUES", "POLYGON"), ("CF_SECTOR", "POLYGON"), ("VL_ARANCEL", "POLYLINE"),
                         ("CF_ARANCEL", "POLYLINE"), ("CF_EJE_VIAL", "POLYLINE"), ("CF_SEG_VIAL", "POLYLINE"), ("CF_MANZANA_URB", "POLYGON"), ("CF_MANZANA_CAT", "POLYGON"),
                         ("CF_LOTES_POL", "POLYGON"), ("CF_LOTES_PUN", "POINT"), ("CF_PREDIO", "POINT"), ("CF_NUMERACION", "POINT")]

for r in list_datasets:
    print "Creating features class in {}".format(r[0])
    if "CARTO_FISCAL_17" == r[0]:
        for i in lista_fc_carto_fiscal:
            arcpy.CreateFeatureclass_management(os.path.join(path_file, str(GDB), r[0]), "{}_17".format(i[0]),
                                                "{}".format(i[1]), "", "DISABLED", "DISABLED", "", "", "0", "0", "0")
    elif "CARTO_FISCAL_18" == r[0]:
        for i in lista_fc_carto_fiscal:
            arcpy.CreateFeatureclass_management(os.path.join(path_file, str(GDB), r[0]), "{}_18".format(i[0]),
                                                "{}".format(i[1]), "", "DISABLED", "DISABLED", "", "", "0", "0", "0")
    elif "CARTO_FISCAL_19" == r[0]:
        for i in lista_fc_carto_fiscal:
            arcpy.CreateFeatureclass_management(os.path.join(path_file, str(GDB), r[0]), "{}_19".format(i[0]),
                                                "{}".format(i[1]), "", "DISABLED", "DISABLED", "", "", "0", "0", "0")
    elif r[0]== "CARTOGRAFIA_TEMATICA":
        for i in lista_fc_tematica_INEI:
            arcpy.CreateFeatureclass_management(os.path.join(path_file, str(GDB), r[0]), "{}".format(i[0]),
                                                "{}".format(i[1]), "", "DISABLED", "DISABLED", "", "", "0", "0", "0")
    elif r[0]== "CARTOGRAFIA_BASE":
        for i in lista_fc_base_INEI:
            arcpy.CreateFeatureclass_management(os.path.join(path_file, str(GDB), r[0]), "{}".format(i[0]),
                                                "{}".format(i[1]), "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

arcpy.CreateTable_management(str(GDB), "TB_PREDIO_T")
arcpy.CreateTable_management(str(GDB), "TB_PUNTO_IMG")
