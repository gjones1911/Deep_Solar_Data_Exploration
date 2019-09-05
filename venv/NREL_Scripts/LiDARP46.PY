import arcpy
import os.path
from arcpy import env
from arcpy import da
from arcpy.sa import *
import time
# Set environment settings
arcpy.env.overwriteOutput = True
# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")
zFactor = 1
outMeasurement = "DEGREE"
dPath = "C:/LiDAR/"
arcpy.env.workspace  = (str(dPath))
try:
        #inTable  = r"C:/LiDAR/LDR.gdb/Altitude"
        #inTablez = r"C:/LiDAR/LDR.gdb/Azimuth"
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

#............................................................................................................

#
#..................................................Dissolve... ...... .............................................................Line 153    
#
        print
        print "*********************:  Final Steps 46 - 49   :*********************"
        print
        combew11        = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combew_bldg")    #Output, combew_bldg     
        combs11         = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combs_bldg")    #Output, combs_bldg  
        combew22        = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combew_bldg10")    #Output, combew_bldg10  
        combs22         = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combs_bldg10")    #Output, combs_bldg10
        outFC1 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combew_bldgdissolve")       #Output, combew_bldg
        outFC2 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combs_bldgdissolve")       #Output, combS_bldg
        outFC3 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combew_bldgdissolve10")       #Output, combew_bldg10
        outFC4 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combs_bldgdissolve10")       #Output, combS_bldg10 
        # Execute Dissolve using LANDUSE and TAXCODE as Dissolve Fields
        arcpy.Dissolve_management(combew11, outFC1,"Bldg_FID",[["Bldg_Area","MEAN"],["SLPF","MEAN"],["flatarea","SUM"],["slopeconv","MEAN"],["slopearea","SUM"]],  "MULTI_PART", "DISSOLVE_LINES") #combew_bldg_dissolve
        arcpy.Dissolve_management(combs11,  outFC2,"Bldg_FID",[["Bldg_Area","MEAN"],["SLPF","MEAN"],["flatarea","SUM"],["slopeconv","MEAN"],["slopearea","SUM"]],  "MULTI_PART", "DISSOLVE_LINES") #combs_bldg_dissolve
        arcpy.Dissolve_management(combew22, outFC3,"Bldg_FID",[["Bldg_Area","MEAN"],["SLPF","MEAN"],["flatarea","SUM"],["slopeconv","MEAN"],["slopearea","SUM"]],  "MULTI_PART", "DISSOLVE_LINES") #combew_bldg_dissolve10
        arcpy.Dissolve_management(combs22,  outFC4,"Bldg_FID",[["Bldg_Area","MEAN"],["SLPF","MEAN"],["flatarea","SUM"],["slopeconv","MEAN"],["slopearea","SUM"]],  "MULTI_PART", "DISSOLVE_LINES") #combs_bldg_dissolve10
        #print "Processed step 46, Dissolve  fields for the city:" +str(cityq)
        print "Processed step 46, Dissolved"
        
