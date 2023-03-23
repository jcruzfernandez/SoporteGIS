#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy, sys, os, unicodedata

reload(sys)
sys.setdefaultencoding('utf-8')

# Diccionarios de los dominios a crear
dominios = {"TIPO_UU": "CODIGO DEL TIPO O CATEGORIA DE LA UNIDAD URBANA",
            "ABRE_UU": "ABREVIATURA DE LAS CATEGORIAS DE UNIDADES URBANAS",
            "LADO": "LADO DE LA CUADRA", "COD_VIA": "CODIGO DEL TIPO DE VIA",
            "COLINDANCIA": "TIPO DE COLINDANCIA", "TIPO_LOTE": "TIPO DE LOTE",
            "ABRE_TIPVIA": "ABREVIATURA DEL TIPO DE VIA", "ESTADO": "ACTIVO O INACTIVO",
            "DIS_PAR": "DISTANCIA A AREAS VERDES", "CONDICION": "FORMAL O INFORMAL",
            "TIPO_PREDIO": "TIPO DE PREDIO", "TIPO_INGRESO": "TIPO DE INGRESO PRINCIPAL",
            "ESTADO_UBI": "UBICADO O INUBICADO", "TIPO_DOC": "TIPO DE DOCUMENTO"}

# Codigos y valores que seran asignados a las capas correspondientes
values_TIPO_UU = {"01": "ASENTAMIENTO HUMANO",
                  "02": "AGRUPACION",
                  "03": "CONJUNTO HABITACIONAL",
                  "04": "CONJUNTO RESIDENCIAL",
                  "05": "PUEBLO JOVEN",
                  "06": "URBANIZACION",
                  "07": "URBANIZACION POPULAR",
                  "08": "CERCADO",
                  "09": "HACIENDA",
                  "10": "ASOCIACION",
                  "11": "COOPERATIVA",
                  "12": "LOTIZACION",
                  "13": "PARCELA",
                  "14": "VALLE",
                  "15": "CASERIO",
                  "16": "UNIDAD VECINAL",
                  "17": "COMUNIDAD",
                  "18": "BARRIO",
                  "19": "FUNDO",
                  "20": "JUNTA DE COMPRADORES",
                  "21": "ASOCIACION DE VIVIENDA",
                  "22": "COOPERATIVA DE VIVIENDA",
                  "23": "SOCIEDAD",
                  "24": "ASOCIACION PRO VIVIENDA",
                  "25": "ZONA",
                  "26": "CENTRO POBLADO",
                  "27": "ANEXO",
                  "28": "LUGAR",
                  "29": "REGION",
                  "30": "SECTOR",
                  "31": "PUEBLO TRADICIONAL",
                  "32": "ZONA URBANA",
                  "33": "URBANIZACION POPULAR DE INTERES SOCIAL",
                  "34": "CENTRO RECREACIONAL",
                  "35": "SIN HABILITACION SN"}

values_ABRE_UU = {"01": "AA.HH.",
                  "02": "AGRUP",
                  "03": "CONJ. HAB.",
                  "04": "C.R.",
                  "05": "P.J.",
                  "06": "URB.",
                  "07": "URB. POP.",
                  "08": "CER",
                  "09": "HCDA",
                  "10": "ASOC",
                  "11": "COOP",
                  "12": "LOT",
                  "13": "PARC",
                  "14": "VALL",
                  "15": "CAS",
                  "16": "U.V.",
                  "17": "C.",
                  "18": "BAR",
                  "19": "FDO",
                  "20": "JTA. COMP.",
                  "21": "ASOC. VIV.",
                  "22": "COOP. VIV.",
                  "23": "ASOC",
                  "24": "A.P.V.",
                  "25": "Z.",
                  "26": "C.P.",
                  "27": "A",
                  "28": "L.",
                  "29": "R.",
                  "30": "S.",
                  "31": "P.T.",
                  "32": "Z.U.",
                  "33": "UPIS",
                  "34": "C.R.",
                  "35": "Sin Hab. SN"}

values_LADO = {'1': "Izquierda", '2': "Derecha"}

values_COD_VIA = {"01": "AVENIDA",
                  "02": "CALLE",
                  "03": "JIRON",
                  "04": "PASAJE",
                  "05": "ALAMEDA",
                  "06": "CARRETERA",
                  "07": "PROLONGACION",
                  "08": "PASEO",
                  "09": "MALECON",
                  "10": "CAMINO",
                  "11": "PLAZA",
                  "12": "PLAZUELA"}

