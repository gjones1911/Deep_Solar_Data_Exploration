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
zPath = "Z:/Temp/"
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
 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#============================================================.SLOPE CALCULATION.===============================================> 
        print
        print "*********************:   Slope Calculation :*********************"
        print
        arcpy.env.snapRaster = (str(dPath)+str(cityq))+"/reflective_surface/refsurf"   
        inRaster = (str(dPath)+str(cityq))+"/reflective_surface/refsurf"  #LiDAR Raster
        outMeasurement = "DEGREE"                                                                  # Line 28
        zFactor = 1
        # Execute Slope           
        outSlope = Slope(inRaster, outMeasurement, zFactor)
        # Save the output 
        outSlope.save(str(dPath)+str(cityq)+"/Slope/"+str("slpraw"))                               #output,  slpraw (floating point)
        del outSlope
        print "Processed step 5,  Slope calculated for the city:" +str(cityq)
#
#..........................Extract by Mask..........................................................Line 33
#
        arcpy.env.workspace  = (str(dPath)+str(cityq)+"/Buildings/")
        fcs = arcpy.ListFeatureClasses()
        for fc in fcs:
            fc2 = fc
        inMaskData = fc2                                                                    #input, Building layer, shape file
        inRasterS2 =  (str(dPath)+str(cityq)+"/Slope/"+str("slpraw"))                       #input  slpraw (floating point)
        outExtractByMask = ExtractByMask(inRasterS2, inMaskData)
        # Save the output 
        outExtractByMask.save(str(dPath)+str(cityq)+"/Slope/"+str("slpbldg"))               #output, slpbldg  (floating point)
        del outExtractByMask
        #print "Processed step 6, Slope extracted with Mask for the city:" +str(cityq)
        print "Processed step 6,  Slope extracted" 
#
#..........................Extract with Attribute....................................................Line 37 
#
        inRasterS3 = (str(dPath)+str(cityq)+"/Slope/"+str("slpbldg"))                       #input slpbldg (floating point)
        inSQLClauseS = "VALUE < 60"
        #print "Raster is:"+str(inRasterS3)
        # Execute ExtractByAttributes
        attExtractS = ExtractByAttributes(inRasterS3, inSQLClauseS) 
        # Save the output 
        attExtractS.save(str(dPath)+str(cityq)+"/Slope/"+str("slplt60"))                    # output, slplt60 (floating point)
        del attExtractS
        #print "Processed step 7, Slope extracted by attribute for the city:" +str(cityq)
        print "Processed step 7,  Slope extracted"
#
#..........................HillShade Final............................................................Line 40
#        
        inRasterS4 = (str(dPath)+str(cityq)+"/Slope/"+str("slplt60"))                        # input. slplt60  (floating point)
        inRasterH4 = (str(dPath)+str(cityq)+"/Combine/sumRec_year/"+str("annual"))           # input. annual (Integer)
        #print " Slope Raster is:"+str(inRasterS4)
        #print " Annual Hillshade Raster is:"+str(inRasterH4)
        Sval1 = Float(inRasterS4)                                 
        Hval1 = Int(inRasterH4)                                   
        outConS = Con(Sval1<= 9.5,Hval1 * 1.5, Hval1)
        outConS.save(str(dPath)+(cityq)+"/Slope/"+str("hillfinal"))                          #output, hillfinal, (floating point)
        del outConS
        #print "Processed step 8, Slope.. Hillshade final calculated for the city:" +str(cityq)
        print "Processed step 8,  Slope (Hillshade final calculated)"

#
#..........................Slope  focal mean............................................................Line 80
#            
        neighborhood = NbrRectangle(3, 3, "CELL")
        outFocalStatistics = FocalStatistics(inRasterS4, neighborhood, "MEAN","")                     #Input. slplt60 (floating point)
        outFocalStatistics.save(str(dPath)+str(cityq)+"/Slope/"+str("slpfmean"))                      #Output, slpfmean (floating point)
        del outFocalStatistics
        #print "Processed step 9, Slope  focal mean for the city:" +str(cityq)
        print "Processed step 9,  Slope  (focal mean)"
