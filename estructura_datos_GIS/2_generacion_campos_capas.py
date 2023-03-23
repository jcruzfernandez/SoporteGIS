#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy, sys, os
reload(sys)
sys.setdefaultencoding('utf-8')

error="Error adding Field..."
# Funciones de creacion de campos para cada capa del GDB
##

def TB_DEPARTAMENTO(fc):
    arcpy.AddField_management(fc, "ID_DPTO", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "CODDPTO", "TEXT", "", "", "2", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "NOMDPTO", "TEXT", "", "", "250", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "FUENTE", "TEXT", "", "", "250", "", "NULLABLE", "NON_REQUIRED", "")


def TB_PROVINCIA(fc):
    arcpy.AddField_management(fc, "ID_PROV", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "CODDPTO", "TEXT", "", "", "2", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc,"CODPROV", "TEXT", "", "", "2", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "NOMDPTO", "TEXT", "", "", "250", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "NOMPROV", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "FUENTE", "TEXT", "", "", "250", "", "NULLABLE", "NON_REQUIRED", "")


def TB_DISTRITO(fc):
    arcpy.AddField_management(fc, "ID_DIST", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields=[("CODDPTO",2),("CODPROV",2),("CODDIST",2),("NOMDPTO",250),("NOMPROV",250), ("NOMDIST",250),("UBIGEO",6),
            ("FUENTE",250)]   #>>("CATMEF",1)  Se saco de la lista de campos
    for field in fields:
        arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE", "NON_REQUIRED", "")


def CTF_ZONA_INEI(fc):
    # arcpy.AddField_management(fc, "ID_MZN_INEI", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("IDZONA",11), ("COD_DPTO", 2), ("COD_PROV", 2), ("COD_DIST", 2), ("UBIGEO", 6), ("IDCCPP", 10), ("NOMCCPP", 255), ("ANO_CART", 4), ("FUENTE", 255)]
    for field in fields:
        try:
            arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                      "NON_REQUIRED", "")
        except:
            pass

def CTF_EJE_VIAL(fc):
    # arcpy.AddField_management(fc, "ID_SEG_VIA", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields=[("ID_SVIA", 20), ("UBIGEO", 6), ("COD_VIA", 4), ("COD_SECT", 2), ("COD_SEGM", 4), ("TIP_VIA", 20), ("NOM_VIA", 255), ("CUADRA", 4), ("FUENTE", 255)]
    for field in fields:
        try:
            arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE", "NON_REQUIRED", "")
        except: pass

def CTF_MANZANA_INEI(fc):
    # arcpy.AddField_management(fc, "ID_MZN_INEI", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("IDMZINEI", 15), ("UBIGEO", 6), ("COD_SECT", 2), ("COD_MZN", 4), ("COD_ZONA", 5), ("MZ_INEI", 4), ("AÑO_CAT", 4), ("FUENTE", 255)]
    for field in fields:
        try:
            arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                      "NON_REQUIRED", "")
        except:
            print error

def CTF_FRENTE_INEI(fc):
    # arcpy.AddField_management(fc, "ID_FRENTE_INEI", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("IDFRINEI",18), ("UBIGEO", 6), ("COD_SECT", 2),("COD_ZONA", 5), ("MZ_INEI", 4),("FRENTE", 2), ("CUADRA", 4), ("ID_SVIA", 20),
             ("ANO_CAT", 4), ("FUENTE", 255), ("COD_VIA", 4), ("VAL_ACT", 6)]
    for field in fields:
        try:
            arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                      "NON_REQUIRED", "")
        except:
            print error

def DIRECCION(fc):
    # arcpy.AddField_management(fc, "ID_DIREC", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("ID_DIREC", 20), ("UBIGEO", 6), ("NOM_DIST",255), ("TIP_VIA",20), ("NOM_VIA",255), ("NUM_MUN",10),("NOM_UU",255),
             ("MZN_URB", 4),("LOT_URB", 5), ("DIR_MUN", 255), ("ID_FRENT", 20),("REFEREN", 255), ("FUENTE",255)]
    for field in fields:
        try:
            arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                      "NON_REQUIRED", "")
        except:
            print error