values_TIPO_PREDIO = {"U": "Urbano", "R": "Rural"}
values_TIPO_INGRESO = {"P": "Principal", "G": "Garaje"}

values_COLINDANCIA = {'1': "Predio Urbano",
                      '2': "Predio Rustico o Agricola",
                      '3': "Quebrada",
                      '4': "Canales o Similares",
                      '5': "Zona de Riesgo",
                      '6': "Rio"}

values_TIPO_LOTE = {'1': "Regular", '2': "Mediterraneo"}

values_ABRE_TIPVIA = {'01': 'AV',
                      '02': 'CA',
                      '03': 'JR',
                      '04': 'PJE',
                      '06': 'CARR',
                      '07': 'PRLG',
                      '10': 'C'}

values_DIS_PAR = {"01": "FRENTE A PARQUE",
                  "02": "FRENTE A BERMA AVENIDA",
                  "03": "MEDIANAMENTE CERCANO A AREAS VERDES",
                  "04": "OTRAS UBICACIONES LEJOS"}

values_CONDICION = {'1': "Formal", '2': "Informal"}

values_ESTADO = {'1': "Activo", '0': "Inactivo"}

values_ESTADO_UBI = {'1': "UBICADO", '0': "SIN UBICAR"}

values_TIPO_DOC = {'00': "S/N", '01': "DNI", "04": "CARNET DE EXTRANJERIA", "06": "RUC", "08": "SUCESION INTESTADA"}

# Ruta del GDB creado: "Catastro Fiscal" <<<<<<<<<
workspace = r"C:\Users\JULIO_CRUZ\Documents\ArcGIS\GDB_temporal\Catastro_Fiscal.gdb"


def domain():
    # Proceso: Creacion Dominios
    for dominio in dominios:
        print "Creating dominino: " + dominio
        arcpy.CreateDomain_management(workspace, "{}".format(dominio), "{}".format(dominios[dominio]), "TEXT", "CODED",
                                      "DEFAULT", "DEFAULT")
    # Proceso: Add Coded Value To Domain
    for i in arcpy.da.ListDomains(workspace):
        if i.name == "TIPO_UU":
            for d in values_TIPO_UU:
                arcpy.AddCodedValueToDomain_management(workspace, i.name, d, values_TIPO_UU[d])
        elif i.name == "ABRE_UU":
            for d in values_ABRE_UU:
                arcpy.AddCodedValueToDomain_management(workspace, i.name, d, values_ABRE_UU[d])
        elif i.name == "LADO":
            for d in values_LADO:
                arcpy.AddCodedValueToDomain_management(workspace, i.name, d, values_LADO[d])
        elif i.name == "COD_VIA":
            for d in values_COD_VIA:
                arcpy.AddCodedValueToDomain_management(workspace, i.name, d, values_COD_VIA[d])
        elif i.name == "TIPO_LOTE":
            for d in values_TIPO_LOTE:
                arcpy.AddCodedValueToDomain_management(workspace, i.name, d, values_TIPO_LOTE[d])
        elif i.name == "COLINDANCIA":
            for d in values_COLINDANCIA:
                arcpy.AddCodedValueToDomain_management(workspace, i.name, d, values_COLINDANCIA[d])
        elif i.name == "ABRE_TIPVIA":
            for d in values_ABRE_TIPVIA:
                arcpy.AddCodedValueToDomain_management(workspace, i.name, d, values_ABRE_TIPVIA[d])
        elif i.name == "DIS_PAR":
            for d in values_DIS_PAR:
                arcpy.AddCodedValueToDomain_management(workspace, i.name, d, values_DIS_PAR[d])
        elif i.name == "CONDICION":
            for d in values_CONDICION:
                arcpy.AddCodedValueToDomain_management(workspace, i.name, d, values_CONDICION[d])
        elif i.name == "ESTADO":
            for d in values_ESTADO:
                arcpy.AddCodedValueToDomain_management(workspace, i.name, d, values_ESTADO[d])
        elif i.name == "ESTADO_UBI":
            for d in values_ESTADO_UBI:
                arcpy.AddCodedValueToDomain_management(workspace, i.name, d, values_ESTADO_UBI[d])
        elif i.name == "TIPO_DOC":
            for d in values_TIPO_DOC:
                arcpy.AddCodedValueToDomain_management(workspace, i.name, d, values_TIPO_DOC[d])
        elif i.name == "TIPO_PREDIO":
            for d in values_TIPO_PREDIO:
                arcpy.AddCodedValueToDomain_management(workspace, i.name, d, values_TIPO_PREDIO[d])