#
#..........................Slope  focal mean 2............................................................Line 83
#
        inRasterS5 = (str(dPath)+str(cityq)+"/Slope/"+str("slpfmean"))                              #input: slpfmean  (floating point)
        neighborhood = NbrRectangle(3, 3, "CELL")
        outFocalStatistics = FocalStatistics(inRasterS5, neighborhood, "MEAN","")                   
        outFocalStatistics.save(str(dPath)+str(cityq)+"/Slope/"+str("slpfmean2"))                   #output, slpfmean2 (floating point)
        del outFocalStatistics
        #print "Processed step 10, Slope focal mean for the city:" +str(cityq)
        print "Processed step 10, Slope (focal mean)"
#
#=================================================.ASPECT CALACULATION.=================================================================> 
#
        print
        print "*********************:   Aspect Calculation :*********************"
        print
        # Execute Aspect                                                        # Line 31
        inRaster = (str(dPath)+str(cityq))+"/reflective_surface/refsurf"  #LiDAR Raster
        outAspect = Aspect(inRaster)                                                                  #Input, refsurf (Integer)
        # Save the output 
        outAspect.save(str(dPath)+str(cityq)+"/Aspect/"+str("aspraw"))                                #Output, aspraw (floating point)
        del outAspect
        #print "Processed step 11, Aspect calculated for the city:" +str(cityq)
        print "Processed step 11, Aspect calculated"
#
#..........................Extract by Mask............................................................Line 35
#       
        inRasterA2 = (str(dPath)+str(cityq)+"/Aspect/"+str("aspraw"))                                #Input, aspraw (floating point) & buildings  (shapefile)        
        #print "In mask is:"+str(inMaskData)
        #print "Raster is:"+str(inRasterA2)
        outExtractByMaskA = ExtractByMask(inRasterA2, inMaskData)
        # Save the output 
        outExtractByMaskA.save(str(dPath)+str(cityq)+"/Aspect/"+str("aspbldg"))                     #Output, aspbldg (floating point)
        del outExtractByMaskA
        #print "Processed step 12, Aspect extracted with Mask for the city:" +str(cityq)
        print "Processed step 12, Aspect extracted with Mask"
#
#..........................Flat Roof...................................................................Line 43
#
        inRasterS4 = (str(dPath)+str(cityq)+"/Slope/"+str("slplt60"))
        Sval1 = Float(inRasterS4)
        inRasterA3 = (str(dPath)+str(cityq)+"/Aspect/"+str("aspbldg"))                                #Input, aspbldg & slplt60 (floating points)
        Aval1 = Float(inRasterA3)                                                
        outConA = Con(Sval1<= 9.5,-1, Aval1)                                               
        outConA.save(str(dPath)+(cityq)+"/Aspect/"+str("aspflat"))                                    #Output, aspflat (floating point)
        del outConA
        #print "Processed step 13, Flat roof  calculated for the city:" +str(cityq)
        print "Processed step 13, Flat roof  calculated"
#
#..........................Flat Roof Reclassification..................................................Line 46
#
        inRasterA4 = (str(dPath)+str(cityq)+"/Aspect/"+str("aspflat"))                                 #Input, aspflat (floating point)
        reclassField = "VALUE"
        remapA1 = RemapValue([[-1,0,0],[0,22.5,1],[22.5,67.5,2] ,[67.5,112.5,3],[112.5,157.5,4],[157.5,202.5,5],[202.5,247.5,6],[247.5,292.5,7],[292.5,337.5,8],[337.5,360,1]])      #                
        outReclassifyA = Reclassify(inRasterA4, reclassField, remapA1, "NODATA")
        outReclassifyA.save(str(dPath)+str(cityq)+"/Aspect/"+str("aspflatrc"))                          #Output, aspflatrc (Integer)
        del outReclassifyA
        #print "Processed step 14, Flat roof recalssification calculated for the city:" +str(cityq)
        print "Processed step 14, Flat roof recalssification calculated"