"""
####### CAPA CTF_PUERTA SE ELIMINA DE LA ESTRUCTURA POR REDUNDAR EN INFORMACION ######
def CTF_PUERTA(fc):
    arcpy.AddField_management(fc, "ID_PUERT", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields=[("UBIGEO",6),("COD_SECT",2), ("MZ_INEI", 4), ("FRENTE", 255),("NUM_PUER",255), ("FUENTE",255),("AÑO_CAT", 4),("DIRECCION", 255)]
    for field in fields:
        try:
            arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE", "NON_REQUIRED", "")
        except: pass
"""

def CF_PARQUES(fc):
    arcpy.AddField_management(fc, "ID_PARQ", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("UBIGEO", 6), ("COD_SECT", 2), ("MZN_URB", 10), ("COD_MZN", 3), ("TIP_PARQ", 10), ("NOM_PARQ", 250), ("FUENTE", 255)]
    for field in fields:
        try:
            arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                      "NON_REQUIRED", "")
        except:
            print error + field[0]

def CF_SECTOR(fc):
    arcpy.AddField_management(fc, "ID_SECT", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("UBIGEO", 6), ("COD_SECT", 2), ("FUENTE", 255)]
    for field in fields:
        try:
            arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                      "NON_REQUIRED", "")
        except:
            print error + field[0]

def CF_UNIDADES_URBANAS(fc):
    arcpy.AddField_management(fc, "ID_URB", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("UBIGEO", 6), ("COD_UU", 4), ("NOM_UU", 255), ("NOM_REF", 255), ("TIPO_UU", 2), ("ABR_TUU", 2),
             ("PARTIDA", 20), ("TIP_RES", 20), ("RESOLU", 120), ("CONDIC", 1), ("FUENTE", 255)]
    for field in fields:
        try:
            arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE", "NON_REQUIRED", "")
        except:
            print error + field[0]

