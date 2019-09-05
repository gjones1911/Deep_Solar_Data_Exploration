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
#
#
#=========================================.Hillshade reclassification.==========================================================> 
#
        print
        print "*********************:  Hillshade reclassification   :*********************"
        print
        env.workspace = str(dPath)+str(cityq)+"/HillShade/"                                             
        datapath1 = str(dPath)+str(cityq)+"/HillShade/"
        #print datapath1
        inRasterList1 = arcpy.ListRasters('mar*','')
        reclassField = "VALUE"
        #print inRasterList1
        for inRaster1 in inRasterList1:
                #print "1:" +str(inRaster1)
                #print "Reclassifying raster: %s" %os.path.join("dataPath1",inRaster1)
                print inRaster1
                remap1 = RemapValue([[0,153,0],[153,254,1]])      # March
                #print "2:" +str(inRaster1)
                outReclassify = Reclassify(inRaster1, reclassField, remap1, "NODATA")
                #print "3:" +str(inRaster1)
                outReclassify.save(str(dPath)+str(cityq)+"/Reclass/"+str(inRaster1)+str("rec"))
                del outReclassify
                #print "4:" +str(inRaster1)
        datapath2 = str(dPath)+str(cityq)+"/HillShade/"
        inRasterList2 = arcpy.ListRasters('jun*','')
        #reclassField = "VALUE"
        for inRaster2 in inRasterList2:
                #print "Reclassifying raster: %s" %os.path.join("dataPath2",inRaster2)
                print inRaster2
                remap2 = RemapValue([[0,178.5,0],[178.5,254,1]])  # June
                outReclassify = Reclassify(inRaster2, reclassField, remap2, "NODATA")
                outReclassify.save(str(dPath)+str(cityq)+"/Reclass/"+str(inRaster2)+str("rec"))
                del outReclassify
        datapath3 = str(dPath)+str(cityq)+"/HillShade/"
        inRasterList3 = arcpy.ListRasters('sep*','')
        #reclassField = "VALUE"
        for inRaster3 in inRasterList3:
                #print "Reclassifying raster: %s" %os.path.join("dataPath3",inRaster3)
                print inRaster3
                remap3 = RemapValue([[0,153,0],[153,254,1]])      # September                        
                outReclassify = Reclassify(inRaster3, reclassField, remap3, "NODATA")
                outReclassify.save(str(dPath)+str(cityq)+"/Reclass/"+str(inRaster3)+str("rec"))
                del outReclassify
        datapath4 = str(dPath)+str(cityq)+"/HillShade/"
        inRasterList4 = arcpy.ListRasters('dec*','')
        #reclassField = "VALUE"
        for inRaster4 in inRasterList4:
                #print "Reclassifying raster: %s" %os.path.join("dataPath4",inRaster4)
                print inRaster4
                remap4 = RemapValue([[0,127.5,0],[127.5,254,1]])  # December                         
                outReclassify = Reclassify(inRaster4, reclassField, remap4, "NODATA")
                outReclassify.save(str(dPath)+str(cityq)+"/Reclass/"+str(inRaster4)+str("rec"))
                del outReclassify
        print
        print "Processed step 2, Hillshade recalssifcation completed" # for City:" +str(cityq)
#
#================================.Summation of reclassified Hillshade raster on month to month bases.===================================> 
#            
        print
        print "*********************:  Monthly Summation    :*********************"
        print
        arcpy.env.workspace = str(dPath)+str(cityq)+"/Reclass/"                                        #Line 21 
        datapath = str(dPath)+str(cityq)+"/Reclass/"
        rasters1 = arcpy.ListRasters('mar*','')
        i = 0
        # Sum of all the rasters for the Month of March
        for inRaster1 in rasters1:
            #print "processing raster for summation (monthly): %s" %os.path.join("dataPath",inRaster1)
            print inRaster1
            if  i == 0:
                outSum1 = arcpy.Raster(inRaster1)
                i += 1
            else:
                outSum1 = outSum1 + inRaster1
                i += 1
        outSum1.save(str(dPath)+str(cityq)+"/Combine/sumRec_month/"+str("Mar_sum"))
        del outSum1
        # Sum of all the rasters for the Month of June
        datapath = str(dPath)+str(cityq)+"/Reclass/"  
        rasters2 = arcpy.ListRasters('jun*','')
        #print rasters2
        i = 0
        for inRaster2 in rasters2:            
                #print "processing raster for summation (monthly): %s" %os.path.join("dataPath",inRaster2)
                print inRaster2
                if  i == 0:
                    outSum2 = arcpy.Raster(inRaster2)
                    i += 1
                else:
                    outSum2 = outSum2 + inRaster2
                    i += 1
        outSum2.save(str(dPath)+str(cityq)+"/Combine/sumRec_month/"+str("Jun_sum"))
        del outSum2
        # Sum of all the rasters for the Month of September
        datapath = str(dPath)+str(cityq)+"/Reclass/"  
        rasters3 = arcpy.ListRasters('sep*','')
        #print rasters3
        i = 0
        for inRaster3 in rasters3:
                #print "processing raster for summation (monthly): %s" %os.path.join("dataPath",inRaster3)
                print inRaster3
                if  i == 0:
                    outSum3 = arcpy.Raster(inRaster3)
                    i += 1
                else:
                    outSum3 = outSum3 + inRaster3
                    i += 1
        outSum3.save(str(dPath)+str(cityq)+"/Combine/sumRec_month/"+str("Sep_sum"))
        del outSum3        
        # Sum of all the rasters for the Month of December
        datapath = str(dPath)+str(cityq)+"/Reclass/"  
        rasters4 = arcpy.ListRasters('dec*','')
        #print rasters4
        i = 0
        for inRaster4 in rasters4:
            #print "processing raster for summation (monthly): %s" %os.path.join("dataPath",inRaster4)
            print inRaster4
            if  i == 0:
                outSum4 = arcpy.Raster(inRaster4)
                i += 1
            else:
                outSum4 = outSum4 + inRaster4
                i += 1
        outSum4.save(str(dPath)+str(cityq)+"/Combine/sumRec_month/"+str("Dec_sum"))
        del outSum4
        print
        print "Processed step 3, Summation of Hillshade for indivual months is completed" # for the city:" +str(cityq)   
#
#========================================.Reclassified HILLSHADE  raster on Annual bases.===============================>
#
        print
        print "*********************:  Annual Summation    :*********************"
        print
        arcpy.env.workspace = str(dPath)+str(cityq)+"/Combine/sumRec_month/"                     # Line 25
        datapath = str(dPath)+str(cityq)+"/Combine/sumRec_month/"  
        rasters = arcpy.ListRasters('','')
        #print rasters
        i = 0
        for inRaster in rasters:
            #print "processing raster for summation(annual) : %s" %os.path.join("dataPath",inRaster)
            print inRaster
            if  i == 0:
                outSum = arcpy.Raster(inRaster)
                i += 1
            else:
                outSum = outSum + inRaster
                i += 1
        outSum.save(str(dPath)+str(cityq)+"/Combine/sumRec_year/"+str("annual"))                  #  output,  annual   (Integer)
        del outSum
        print "Processed step 4, Summation of Hillshade for whole year is completed" # for the city:" +str(cityq)
#
#...................................................................... Dissolve field .............................................................Step 29
        print
        EndTime = time.clock()
        time = ((EndTime - StartTime)/60)
        print "Time taken to process steps 2-4 is:" +str(time)+" Minutes" 
        print "Now Running LiDARP5 script to process steps 5 - 24"
        print

except Exception as e:
    print e.message
    arcpy.AddError(e.message)
