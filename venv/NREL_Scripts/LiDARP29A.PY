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

#..........................................................................
        # Set local variables
        print
        print "********:  Dissolve polygon by Slope Final Field of combs_poly2  :********"
        print
        StartTime5 = time.clock()
        inFeatureD2      = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_poly2")                          # Input,  combs_poly2
        outFeatureClass2 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_slppoly")        
        dissolveFields = ["SLPF"]     
        # Execute Dissolve using LANDUSE and TAXCODE as Dissolve Fields
        arcpy.Dissolve_management(inFeatureD2, outFeatureClass2, "SLPF", "" , "SINGLE_PART", "DISSOLVE_LINES")                 #Output, cs_slppoly         
        EndTime5 = time.clock()
        #print "Processed step 29 A, Dissolve (combs_poly2)  fields for the city:" +str(cityq)
        print "Processed step 29 A, Dissolve by field SLPF"
        print
        print "Time taken by step 29 A %s Minutes:" % ((EndTime5 - StartTime5)/60)
        print "Now running LiDarP29B script to process step 29 B"
        print
        #time.sleep(5)


except Exception as e:
    print e.message
    arcpy.AddError(e.message)