def CF_ARANCEL(fc):
    arcpy.AddField_management(fc, "ID_ARANC", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("UBIGEO", 6), ("SEC_EJEC", "LONG", 1), ("COD_UU", 4), ("COD_SECT", 2), ("COD_MZN", 3), ("F_MZN", 2), ("MZN_URB", 10),
              ("DIS_PAR", 2), ("COD_VIA", 4), ("TIP_VIA", 2), ("NOM_VIA", 255), ("NOM_ALT", 255), ("LADO", 1),
              ("CUADRA", 4), ("ANO_EJEC", 6), ("VAL_ACT", ), ("ID_SVIA", "LONG", 1), ("TIP_RES", 20), ("RESOLU", 120), ("CONDIC", 1),
              ("COLING", 1), ("FUENTE", 255), ("ID_CL", "LONG", 1)]
    for field in fields:
        if len(field) == 2:
            try:
                arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                          "NON_REQUIRED", "")
            except:
                print error + field[0]
        elif len(field) == 3 and field[1] == 'INT':
            arcpy.AddField_management(fc, "{}".format(field[0]), "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        elif len(field) == 3 and field[1] == 'LONG':
            arcpy.AddField_management(fc, "{}".format(field[0]), "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        else:
            arcpy.AddField_management(fc, "{}".format(field[0]), "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

def VL_ARANCEL(fc):
    arcpy.AddField_management(fc, "ID_ARANC", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "SECUEN", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("UBIGEO", 6), ("COD_SECT", 2), ("COD_MZN", 3), ("F_MZN", 2), ("TIP_VIA", 2), ("NOM_VIA", 255),
              ("NOM_ALT", 255), ("CUADRA", 4), ("ANO", 4), ("VAL_ACT", ), ("LADO", 1), ("TIP_RES", 20), ("RESOLU", 120),
              ("CONDIC", 1), ("FUENTE", 255)]
    for field in fields:
        if len(field) == 2:
            try:
                arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                          "NON_REQUIRED", "")
            except:
                print error + field[0]
        else:
            arcpy.AddField_management(fc, "{}".format(field[0]), "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

def CF_EJE_VIAL(fc):
    arcpy.AddField_management(fc, "ID_VIA", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("UBIGEO", 6), ("COD_VIA", 4), ("ABR_TVIA", 10), ("TIP_VIA", 2), ("DES_VIA", 6), ("NOM_VIA", 255),
              ("NOM_ALT", 255), ("CANT_SEG", 4), ("CONDIC", 1), ("C_INI", "INT", 1), ("C_FIN", "INT", 1), ("FUENTE", 255)]
    for field in fields:
        if len(field) == 2:
            try:
                arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE", "NON_REQUIRED", "")
            except: print error + field[0]
        elif len(field) == 3 and field[1] == 'INT':
            arcpy.AddField_management(fc, "{}".format(field[0]), "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        elif len(field) == 3 and field[1] == 'LONG':
            arcpy.AddField_management(fc, "{}".format(field[0]), "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        else:
            arcpy.AddField_management(fc, "{}".format(field[0]), "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

def CF_SEG_VIAL(fc):
    arcpy.AddField_management(fc, "ID_SVIA", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ID_VIA", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("UBIGEO", 6), ("COD_VIA", 4), ("COD_SECT", 2), ("COD_SEGM", 4), ("DES_VIA", 6), ("ABR_TVIA", 10),
              ("TIP_VIA", 2), ("NOM_VIA", 255), ("NOM_ALT", 255), ("CUADRA", 4), ("FUENTE", 255)]
    for field in fields:
        if len(field) == 2:
            try:
                arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE", "NON_REQUIRED", "")
            except: print error + field[0]
        else:
            arcpy.AddField_management(fc, "{}".format(field[0]), "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")


def CF_MANZANA_URB(fc):
    arcpy.AddField_management(fc, "ID_MZN_U", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("UBIGEO", 6), ("COD_SECT", 2), ("COD_MZN", 3), ("MZN_URB", 10), ("COD_UU", 4), ("TIPO_UU", 2), ("NOM_UU", 255),
              ("NOM_REF", 255), ("ANO_CART", 4), ("FUENTE", 255)]
    for field in fields:
        try:
            arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                      "NON_REQUIRED", "")
        except:
            print error + field[0]

def CF_MANZANA_CAT(fc):
    arcpy.AddField_management(fc, "ID_MZN_C", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("UBIGEO", 6), ("COD_SECT", 2), ("COD_MZN", 3), ("ANO_CART", 4), ("FUENTE", 255)]
    for field in fields:
        try:
            arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                      "NON_REQUIRED", "")
        except:
            print error + field[0]

def CF_LOTES_POL(fc):
    arcpy.AddField_management(fc, "ID_LOTE_P", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("UBIGEO", 6), ("COD_SECT", 2), ("COD_MZN", 3), ("COD_LOTE", 3), ("COD_UU", 4), ("COD_VIA", 4), ("TIPO_UU", 2),("NOM_UU", 255),
              ("NOM_REF", 255), ("MZN_URB", 10), ("LOT_URB", 15), ("TIP_VIA", 2), ("NOM_VIA", 255), ("NUM_MUN", 10), ("NOM_ALT", 255), ("BLOCK", 6),
              ("NUM_DEP", 6), ("INTERIOR", 5), ("PISO", 2), ("KM", 4), ("REFEREN", 255), ("RAM_NUM", 50), ("CUADRA", 4), ("LADO", 1), ("PARTIDA", 20),
              ("TIP_LOT", 1), ("ANO_CART", 4), ("FUENTE", 255), ("ID_ARANC", "LONG", 1), ("COORD_X",), ("COORD_Y",), ("ID_IMG", 25),
              ("RAN_CPU", "LONG", 1), ("R_CPU_A", "LONG", 1)]
    for field in fields:
        if len(field) == 2:
            try:
                arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE", "NON_REQUIRED", "")
            except:
                print error + field[0]
        elif len(field) == 3 and field[1] == 'INT':
            arcpy.AddField_management(fc, "{}".format(field[0]), "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        elif len(field) == 3 and field[1] == 'LONG':
            arcpy.AddField_management(fc, "{}".format(field[0]), "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        else:
            arcpy.AddField_management(fc, "{}".format(field[0]), "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

def CF_LOTES_PUN(fc):
    arcpy.AddField_management(fc, "ID_LOTE", "TEXT", "", "", "25", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ID_LOTE_P", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "RAN_CPU", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "SECUEN", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("UBIGEO", 6), ("COD_SECT", 2), ("COD_MZN", 3), ("COD_LOTE", 3), ("COD_UU", 4), ("COD_VIA", 4), ("TIPO_UU", 2), ("NOM_UU", 255),
              ("NOM_REF", 255), ("MZN_URB", 10), ("LOT_URB", 15), ("TIP_VIA", 2), ("NOM_VIA", 255), ("NUM_MUN", 10), ("NOM_ALT", 255), ("BLOCK", 6),
              ("NUM_DEP", 6), ("INTERIOR", 5), ("PISO", 2), ("KM", 4), ("REFEREN", 255), ("RAM_NUM", 50), ("CUADRA", 4), ("LADO", 1), ("PARTIDA", 20),
              ("TIP_LOT", 1), ("ANO_CART", 4), ("FUENTE", 255), ("ID_ARANC", "LONG", 1), ("COORD_X",), ("COORD_Y",), ("ID_IMG", 25), ("VAL_ACT",),
              ("R_CPU_A", "LONG", 1)]
    for field in fields:
        if len(field) == 2:
            try:
                arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE", "NON_REQUIRED", "")
            except:
                print error + field[0]
        elif len(field) == 3 and field[1] == 'INT':
            arcpy.AddField_management(fc, "{}".format(field[0]), "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        elif len(field) == 3 and field[1] == 'LONG':
            arcpy.AddField_management(fc, "{}".format(field[0]), "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        else:
            arcpy.AddField_management(fc, "{}".format(field[0]), "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")


def CF_PREDIO(fc):
    arcpy.AddField_management(fc, "ID_PRED", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ID_LOTE_P", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("UBIGEO", 6), ("SEC_EJEC", "LONG", 1), ("COD_PRE", 100), ("COD_CPU", 15), ("ID_ARANC", "LONG", 1), ("ID_LOTE", "LONG", 1), ("COD_SECT", 2), ("COD_MZN", 3),
              ("COD_LOTE", 3), ("COD_UU", 4), ("COD_VIA", 4), ("TIPO_UU", 2), ("NOM_UU", 255), ("NOM_REF", 255), ("MZN_URB", 10), ("LOT_URB", 5),
              ("TIP_VIA", 2), ("NOM_VIA", 255), ("NOM_ALT", 255), ("NUM_MUN", 10), ("NUM_ALT", 100), ("BLOCK", 6), ("NUM_DEP", 6), ("INTERIOR", 5),
              ("PISO", 2), ("KM", 4), ("REFEREN", 255), ("CUADRA", 4), ("LADO", 1), ("DIR_MUN", 255), ("DIR_URB", 255), ("PARTIDA", 20),
              ("ANO_CART", 4), ("FUENTE", 255), ("COORD_X",), ("COORD_Y",), ("COD_CUC", 12), ("ESTADO", 1)]
    for field in fields:
        if len(field) == 2:
            try:
                arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                          "NON_REQUIRED", "")
            except:
                print error + field[0]
        elif len(field) == 3 and field[1] == 'INT':
            arcpy.AddField_management(fc, "{}".format(field[0]), "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        elif len(field) == 3 and field[1] == 'LONG':
            arcpy.AddField_management(fc, "{}".format(field[0]), "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        else:
            arcpy.AddField_management(fc, "{}".format(field[0]), "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "FOTO", "RASTER", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "VAL_ACT", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "RAN_CPU", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "COD_UI", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "COD_VER", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

def CF_NUMERACION(fc):
    arcpy.AddField_management(fc, "ID_NUM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ID_LOTE_P", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "RAN_CPU", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("UBIGEO", 6), ("COD_SECT", 2), ("COD_MZN", 3), ("COD_LOTE", 3), ("COD_UU", 4), ("COD_VIA", 4), ("TIPO_UU", 2), ("NOM_UU", 255),
              ("NOM_REF", 255), ("MZN_URB", 10), ("LOT_URB", 15), ("TIP_VIA", 2), ("NOM_VIA", 255), ("TIP_PUER", 1), ("NUM_MUN", 10),
              ("NOM_ALT", 255), ("BLOCK", 6), ("N_DEP", 6), ("INTERIOR", 5), ("PISO", 2), ("KM", 4), ("REFEREN", 255), ("RAM_NUM", 50),
              ("CUADRA", 4), ("LADO", 1), ("PARTIDA", 20), ("ANO_CART", 4), ("FUENTE", 255), ("ID_ARANC", "LONG", 1), ("COORD_X",), ("COORD_Y",)]
    for field in fields:
        if len(field) == 2:
            try:
                arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                          "NON_REQUIRED", "")
            except:
                print error + field[0]
        elif len(field) == 3 and field[1] == 'INT':
            arcpy.AddField_management(fc, "{}".format(field[0]), "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        elif len(field) == 3 and field[1] == 'LONG':
            arcpy.AddField_management(fc, "{}".format(field[0]), "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        else:
            arcpy.AddField_management(fc, "{}".format(field[0]), "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

def TB_PREDIO_T(fc):
    arcpy.AddField_management(fc, "ID_PRED", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("COD_PRE", 100), ("SEC_EJEC", "LONG", 1), ("UBIGEO", 6), ("ID_LOTE", 18), ("COD_CPU", 15), ("COD_SECT", 2), ("COD_UU", 4), ("COD_MZN", 3),
              ("COD_LOTE", 5), ("COD_CUC", 18), ("TIPO_UU", 2), ("NOM_UU", 255), ("NOM_REF", 255), ("MZN_URB", 10), ("LOT_URB", 10),
              ("TIP_VIA", 2), ("NOM_VIA", 255), ("NOM_ALT", 255), ("NUM_MUN", 10), ("NUM_ALT", 100), ("BLOCK", 6), ("NUM_DEP", 6), ("INTERIOR", 5),
              ("PISO", 2), ("KM", 4), ("REFERENCIA", 250), ("DIR_MUN", 255), ("DIR_URB", 255), ("DIR_ASIG", 255), ("COORD_X",), ("COORD_Y",),
              ("ID_ARANC", "LONG", 1), ("TIP_DOC", 2), ("DOC_IDEN", 15), ("COD_CONTR", 15), ("NOMBRE", 250), ("AP_PAT", 250), ("AP_MAT", 250), ("CONTRIBUYENTE", 255),
              ("DIR_FISCAL", 250), ("ESTADO", 1), ("Area_terrano", ), ("Area_construida",), ("Longitud_frente",), ("DIS_PAR", 2), ("Grupo_uso_desc", 50),
              ("Cantidad_habitantes", "LONG", 1), ("Clasificacion_predio_desc", 90), ("Estado_construccion_desc", 120), ("Tipo_predio", 20), ("Autoavaluo_total",),
              ("Condominio",), ("Deduccion",), ("Autoavaluo_afecto",), ("FUENTE", 255), ("TDOC_RES", 2), ("NDOC_RES", 255), ("L_FOTO", 255), ("ID_IMG", 25), ("ESTADO_P", 1),
              ("VAL_ACT", ), ("COD_UI", "LONG", 1), ("COD_VER", "LONG", 1)]
    for field in fields:
        if len(field) == 2:
            try:
                arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                          "NON_REQUIRED", "")
            except:
                print error + field[0]
        elif len(field) == 3 and field[1] == 'INT':
            arcpy.AddField_management(fc, "{}".format(field[0]), "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        elif len(field) == 3 and field[1] == 'LONG':
            arcpy.AddField_management(fc, "{}".format(field[0]), "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        else:
            arcpy.AddField_management(fc, "{}".format(field[0]), "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "VAL_ACT", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "RAN_CPU", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "COD_UI", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "COD_VER", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")


def TB_PUNTO_IMG(fc):
    arcpy.AddField_management(fc, "ID_IMG", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ID_PRED", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "SEC_EJEC", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "ZONA_UTM", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.AddField_management(fc, "SECUEN", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    fields = [("COD_PRE", 100), ("UBIGEO", 6), ("COD_CPU", 15), ("ID_LOTE", 18), ("COD_CUC", 18), ("TIPO_UU", 2), ("NOM_UU", 255), ("NOM_REF", 255),
              ("MZN_URB", 10), ("LOT_URB", 10), ("TIP_VIA", 2), ("NOM_VIA", 255), ("NOM_ALT", 255), ("NUM_MUN", 10), ("BLOCK", 6), ("NUM_DEP", 6), ("INTERIOR", 5),
              ("PISO", 2), ("KM", 4), ("REFERENCIA", 250), ("DIR_MUN", 255), ("DIR_URB", 255), ("DIR_ASIG", 255), ("COORD_X",), ("COORD_Y",),
              ("ID_ARANC", "LONG", 1), ("TIP_DOC", 2), ("DOC_IDEN", 15), ("COD_CONTR", 15), ("NOMBRE", 250), ("AP_PAT", 250), ("AP_MAT", 250), ("CONTRIBUYENTE", 255),
              ("DIR_FISCAL", 250), ("ESTADO", 1), ("Area_terrano", ), ("Longitud_frente",), ("DIS_PAR", 2), ("Grupo_uso_desc", 50),
              ("Cantidad_habitantes", "LONG", 1), ("Clasificacion_predio_desc", 90), ("Estado_construccion_desc", 120), ("Tipo_predio", 20), ("Autoavaluo_total",),
              ("Condominio",), ("Deduccion",), ("Autoavaluo_afecto",), ("FUENTE", 255), ("TDOC_RES", 2), ("NDOC_RES", 255), ("VAL_ACT",)]
    for field in fields:
        if len(field) == 2:
            try:
                arcpy.AddField_management(fc, "{}".format(field[0]), "TEXT", "", "", "{}".format(field[1]), "", "NULLABLE",
                                          "NON_REQUIRED", "")
            except:
                print error + field[0]
        elif len(field) == 3 and field[1] == 'INT':
            arcpy.AddField_management(fc, "{}".format(field[0]), "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        elif len(field) == 3 and field[1] == 'LONG':
            arcpy.AddField_management(fc, "{}".format(field[0]), "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        else:
            arcpy.AddField_management(fc, "{}".format(field[0]), "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")


# Ruta del GDB creado: "Catastro Fiscal"
workspace = r"C:\Users\JULIO_CRUZ\Documents\ArcGIS\GDB_temporal\Catastro_Fiscal.gdb"

# Creacion de todos los campos
walk = arcpy.da.Walk(workspace)  # , datatype="FeatureClass")
for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        path_fc = os.path.join(dirpath, filename)
        print "adding fields in... {}".format(filename)
        if "17" in filename or "18" in filename or "19" in filename:
            exec(r"{}(r'{}')".format(filename[:-3], path_fc))
        else:
            exec(r"{}(r'{}')".format(filename, path_fc))

# fc1=r"C:\Users\JULIO\Documents\ArcGIS\Default.gdb\Export_Output"
#
# DIRECCION(fc1)
# CTF_FRENTE_INEI()
# CTF_MANZANA_INEI()
