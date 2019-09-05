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
zPath = "z:/Temp/"

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

#
#================================================.Selecting the data based on City Query.===============================>
#
        lyr1 = arcpy.MakeFeatureLayer_management(inTable,"lyr")
        inTable2 = arcpy.SelectLayerByAttribute_management(lyr1,"NEW_SELECTION",qry1)
        lyrz2 = arcpy.MakeFeatureLayer_management(inTablez,"lyrz")
        inTablez2 = arcpy.SelectLayerByAttribute_management(lyrz2,"NEW_SELECTION",qry1)
        cnt = arcpy.GetCount_management(inTablez2)
        #print "number of selected record is:"+str(cnt)

#=================================================. COMBINE.=================================================================> 
 
#
#..........................Combine Hillshade / Slope / Aspect .........................................................Line 92
#
        print
        print "********************:   Combine Hillshade / Slope / Aspect :********************"
        print
        inRasterA10 = (str(dPath)+str(cityq)+"/Aspect/"+str("aspfinal"))
        inRasterHfinal = (str(dPath)+(cityq)+"/Slope/"+str("hillfinal"))                                       #Input, hillfinal (Floating point)
        inRasterCon1 = (str(dPath)+(cityq)+"/Combine/"+str("slpfinal"))                                        #Input, slpfinal (Floating point)

        # Execute PolygonToRaster
        outCombine = Combine([inRasterA10,inRasterHfinal,inRasterCon1])                                  
        # Save the output 
        outCombine.save(str(dPath)+str(cityq)+"/Combine/"+str("comb"))                                         #Output, comb  (Integer)
        del outCombine
        #print "Processed step 25, Combine Hillshade / Slope / Aspectfor the city:" +str(cityq)
        print "Processed step 25, Combine Hillshade / Slope / Aspect"
        EndTime11 = time.clock()
        print
        print "Time taken to process step 25 %s Minutes:"  %((EndTime11 - StartTime11)/60)
#
#.......................... Combine Extract by Attribute................................................................Line 94 
#
#
        print
        print "*********************:  Shade Value  :*********************"
        print
        StartTime1 = time.clock()
        ShadeTab  = r"C:/LiDAR/Base_map/LDR.gdb/Shade"                                          # reading attribute values from Hillfinal field
        Shadeqry    =  '"City_1"'+" ='"+str(cityq)+"'"
        #print"The Shade value for the city:" +str(cityq)+ " is "+str(Shadeqry)
        Shadelyr1   = arcpy.MakeFeatureLayer_management(ShadeTab,"Shadelyr")
        ShadeTable2 = arcpy.SelectLayerByAttribute_management(Shadelyr1,"NEW_SELECTION",Shadeqry)
        #print "The name of city is :"+str(cityq)
        ShadeField = "Hillfinal"
        #sVal = []
        srows = arcpy.SearchCursor(ShadeTable2)
        for row in srows:
            sVal = row.getValue(ShadeField)
            #sVal.append(nVal)
            print"The Shade value for the city:" +str(cityq)+ " is "+str(sVal)
            inRasterC3 = (str(dPath)+str(cityq)+"/Combine/"+str("comb"))                                          # Input, comb (Integer)
            var1 = str("aspfinal")
            var2 = str("hillfinal")
            inSQLClauseC3 = ('("'+str(var1)+ '" = 0 OR ''"'+str(var1)+'" = 4 OR ''"'+str(var1)+'" = 5 OR ''"'+str(var1)+'" = 6) AND ''"'+str(var2)+'" > '+str(sVal))
            #print inSQLClauseC3
            attExtractC3 = ExtractByAttributes(inRasterC3, inSQLClauseC3) 
            # Save the output 
            attExtractC3.save(str(dPath)+str(cityq)+"/Combine/"+str("combs"))                                   #Output 1, combs (Integer)
            del attExtractC3
            #print "line 94, Combine 1 Extract with attribute for the city:" +str(cityq)
            inSQLClauseC4 = ('("'+str(var1)+ '" = 0 OR ''"'+str(var1)+'" = 3 OR ''"'+str(var1)+'" = 4 OR ''"'+str(var1)+'" = 5 OR ''"'+str(var1)+'" = 6 OR ''"'+str(var1)+'" = 7) AND ''"'+str(var2)+'" > '+str(sVal))
            #print inSQLClauseC4
            attExtractC4 = ExtractByAttributes(inRasterC3, inSQLClauseC4) 
            # Save the output 
            attExtractC4.save(str(dPath)+str(cityq)+"/Combine/"+str("combew"))                                   #Output 2,  combew (Integer)
            del attExtractC4
        EndTime1 = time.clock()
        #print "Processed step 26 A & 26 B, Combine, Extract by attribute for the city:" +str(cityq)
        print
        print "Processed step 26 A & 26 B, Combine, Extract by attribute"
        print "Time taken to process steps 26 A & 26 B %s Minutes:" % ((EndTime1 - StartTime1)/60)      
        EndTime = time.clock()
        time = ((EndTime - StartTime)/60)
        #print " Time taken by the whole process is Minutes: " +str(time)
        print "Now running LiDarP27 script to process steps 27 A & 27 B"
        print

except Exception as e:
    print e.message
    arcpy.AddError(e.message)