#......................................................................................................................................
        #Taarget Feature Class
        zipinter = (str(dPath)+str(cityq)+"/Summary/summary.gdb/zips_intersect")
        dField = ["FID_zip_utm","FID_minboundgeom","area_zip_1"]
        fList = arcpy.ListFields(zipinter)
        nameList = []        
        for f in fList:
                nameList.append(f.name)
        for f in nameList:
                for f2 in dField:
                        if f == f2:
                           arcpy.DeleteField_management(zipinter,f2)
        #input feature class
        inFC1 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combew_bldgdissolve")        #Output, combew_bldg
        inFC2 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combs_bldgdissolve")         #Output, combS_bldg
        inFC3 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combew_bldgdissolve10")      #Output, combew_bldg10
        inFC4 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combs_bldgdissolve10")       #Output, combS_bldg10
        #Output Feature Class
        outFCZ1 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/zip_combew")                 #Output, combew_bldg
        outFCZ2 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/zip_combs")                  #Output, combS_bldg
        outFCZ3 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/zip_combew10")               #Output, combew_bldg10
        outFCZ4 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/zip_combs10")                #Output, combS_bldg10
        inFC   = [inFC1,inFC2,inFC3,inFC4]
        outFC  = [outFCZ1,outFCZ2,outFCZ3,outFCZ4]                     
        for FC1,FC2 in zip (inFC,outFC):
                fms = arcpy.FieldMappings()
                fms.addTable(zipinter)  #Target Feature Class
                fms.addTable(FC1)
                #print "fc is: " +str(FC1)
                AF1                = fms.findFieldMapIndex("MEAN_Bldg_Area") #("Bldg_Area")  # Mean_Building_Area   
                fm1                = fms.getFieldMap(AF1)
                fmname1             = fm1.outputField     
                fmname1.name       = "M_Barea"
                fmname1.aliasName  = "M_Barea"   # Average of Mean_Building_Area
                fm1.outputField    = fmname1
                fm1.mergeRule      = "mean"

                AF2                = fms.findFieldMapIndex("MEAN_SLPF") #("Bldg_Area")  # Mean_Building_Area
                fm2                = fms.getFieldMap(AF2)
                fmname2            = fm2.outputField     
                fmname2.name       = "M_SlP"
                fmname2.aliasName  = "M_SLP"   # Average of Mean_Building_Area
                fm2.outputField    = fmname2
                fm2.mergeRule      = "mean"

                AF3                = fms.findFieldMapIndex("SUM_flatarea") #("Bldg_Area")  # Mean_Building_Area
                fm3                = fms.getFieldMap(AF3)
                fmname3            = fm3.outputField     
                fmname3.name       = "S_FArea"
                fmname3.aliasName  = "S_Flatarea"   # Average of Mean_Building_Area
                fm3.outputField    = fmname3
                fm3.mergeRule      = "sum"

                AF4                = fms.findFieldMapIndex("MEAN_slopeconv") #("Bldg_Area")  # Mean_Building_Area
                fm4                = fms.getFieldMap(AF4)
                fmname4            = fm4.outputField     
                fmname4.name       = "M_SCarea"
                fmname4.aliasName  = "M_Slopconv"   # Average of Mean_Building_Area
                fm4.outputField    = fmname4
                fm4.mergeRule      = "mean"

                AF5                = fms.findFieldMapIndex("SUM_slopearea") #("Bldg_Area")  # Mean_Building_Area
                fm5                = fms.getFieldMap(AF5)
                fmname5            = fm5.outputField     
                fmname5.name       = "S_Sarea"
                fmname5.aliasName  = "S_Sloparea"   # Average of Mean_Building_Area
                fm5.outputField    = fmname5
                fm5.mergeRule      = "sum"
                        
                fms.replaceFieldMap(AF1,fm1)
                fms.replaceFieldMap(AF2,fm2)
                fms.replaceFieldMap(AF3,fm3)
                fms.replaceFieldMap(AF4,fm4)
                fms.replaceFieldMap(AF5,fm5)
                arcpy.SpatialJoin_analysis(zipinter,FC1,FC2,"JOIN_ONE_TO_ONE", "KEEP_ALL",fms,"INTERSECT")

        print "Processed step 47, Quad Summary for the city:" +str(cityq)
      
        print "Step 48: Repair combew geometries" 
        arcpy.RepairGeometry_management(combew11)           

        print "Step 49: Intersect combew_bldgs against aspfinal_poly"      
        arcpy.Intersect_analysis([combew11, (str(dPath)+str(cityq)+"/Aspect/aspfinal_poly.shp")], (str(dPath)+str(cityq)+"/Summary/summary.gdb/developable_planes"))

#........................................................................................................
        EndTime = time.clock()
        time = ((EndTime - StartTime)/60)
        print "Time taken to process steps 46-49 is " +str(time)+" Minutes" 
#.........................................................................................................
        print "Analysis completed for the city of: "+str(cityq)
        print "Creating files for final summary: "+str(cityq)
        print
        #print "Please run the LiDARDelete script to delete the extra files."
        #arcpy.CheckInExtension("Spatial")

except Exception as e:
    print e.message
    arcpy.AddError(e.message)

