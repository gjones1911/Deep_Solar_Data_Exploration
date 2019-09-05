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
        inTable  = r"C:/LiDAR/Base_map/LDR.gdb/Altitude"
        inTablez = r"C:/LiDAR/Base_map/LDR.gdb/Azimuth"
#
#
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
#
#==============================================.Query for City Name.================================================>
#

        
        print( "                            LIDAR PV DATA ANALYST                          ")
        print( "========================================================================")
        print()
        
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
                print "*********************: The City Quad being analyzed  :*********************"               
                print
                print cityq
                print 

        arcpy.env.workspace  = (str(dPath)+str(cityq))
        # Set Snap Raster environment
        arcpy.env.snapRaster = (str(dPath)+str(cityq))+"/reflective_surface/refsurf"
        inRaster = (str(dPath)+str(cityq))+"/reflective_surface/refsurf"  #LiDAR Raster

#Check if the Raster layer is in projected space
        desc = arcpy.Describe(inRaster)
        #print inRaster
        # Get the spatial reference 
        sr = desc.spatialReference
        # Check if the Rastger is in projected space
        if sr.type == "Projected":
            print    
            print "*********************:         PROJECTION            :*********************"
            print
            #print "Raster layer "+str(inRaster)+ " has Projection: " +str(sr.Name)
            print "Raster layer: " +str(sr.Name)
            
        else:
            print "ERROR.....The Projection of Raster layer is: " +str(sr.Name)
            print "Please assign projection to: " +str(inRaster)
            print "LiDAR Analyst is going to exit now."
            sys.exit()
## Buildings layer
##
        arcpy.env.workspace  = (str(dPath)+str(cityq)+"/Buildings/")
        fcs = arcpy.ListFeatureClasses()
        for fc in fcs:
            fc2 = fc
        inMaskData = fc2               #Building layer

#Check if the buidlings layer is in projected space
        desc = arcpy.Describe(inMaskData)
        # Get the spatial reference 
        sr = desc.spatialReference
        # Check if the feature class is in projected space
        if sr.type == "Projected":
            #print "Buildings layer "+str(inMaskData)+ " has Projection: " +str(sr.Name)
            print "Buildings layer: " +str(sr.Name)
            print
        else:
            print "ERROR.....The Projection of buildings layer " +str(inMaskData)+ " is: " +str(sr.Name)
            print "Please assign projection to: " +str(inMaskData)
            print "LiDAR Analyst is going to exit now."
            sys.exit()

#=================================================.Creating Folders.=================================================>
      
        outfolderPath1 = str(dPath)+str(cityq)
        folderName1    = "HillShade"
        arcpy.CreateFolder_management(outfolderPath1,folderName1) # creates folder by the name of HillShade       
        folderName2    = "Reclass"
        arcpy.CreateFolder_management(outfolderPath1,folderName2) # creates folder by the name of Reclass         
        folderName5    = "Slope"
        arcpy.CreateFolder_management(outfolderPath1,folderName5) # creates folder by the name of sumRec_year for year         
        folderName6    = "Aspect"
        arcpy.CreateFolder_management(outfolderPath1,folderName6) # creates folder by the name of Aspect for year            
        folderName7    = "Summary"
        arcpy.CreateFolder_management(outfolderPath1,folderName7) # creates folder by the name of Summary for year
        folderName8    = "Combine"
        arcpy.CreateFolder_management(outfolderPath1,folderName8) # creates folder by the name of Combine
        outfolderPath2 = str(dPath)+str(cityq)+"/Combine/"
        folderName3    = "sumRec_month"
        arcpy.CreateFolder_management(outfolderPath2,folderName3) # creates folder by the name of sumRec_month for month                
        folderName4    = "sumRec_year"
        arcpy.CreateFolder_management(outfolderPath2,folderName4) # creates folder by the name of sumRec_year for year
        #print "Folders (Aspect, Combine, Hillshade, Reclass, Slope, & Summary) created for the city :" +str(cityq)
        print
        print "*********************:    HILLSHADE CALCULATION      :*********************"
        print

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
#=================================================.Hillshade calculation.==============================================>        
#
        fName = []   # Name of the fields                                                          #Line 5
        nAlt  = []   # Altitude
        aZi   = []   # Azimuth
        rows = arcpy.SearchCursor(inTable2)
        rowsz = arcpy.SearchCursor(inTablez2)
        cols = arcpy.ListFields(inTable2,"*","DOUBLE")
        for row,rowz in zip (rows,rowsz):
            for col in cols:
                fName.append(col.name)
                nAlt.append(row.getValue(col.name))
                aZi.append(rowz.getValue(col.name))
        count = 0
        inRaster = (str(dPath)+str(cityq))+"/reflective_surface/refsurf"  #LiDAR Raster
        #print inRaster
        for N,A,Z in zip (fName,nAlt,aZi):
            # Set local variables
            inRaster = "refsurf"
            Altitude = A
            Azimuth = Z
            modelShadows = "SHADOWS"
            zFactor = 1
            # Execute HillShade (HillShade calculation)
            inRaster = (str(dPath)+str(cityq))+"/reflective_surface/refsurf"  #LiDAR Raster
            if Azimuth > 0 or Altitude > 0:
                    outHillShade = Hillshade(inRaster, Azimuth, Altitude, modelShadows, zFactor) 
                    # Save the output
                    outHS = str(dPath)+str(cityq)+"/HillShade/"+str(N)
                    #print outHS
                    outHillShade.save(outHS)  #................ Integer
                    del outHillShade  
                    #print "Hillshade calculated for: City:"+str(cityq),  "Month_Day: "+str(N),"Altitude:"+str(A),"Azimuth:"+str(Z)
                    print "Day: "+str(N)+" ,","Altitude:"+str(A)+" ,","Azimuth:"+str(Z)
            count += 1
        print
        print "Processed step 1, Hillshade calculation completed." # for the all the months for City:" +str(cityq) #+ "is" +str(count)
#
        EndTime = time.clock()
        time = ((EndTime - StartTime)/60)
        print "Time taken to process step 1  is:" +str(time)+" Minutes" 
        print "Now Running LiDARP2 script to process steps 2-4"

except Exception as e:
    print e.message
    arcpy.AddError(e.message)
