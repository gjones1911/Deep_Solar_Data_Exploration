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
        StartTime11 = time.clock()
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
        #print inRaster

##
        arcpy.env.workspace  = (str(dPath)+str(cityq)+"/Buildings/")
        fcs = arcpy.ListFeatureClasses()
        for fc in fcs:
            fc2 = fc
        inMaskData = fc2               #Building layer
        #print inMaskData

#
#================================================.Selecting the data based on City Query.===============================>
#
        lyr1 = arcpy.MakeFeatureLayer_management(inTable,"lyr")
        inTable2 = arcpy.SelectLayerByAttribute_management(lyr1,"NEW_SELECTION",qry1)
        lyrz2 = arcpy.MakeFeatureLayer_management(inTablez,"lyrz")
        inTablez2 = arcpy.SelectLayerByAttribute_management(lyrz2,"NEW_SELECTION",qry1)
        cnt = arcpy.GetCount_management(inTablez2)
        #print "number of selected record is:"+str(cnt)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#
#.......................... Combine ................................................................Line 98 & 99
#
        print
        print "*********************:  Combine  :*********************"
        print
        StartTime2 = time.clock()
        outFolderP1 = (str(dPath)+str(cityq)+"/Combine")
        outName1   =  "combine.gdb"              
        arcpy.CreateFileGDB_management(outFolderP1, outName1)
        inRasterC5 = (str(dPath)+str(cityq)+"/Combine/"+str("combs"))                                           #Input, combs (Integer)
        FieldC5 = "VALUE"       
        outPolygonsC5 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_poly")                               #Output, combs_poly (Feature Class)
        arcpy.RasterToPolygon_conversion(inRasterC5, outPolygonsC5, "NO_SIMPLIFY", FieldC5)
        arcpy.FeatureClassToShapefile_conversion(outPolygonsC5, outFolderP1)                                     #To use for UTM projection in step 38
        #print "Processed step 27 A, Combine raster to polygon for the city:" +str(cityq)
        print "Processed step 27 A, Combine raster to polygon"
#..........................................................................................................................................
        inRasterC6 = (str(dPath)+str(cityq)+"/Combine/"+str("combew"))                                          #Input, combew   (Integer)
        FieldC6 = "VALUE"
        outPolygonsC6 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_poly")                              #Output, combew_poly (shapefile)
        arcpy.RasterToPolygon_conversion(inRasterC6, outPolygonsC6, "NO_SIMPLIFY", FieldC6)
        EndTime2 = time.clock()
        #print "Processed step 27 B, Combine raster to polygon for the city:" +str(cityq)
        print "Processed step 27 B, Combine raster to polygon"
        print
        #print "Time taken by step 27 A & 27 B %s Minutes:" % ((EndTime2 - StartTime2)/60)
        time.sleep(5)

        EndTime = time.clock()
        time = ((EndTime - StartTime)/60)
        print "Time taken to process step 27 A & 27 B is:"+str(time)+" Minutes" 
        print "Please run LiDarP28 script to process steps 28 A & 28 B"
        print
except Exception as e:
    print e.message
    arcpy.AddError(e.message)