domain()
# Asignacion de todos dominios a los campos necesarios

walk = arcpy.da.Walk(workspace)#, datatype="FeatureClass")
for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        path_fc = os.path.join(dirpath, filename)
        # Proceso: Assign Domain To Field
        advertencia = "inserting Domain in... {}".format(filename)
        if "CF_UNIDADES_URBANAS" in filename or "CF_LOTES" in filename or "CF_PREDIO" in filename or "CF_MANZANA_URB" in filename or "CF_NUMERACION" in filename or "TB_PUNTO" in filename or "TB_PREDIO" in filename:
            print advertencia + ", field -> TIPO_UU"
            arcpy.AssignDomainToField_management(path_fc, "TIPO_UU", "TIPO_UU", "")
        if "CF_UNIDADES_URBANAS" in filename:
            print advertencia + ", field -> ABR_TUU"
            arcpy.AssignDomainToField_management(path_fc, "ABR_TUU", "ABRE_UU", "")
        if "ARANCEL" in filename or "CF_PREDIO" in filename or "CF_LOTES" in filename or "CF_NUMERACION" in filename:
            print advertencia + ", field -> LADO"
            arcpy.AssignDomainToField_management(path_fc, "LADO", "LADO", "")
        if "ARANCEL" in filename or "CF_SEG_VIAL" in filename or "CF_PREDIO" in filename or "CF_LOTES" in filename or "CF_NUMERACION" in filename or "TB_PREDIO" in filename or "TB_PUNTO" in filename:
            print advertencia + ", field -> TIP_VIA"
            arcpy.AssignDomainToField_management(path_fc, "TIP_VIA", "COD_VIA", "")
        if "CF_EJE_VIAL" in filename or "CF_SEG_VIAL" in filename:
            print advertencia + ", field -> ABR_TVIA"
            arcpy.AssignDomainToField_management(path_fc, "ABR_TVIA", "ABRE_TIPVIA", "")
        if "CF_ARANCEL" in filename:
            print advertencia + ", field -> COLING"
            arcpy.AssignDomainToField_management(path_fc, "COLING", "COLINDANCIA", "")
        if "CF_LOTES" in filename:
            print advertencia + ", field -> TIP_LOT"
            arcpy.AssignDomainToField_management(path_fc, "TIP_LOT", "TIPO_LOTE", "")
        if "CF_ARANCEL" in filename or "TB_PREDIO" in filename or "TB_PUNTO" in filename:
            print advertencia + ", field -> DIS_PAR"
            arcpy.AssignDomainToField_management(path_fc, "DIS_PAR", "DIS_PAR", "")
        if "ARANCEL" in filename or "CF_EJE_VIAL" in filename or "CF_UNIDADES_URBANAS" in filename:
            print advertencia + ", field -> CONDIC"
            arcpy.AssignDomainToField_management(path_fc, "CONDIC", "CONDICION", "")
        if "TB_PREDIO" in filename:
            print advertencia + ", field -> ESTADO_P"
            arcpy.AssignDomainToField_management(path_fc, "ESTADO_P", "ESTADO", "")
        if "TB_PREDIO" in filename or "TB_PUNTO" in filename:
            print advertencia + ", field -> ESTADO_UBI"
            arcpy.AssignDomainToField_management(path_fc, "ESTADO", "ESTADO_UBI", "")
        if "TB_PREDIO" in filename or "TB_PUNTO" in filename:
            print advertencia + ", field -> TIP_DOC"
            arcpy.AssignDomainToField_management(path_fc, "TIP_DOC", "TIPO_DOC", "")
        if "TB_PREDIO" in filename or "TB_PUNTO" in filename:
            print advertencia + ", field -> TIPO_PREDIO"
            arcpy.AssignDomainToField_management(path_fc, "Tipo_predio", "TIPO_PREDIO", "")
        #     arcpy.AssignDomainToField_management(path_fc, "TIPO_INGRESO", "TIPO_INGRESO", "")