#
#..........................Focal Statistics.............................................................Line 59
#
        inRasterA5 = (str(dPath)+str(cityq)+"/Aspect/"+str("aspflatrc"))                                #Input, aspflatrc (Integer)
        neighborhood = NbrRectangle(3, 3, "CELL")
        # Execute FocalStatistics
        outFocalStatistics = FocalStatistics(inRasterA5, neighborhood, "VARIETY","")
        # Save the output
        outFocalStatistics.save(str(dPath)+str(cityq)+"/Aspect/"+str("aspvar"))                          #Output, aspvar (Integer)
        del outFocalStatistics
        #print "Processed step 15, Focal Statistics calculated for the city:" +str(cityq)
        print "Processed step 15, Focal Statistics calculated"
#
#..........................Extract with Attribute.......................................................Line 62 
#
        inRasterA6 = (str(dPath)+str(cityq)+"/Aspect/"+str("aspvar"))                                     #Input, aspvar (Integer)
        inSQLClauseA = "VALUE < 4"
        attExtractA = ExtractByAttributes(inRasterA6, inSQLClauseA) 
        # Save the output 
        attExtractA.save(str(dPath)+str(cityq)+"/Aspect/"+str("aspvarext"))                               #Output, aspvarext (Integer)
        del attExtractA
        #print "Processed step 16, Aspect extracted by attribute for the city:" +str(cityq)
        print "Processed step 16, Aspect extracted by attribute"
#
#..........................Extract by Mask 2............................................................Line 65
#       
        inMaskDataA7 = (str(dPath)+str(cityq)+"/Aspect/"+str("aspvarext"))                               #Input, aspvarext (Integer) & aspflatrc (Integer)  (line 46)
        outExtractByMaskAA = ExtractByMask(inRasterA5, inMaskDataA7)
        # Save the output 
        outExtractByMaskAA.save(str(dPath)+str(cityq)+"/Aspect/"+str("aspflatmk"))                       #Output, aspflatmk (Integer)
        #arcpy.Delete_management(outExtractByMaskAA, "")
        #print "Processed step 17, Aspect for Flat Roof extracted with Mask for the city:" +str(cityq)
        print "Processed step 17, Aspect for Flat Roof extracted with Mask"
          
#
#..........................Focal Statistics  2.............................................................Line 68
#
        inRasterA8 = (str(dPath)+str(cityq)+"/Aspect/"+str("aspflatmk"))                                  #Input, aspflatmk (Integer)
        neighborhood = NbrRectangle(3, 3, "CELL")
        # Execute FocalStatistics
        outFocalStatisticsAA = FocalStatistics(inRasterA8, neighborhood, "MAJORITY","")
        # Save the output 
        outFocalStatisticsAA.save(str(dPath)+str(cityq)+"/Aspect/"+str("aspmaj"))                         #Output, aspmaj (Integer)
        del outFocalStatisticsAA
        #print "Processed step 18, Focal Statistics Majority calculated for the city:" +str(cityq)
        print "Processed step 18, Focal Statistics Majority calculated"

#
#..........................Extract by Mask 3............................................................Line 70
#       
        inRasterA9 = (str(dPath)+str(cityq)+"/Aspect/"+str("aspmaj"))                                     #Input, aspmaj (Integer) & buildings (shapefile)
        outExtractByMaskAAA = ExtractByMask(inRasterA9, inMaskData)
        # Save the output 
        outExtractByMaskAAA.save(str(dPath)+str(cityq)+"/Aspect/"+str("aspfinal"))                        #Output, aspfinal (Integer)
        del outExtractByMaskAAA
        #print "Processed step 19, Aspect for Flat Roof extracted with Mask 3 for the city:" +str(cityq)
        print "Processed step 19, Aspect for Flat Roof extracted with Mask"

