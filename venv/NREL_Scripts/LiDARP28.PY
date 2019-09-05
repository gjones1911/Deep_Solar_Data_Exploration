##
## Basic requirements
## Must contain folder in accordance with the naming conventions used in the "City_1" field of the "Altitude.shp".
## This folder must have two sub folders i.e. (1) "reflective_surface" having the grid "refsurf", (2) Buildings having "City_1_2d_buildings.shp" (keep only one file in this folder) file.
## Base_map folder having files "Zip.shp" and "ShadeThreshold.shp" files.
## LDR.gdb Database having feature layers "Altitude.shp", & "Azimuth.shp"
##



import arcpy
import os.path
from arcpy import env
from arcpy import da
from arcpy.sa import *
import time
# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")
zFactor = 1
outMeasurement = "DEGREE"
dPath = "C:/LiDAR/"
arcpy.env.workspace  = (str(dPath))
try:

        StartTime = time.clock()
        #StartTime11 = time.clock()
        inTable  = r"C:/LiDAR/Base_map/LDR.gdb/Altitude"
        inTablez = r"C:/LiDAR/Base_map/LDR.gdb/Azimuth"

#
#==============================================.Query for City Needed to be analyzed.================================================>
#
        exprInTab =  "!Analyzed!+!Process!"
        arcpy.CalculateField_management(inTable, "AP", exprInTab, "PYTHON_9.3", "")
        V1 = 'NY'
        qryInTab  =  '"AP"'+" ='"+str(V1)+"'"       
        #print qryInTab
        InTab1 = arcpy.MakeFeatureLayer_management(inTable,"InTab")
        inTableA = arcpy.SelectLayerByAttribute_management(InTab1,"NEW_SELECTION",qryInTab)
        cnt = arcpy.GetCount_management(inTableA)
        #print "number of Cities selected:"+str(cnt)
        
#
#==============================================.Query for City Name.================================================>
#
        CityName = "City_1"
        CityF = set()
        #cities = arcpy.SearchCursor(inTable)
        cities = arcpy.SearchCursor(inTableA)
        for cityn in cities:
            CityF.add(cityn.getValue(CityName))
            #print "List of cities needs to be analyzed:" + str(CityF)
            for Val1 in CityF:
                cityq = Val1
                #print "city name is :"+str(cityq)
                qry1 =  '"City_1"'+" ='"+str(cityq)+"'"
                #print "The City being analyzed:" +str(qry1)

        arcpy.env.workspace  = (str(dPath)+str(cityq))
        # Set Snap Raster environment
        arcpy.env.snapRaster = (str(dPath)+str(cityq))+"/reflective_surface/refsurf"
        inRaster = (str(dPath)+str(cityq))+"/reflective_surface/refsurf"  #LiDAR Raster

##
        arcpy.env.workspace  = (str(dPath)+str(cityq)+"/Buildings/")
        fcs = arcpy.ListFeatureClasses()
        for fc in fcs:
            fc2 = fc
        inMaskData = fc2               #Building layer

