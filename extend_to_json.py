# -*- coding: utf-8 -*-
import arcpy, os, sys, json,datetime
inicio = datetime.datetime.now()
#print inicio
reload(sys)
root_mxd = r'C:\Users\jcruz\Desktop\pruebas_json\22_45207.mxd'
mxd=arcpy.mapping.MapDocument(root_mxd)
df = arcpy.mapping.ListDataFrames(mxd, "L*")[0]
Layer1=arcpy.mapping.ListLayers(mxd,"MANZANAS_PERU",df)[0]
x1=str(df.extent).split(" ")[0]
y1=str(df.extent).split(" ")[1]
x2=str(df.extent).split(" ")[2]
y2=str(df.extent).split(" ")[3]
#print str(df.extent).split(" ")

dict_fc={
  "displayFieldName": "",
  "fieldAliases": {
    "OBJECTID": "OBJECTID",
    "NAME": "NAME"
  },
  "geometryType": "esriGeometryPolygon",
  "spatialReference": {
    "wkid": 4326,
    "latestWkid": 4326
  },
  "fields": [{
      "name": "OBJECTID",
      "type": "esriFieldTypeOID",
      "alias": "OBJECTID"    },
     {
      "name": "NAME",
      "type": "esriFieldTypeString",
      "alias": "NAME",
      "length": 50}],
  "features": [
    {
      "attributes": {
        "OBJECTID": 1,
        "NAME": "NOMBRE"
      },
      "geometry": {
        "rings": [
          [ [
              float('{}'.format(x1)),
              float('{}'.format(y2))
            ],[
              float('{}'.format(x2)),
              float('{}'.format(y2))
            ],[
              float('{}'.format(x2)),
              float('{}'.format(y1))
            ],[
              float('{}'.format(x1)),
              float('{}'.format(y1))
            ],[
              float('{}'.format(x1)),
              float('{}'.format(y2))
            ]          ]        ]      }    }  ]}
json_fc = json.dumps(dict_fc)
f = open("dict_fc.json","w")
f.write(json_fc)
f.close()
hr=(datetime.datetime.now().strftime('%H:%M:%S')).replace(":","_")
new_fc=r'C:\Users\jcruz\Documents\ArcGIS\Default.gdb\json_to_fc_{}'.format(hr)
arcpy.JSONToFeatures_conversion("dict_fc.json",new_fc)

layer_df=arcpy.MakeFeatureLayer_management(new_fc,"layer_Extend")
sent1=arcpy.SelectLayerByLocation_management(Layer1,"INTERSECT",layer_df)
#getcount=arcpy.management.GetCount(Layer1)
X=[]
Y=[]
with arcpy.da.SearchCursor(Layer1,["SHAPE@XY"]) as cursor:
    for i in cursor:
        X.append(i[0][0])
        Y.append(i[0][1])
averageX=sum(X)/len(X)
averageY=sum(Y)/len(Y)
df_x=[]
df_y=[]
with arcpy.da.SearchCursor(layer_df,["SHAPE@XY"]) as cursor_df:
    for i in cursor_df:
        df_x.append(i[0][0])
        df_y.append(i[0][1])

dif_x=df_x[0]-averageX
dif_y=df_y[0]-averageY

#print dif_x,dif_y

with arcpy.da.UpdateCursor(layer_df,["SHAPE@XY"]) as cursor_df2:
    for i in cursor_df2:
        i[0]=(df_x[0]-(dif_x*1.5),df_y[0]-(dif_y))
        cursor_df2.updateRow(i)
#print df_x[0]-dif_x,df_y[0]-dif_y
guardar= df.scale
extend_F=arcpy.management.MakeFeatureLayer(new_fc,"okidoki").getOutput(0).getExtent()
df.extent=extend_F
df.scale = guardar
arcpy.SelectLayerByAttribute_management(Layer1,"CLEAR_SELECTION")
arcpy.RefreshActiveView()
mxd.saveACopy(r'C:\Users\jcruz\Desktop\pruebas_json\22_45207_move.mxd')
fin = datetime.datetime.now()

print fin-inicio