#
#..........................Aspect Raster to Polygon...................................................................Line 72
#       
        inRasterA10 = (str(dPath)+str(cityq)+"/Aspect/"+str("aspfinal"))                                  #Input, aspfinal (Integer)
        FieldA = "VALUE"
        outPolygons = (str(dPath)+str(cityq)+"/Aspect/"+str("aspfinal_poly"))                            #Output, aspfinal_poly  (shapefile)
        arcpy.RasterToPolygon_conversion(inRasterA10, outPolygons, "NO_SIMPLIFY", FieldA)
        #print "Processed step 20, Aspect, raster to polygon for the city:" +str(cityq)
        print "Processed step 20, Aspect, raster to polygon"

#
#..........................Aspect Feature to Raster...................................................................Line 75
#
        inFeature = (str(dPath)+str(cityq)+"/Aspect/"+str("aspfinal_poly.shp"))                  #Input, aspfinal_poly (shapefile)
        FieldAA = "ID"
        outRaster = (str(dPath)+str(cityq)+"/Aspect/"+str("aspid"))                                          
        cellSize = 1
        # Execute PolygonToRaster
        arcpy.FeatureToRaster_conversion(inFeature, FieldAA, outRaster, cellSize)                        #Output, aspid   (Integer)    
        #print "Processed step 21, Aspect, feature to raster for the city:" +str(cityq)
        print "Processed step 21, Aspect, feature to raster"

#
#..........................Combine Aspect ............................................................................Line 78
#
        inRasterA11 = (str(dPath)+str(cityq)+"/Aspect/"+str("aspid"))                                    #Input, aspid (Integer) & aspfinal (Integer)
        # Execute PolygonToRaster
        outCombine = Combine([inRasterA11,inRasterA10])
        # Save the output 
        outCombine.save(str(dPath)+str(cityq)+"/Aspect/"+str("aspcomb"))                                 #Output, aspcomb  (Integer)
        del outCombine
        #print "Processed step 22, Combine Aspect for the city:" +str(cityq)
        print "Processed step 22, Combine Aspect"



#
#=================================================. SLOPE  Zonal mean.=================================================================> 
#  
#
#..........................Slope zonal mean ..................................................................Line 86
#
        print
        print "*********************:   Slope Zonal Mean  :*********************"
        print
        inValueRasterS6 = (str(dPath)+str(cityq)+"/Slope/"+str("slpfmean2"))                                    #Input,   slpfmean2
        inZoneRasterA12= (str(dPath)+str(cityq)+"/Aspect/"+str("aspcomb"))                                      #Input,   aspcomb  (line 78)
        zoneField = "VALUE"
        outZonalStatistics = ZonalStatistics(inZoneRasterA12, zoneField, inValueRasterS6,"MEAN", "NODATA") 
        outZonalStatistics.save(str(dPath)+str(cityq)+"/Combine/"+str("slpzmean"))                              #Output, slpzmean
        del outZonalStatistics
        #print "Processed step 23, Slope / Aspect Zonal mean for the city:" +str(cityq)
        print "Processed step 23, Slope Zonal mean"

#
#..........................Slope Aspect values assingment ..............................................................Line 89

        AvalA2 = Int(inRasterA10)                                                                               #Input,   aspfinal (Integer)
        inRasterS7 = (str(dPath)+str(cityq)+"/Combine/"+str("slpzmean"))                                        #Input,   slpzmean(Floating point)
        AvalS2 = Float(inRasterS7)
        outConAS = Con(AvalA2 == 0,0, AvalS2)
        outConAS.save(str(dPath)+(cityq)+"/Combine/"+str("slpfinal"))                                           #Output,  slpfinal (Floating point)
        del outConAS
        #print "Processed step 24, Slope / Aspect values assinged for the city:" +str(cityq)
        print "Processed step 24, Slope / Aspect values assinged"
        EndTime = time.clock()
        time = ((EndTime - StartTime)/60)
        print
        print "Time taken to process steps 5 - 24 is:" +str(time)+" Minutes" 
        print "Now Running LiDARP25 script to process steps 25 - 26"
        print
        

except Exception as e:
    print e.message
    arcpy.AddError(e.message)