#
#================================================.Selecting the data based on City Query.===============================>
#
        lyr1 = arcpy.MakeFeatureLayer_management(inTable,"lyr")
        inTable2 = arcpy.SelectLayerByAttribute_management(lyr1,"NEW_SELECTION",qry1)
        lyrz2 = arcpy.MakeFeatureLayer_management(inTablez,"lyrz")
        inTablez2 = arcpy.SelectLayerByAttribute_management(lyrz2,"NEW_SELECTION",qry1)
        cnt = arcpy.GetCount_management(inTablez2)
        #print "number of selected record is:"+str(cnt)



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#.......................... Join raster and shapefiles tables................................................................Line 102
#   
#         # Set local variables for combs join
        print
        print "*********************:  Join raster and shapefiles tables  :********************"
        print
        StartTime3 = time.clock()
        inRasterC5 = (str(dPath)+str(cityq)+"/Combine/"+str("combs"))        
        env.qualifiedFieldNames = False
        inFeatureJ1 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_poly")                    #Input, combs_poly
        layerNameJ1 = "Combs_poly"
        joinFieldJ1 = "GRID_CODE"
        #inRasterC5 # combs
        joinFieldJ2 = "VALUE"
        outFeatureJ1 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_poly2")                   #Output, combs_poly2
        arcpy.MakeFeatureLayer_management (inFeatureJ1,  layerNameJ1)        
        # Join the feature layer to a table
        arcpy.AddJoin_management(layerNameJ1, joinFieldJ1, inRasterC5, joinFieldJ2, "KEEP_ALL")  #created new layer combs_poly2 with join fields              
        # Copy the layer to a new permanent feature class
        arcpy.CopyFeatures_management(layerNameJ1, outFeatureJ1)
        fieldLength = 3        
        arcpy.AddField_management(outFeatureJ1,"SLPF", "LONG","", "",fieldLength)
        Field33B =  "vat_SLPFINAL"
        arcpy.CalculateField_management(outFeatureJ1,"SLPF","!"+str(Field33B)+"!","PYTHON_9.3","")
        dField = ["Id","grid_code","vat_Rowid","vat_VALUE","vat_COUNT","vat_ASPFINAL","vat_HILLFINAL","vat_SLPFINAL"]
        fList = arcpy.ListFields(outFeatureJ1)
        nameList = []        
        for f in fList:
                nameList.append(f.name)
        for f in nameList:
                for f2 in dField:
                        if f == f2:
                           arcpy.DeleteField_management(outFeatureJ1,f2)
        EndTime3 = time.clock()
        #print "Processed step 28 A, Join of  raster & polygon tables (combs_poly2) done for the city:" +str(cityq)
        print "Processed step 28 A, Join of  raster & polygon tables (combs_poly2)"
        print
        print "Time taken to process step 28 A  %s Minutes:" % ((EndTime3 - StartTime3)/60)
        print
        #time.sleep(5)
#.......................................................................................................................
         # Set local variables for combew join
        StartTime4 = time.clock()
        inRasterC6 = (str(dPath)+str(cityq)+"/Combine/"+str("combew"))
        env.qualifiedFieldNames = False
        inFeatureJ3 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_poly")                        #Input, combew_poly
        layerNameJ2 = "Combs_poly2"
        joinFieldJ2 = "GRID_CODE"
        #inRasterC6 # combew (_cob)
        joinFieldJ3 = "VALUE"
        outFeatureJ3 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_poly2")                      #Output, combew_poly2
        arcpy.MakeFeatureLayer_management (inFeatureJ3,  layerNameJ2)        
        # Join the feature layer to a table
        arcpy.AddJoin_management(layerNameJ2, joinFieldJ2, inRasterC6, joinFieldJ3, "KEEP_ALL")  #created new layer combew_poly2 with join fields              
        # Copy the layer to a new permanent feature class
        arcpy.CopyFeatures_management(layerNameJ2, outFeatureJ3)        
        inFeatureJ33 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_poly2")   #Input, combew_poly2
        #inFeatureJ33 = "Z:/Temp/Denver/Denver1/combine.gdb/combew_poly2" 
        fieldLength = 3               
        arcpy.AddField_management(inFeatureJ33,"SLPF", "LONG","", "",fieldLength) # (for tuple * and , )
        Field34B =  "vat_SLPFINAL"
        arcpy.CalculateField_management(inFeatureJ33,"SLPF","!"+str(Field34B)+"!","PYTHON_9.3","")
        dField = ["Id","grid_code","vat_Rowid","vat_VALUE","vat_COUNT","vat_ASPFINAL","vat_HILLFINAL","vat_SLPFINAL"]
        fList = arcpy.ListFields(inFeatureJ33)
        nameList = []        
        for f in fList:
                nameList.append(f.name)
        for f in nameList:
                for f2 in dField:
                        if f == f2:
                           arcpy.DeleteField_management(inFeatureJ33,f2)
        EndTime4 = time.clock()
        #print "Processed step 28 B, Join of  raster & polygon tables (combew_poly2) done for the city:" +str(cityq)
        print "Processed step 28 B, Join of  raster & polygon tables (combew_poly2)"
        print
        print "Time taken to process step 28 B %s Minutes:" % ((EndTime4 - StartTime4)/60)  
        #time.sleep(5)

        EndTime = time.clock()
        time = ((EndTime - StartTime)/60)
        #print "Time taken by the whole process is Minutes: " +str(time)
        print "Now runniing LiDarP29A script to process step 29 A"
        print

except Exception as e:
    print e.message
    arcpy.AddError(e.message)
