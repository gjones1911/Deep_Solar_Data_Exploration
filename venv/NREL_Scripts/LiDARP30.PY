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

        
        qry1 = '"City_1"'+" ='"+str(cityq)+"'"  
        lyr1 = arcpy.MakeFeatureLayer_management(inTable,"lyr")
        inTable2 = arcpy.SelectLayerByAttribute_management(lyr1,"NEW_SELECTION",qry1)        
        CityName = "City"
        CityF = set()
        cities = arcpy.SearchCursor(inTable2)
        for cityn in cities:
            CityF.add(cityn.getValue(CityName))
            #print "List of cities needs to be analyzed:" + str(CityF)
            for Val1 in CityF:
                cityq2 = Val1
                #print "city name is :"+str(cityq)
                qry2 =  '"City"'+" ='"+str(cityq2)+"'"
                #print "The City being analyzed:" +str(qry2)

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




#............................................................................................................


#
#....................................................................... Clip to buildings ....................................................Line 107, 110, 113, 117 & 120
#
        print
        print "*********************:  Clip to buildings  :*********************"
        print
        # Set local variables        
        clip_features = inMaskData
        xy_tolerance = ""
        inFeatureCL2  = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_slppoly")             #Input: cs_slppoly
        out_feature_class2 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_slpClip")     #Output, combs_slpClip       
        # Execute Clip / adding field
        arcpy.Clip_analysis(inFeatureCL2 , clip_features, out_feature_class2, xy_tolerance)              #line 107  (clipping)  Output,& creating combs_slpClip
        #print "Processed step 30 A , Clip (cs_slppoly) / Add field  for the city:" +str(cityq)
        print "Processed step 30 A, Clip (cs_slppoly)"
        arcpy.AddField_management(out_feature_class2,"flatarea",  "DOUBLE","", "","5")                   #line 110  (adding field)                                 
        geometryField = arcpy.Describe(out_feature_class2).shapeFieldName 
        cursor = arcpy.UpdateCursor(out_feature_class2)        
        for row in cursor:
            AreaValue = row.getValue(geometryField).area
            row.setValue("flatarea",AreaValue) #Write area value to field
            cursor.updateRow(row)
        del row, cursor #Clean up cursor objects
        #print "Processed step 31 A, Clip (cs_slppoly) / Add field  for the city:" +str(cityq)
        print "Processed step 31 A, Clip (cs_slppoly)"
        arcpy.AddField_management(out_feature_class2,"slopeconv", "DOUBLE","", "","5")                   #line 113  (adding field) 
        expression1 = "1/(math.cos((!SLPF!)*3.14/180))"
        arcpy.CalculateField_management(out_feature_class2, "slopeconv", expression1, "PYTHON_9.3", "")   #line 113
        #print "Processed step 32 A, Clip (cs_slppoly) / Add field  for the city:" +str(cityq)
        print "Processed step 32 A, Clip (cs_slppoly)"
        arcpy.AddField_management(out_feature_class2,"slopearea", "DOUBLE","", "","5")                   #line 117  (adding field) 
        expression2 = "!flatarea!*!slopeconv!"
        arcpy.CalculateField_management(out_feature_class2, "slopearea", expression2, "PYTHON_9.3", "")   #line 117
        #print "Processed step 33 A, Clip (cs_slppoly) / Add field  for the city:" +str(cityq)
        print "Processed step 33 A, Clip (cs_slppoly)"
        slopeqry1 = '"slopearea" >= 9.99999'                   ## Changed for second round
        #slopeqry1 = '"slopearea" >= 19.99999'
        slplyr1 = arcpy.MakeFeatureLayer_management(out_feature_class2,"slplyr")
        out_featclas22 = arcpy.SelectLayerByAttribute_management(slplyr1,"NEW_SELECTION",slopeqry1)       #line 120
        #slpcnt = arcpy.GetCount_management(out_featclas22)
        #print slpcnt        
        out_featclas222  = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_slpclip10")       #Output, combs_slpclip10
        arcpy.CopyFeatures_management(slplyr1, out_featclas222)                                           
        #print "Processed step 34 A, Clip / Add fields / calculations for the city:" +str(cityq)
        print "Processed step 34 A, Clip (cs_slppoly)"
        #
        #
        #
        # Set local variables
        inFeatureCL3 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_slppoly")           # input: combew_slp_poly
        out_feature_class3 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_slpClip")     # combew_slp_Clip  
        # Execute Clip / adding field
        arcpy.Clip_analysis(inFeatureCL3 , clip_features, out_feature_class3, xy_tolerance)              #line 107  (clipping)& creating combew_slp_Clip
        #print "Processed step 30 B, Clip (cw_slppoly) / Add field  for the city:" +str(cityq)
        print "Processed step 30 B, Clip (cw_slppoly)"
        arcpy.AddField_management(out_feature_class3,"flatarea",  "DOUBLE","", "","5")                   #line 110  (adding field)        
        CursorFieldNames = ["SHAPE@","flatarea"]  #SHAPE@ is a shape field                               #line 110 calculate geometry
        cursor = arcpy.da.UpdateCursor(out_feature_class3,CursorFieldNames)
        for row in cursor:
            AreaValue = row[0].area #Read area value as double
            row[1] = AreaValue #Write area value to field
            cursor.updateRow(row)
        del row, cursor #Clean up cursor objects
        #print "Processed step 31 B, Clip (cw_slppoly) / Add field  for the city:" +str(cityq)
        print "Processed step 31 B, Clip (cw_slppoly)"
        arcpy.AddField_management(out_feature_class3,"slopeconv", "DOUBLE","", "","5")                         #line 113  (adding field)
        expression3 = "1/(math.cos((!SLPF!)*3.14/180))"
        arcpy.CalculateField_management(out_feature_class3, "slopeconv", expression3, "PYTHON_9.3", "")        #line 113
        #print "Processed step 32 B, Clip (cw_slppoly) / Add field  for the city:" +str(cityq)
        print "Processed step 32 B, Clip (cw_slppoly)"
        arcpy.AddField_management(out_feature_class3,"slopearea", "DOUBLE","", "","5")                         #line 117  (adding field)        
        expression4 = "!flatarea!*!slopeconv!"
        arcpy.CalculateField_management(out_feature_class3, "slopearea", expression4, "PYTHON_9.3", "")        #line 117
        #print "Processed step 33 B, Clip (cs_slppoly) / Add field  for the city:" +str(cityq)
        print "Processed step 33 B, Clip (cw_slppoly)"
        slopeqry2 = '"slopearea" >= 9.99999'
        #slopeqry2 = '"slopearea" >= 19.99999'
        slplyr2 = arcpy.MakeFeatureLayer_management(out_feature_class3,"slplyr0")
        out_feature_class33 = arcpy.SelectLayerByAttribute_management(slplyr2,"NEW_SELECTION",slopeqry2)       #line 120 
        slpcnt2 = arcpy.GetCount_management(out_feature_class33)
        #print slpcnt2
        out_featclas333 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_slpclip10")
        arcpy.CopyFeatures_management(slplyr2, out_featclas333)                                                #combew_slpclip10       
        #print "Processed step 34 B, Clip (cw_slppoly) / Add field / calculations for the city:" +str(cityq)
        print "Processed step 34 B, Clip (cw_slppoly)"
#
#
#=================================================. SUMMARY.=================================================================> 
#


#
#.......................... Minimum boundary Geometry ...............................................................................Line 127, 
#
        print
        print "*********************:  SUMMARIZATION  :*********************"
        print
        # Create variables for the input and output feature classes
        #inBld1 = ("C:/LiDAR/Base_map/"+str(cityq)+str("_2d_buildings")+str(".shp"))
        import arcpy
        outFolderP2 = (str(dPath)+str(cityq)+"/Summary")
        outName2   =  "summary.gdb"
        arcpy.CreateFileGDB_management(outFolderP2, outName2)        
        inBld1 = inMaskData
        inBld2 = arcpy.MakeFeatureLayer_management(inBld1, "bldg_lyr")
        inBld3 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/bldg") 
        arcpy.CopyFeatures_management(inBld2,inBld3)
        dField = ["id","AREA_M2","AVGHT_M","MINHT_M","MAXHT_M","BASE_M","LEN","WID","ORIENT8"]
        fList = arcpy.ListFields(inBld3)
        nameList = []        
        for f in fList:
                nameList.append(f.name)
        for f in nameList:
                for f2 in dField:
                        if f == f2:
                           arcpy.DeleteField_management(inBld3,f2)

        #print "Processed step 35,  Minimum boundary Geometry created for city:" +str(cityq)
        print "Processed step 35, copied Feature Class for Minimum boundary Geometry creation"
        #inBld = (str(dPath)+str(cityq)+"/Combine/"+str("bldg")+str(".shp"))                                     ######## needs to creat for every city########################
        outmbg1 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/minboundgeom")                                     
        # Use MinimumBoundingGeometry function to get a convex hull area
        #for each cluster of trees which are multipoint features
        arcpy.MinimumBoundingGeometry_management(inBld3, outmbg1, "CONVEX_HULL", "ALL")                           #Output, minboundgeom
        arcpy.AddField_management(outmbg1,"area_zip", "DOUBLE","", "","5") 
        #print "Processed step 36,  Minimum boundary Geometry created for city:" +str(cityq)
        print "Processed step 36, Minimum boundary Geometry created"
#
#.......................... zip file ..................................................................................Line 123, 129
#        
        inFeatureZ1 = ("C:/LiDAR/Base_map/zip.shp")                                                     #Input, zip
        inFeatureZ2 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/minboundgeom")               # clipping layer, minboundgeom
        zip1 = arcpy.MakeFeatureLayer_management(inFeatureZ1, "zip_lyr")
        zip2 = arcpy.SelectLayerByLocation_management (zip1, 'intersect', inFeatureZ2)
        zip3 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/nzip")                       #Output, nzip
        arcpy.CopyFeatures_management(zip2, zip3)                                                #line 123   Zips
        deletefields = ["FIPSSTCO","STATE_FIPS"]
        arcpy.DeleteField_management(zip3,deletefields) #Delete the extra fields from output feature class
        
        #print "Processed step 37,  nzip for city:" +str(cityq)
        print "Processed step 37, nzip created"
        zip4 = (str(dPath)+str(cityq)+"/Summary/summary.gdb/zip_utm")                    # for new projection utm       
        outCS = arcpy.SpatialReference(str(dPath)+str(cityq)+"/Combine/"+str("combs_poly.prj"))   #the file use for projection
        #print out_coordinate_system
        arcpy.Project_management(zip3, zip4 ,outCS)
        #print "Processed step 38,  UTM Projection calculated for the zip file of city:" +str(cityq)
        print "Processed step 38, UTM Projection calculated for the zip layer"
        arcpy.AddField_management(zip4,"area_zip", "DOUBLE","", "","5")                          #line 129   Zips
        CursorFieldNameZ = ["SHAPE@","area_zip"]  #SHAPE@ is a shape field                       #line 129 calculate geometry
        cursor = arcpy.da.UpdateCursor(zip4,CursorFieldNameZ)
        for row in cursor:
            AreaValue = row[0].area #Read area value as double
            row[1] = AreaValue #Write area value to field        
            cursor.updateRow(row)
        del row, cursor #Clean up cursor objects
        #print "Processed step 39, Area calculated for the zip file of city:" +str(cityq)
        print "Processed step 39, Area calculated for the zip layer"


#
#...................................................... Intersect ......................................................................Line 132,
#
        inFeatures = [zip4, outmbg1]                                                               #Input, zips & minboundgeom
        zipinter = (str(dPath)+str(cityq)+"/Summary/summary.gdb/zips_intersect")           #Output, zips_intersect
        arcpy.Intersect_analysis(inFeatures, zipinter, "", "", "")                                 
        #print "Processed step 40, zips Intersect file created for city:" +str(cityq)
        print "Processed step 40, zips Intersect layer created"
#
#...................................................... ...... .....................................................................Line 135,138
#       
        arcpy.AddField_management(zipinter,"Area_int", "DOUBLE","", "","5")                         #line 135   zips_intersect        
        CursorFieldNameZ = ["SHAPE@","Area_int"]  #SHAPE@ is a shape field                          #line 135 calculate geometry
        cursor = arcpy.da.UpdateCursor(zipinter,CursorFieldNameZ)
        for row in cursor:
            AreaValue = row[0].area #Read area value as double
            row[1] = AreaValue #Write area value to field
            cursor.updateRow(row)
        del row, cursor #Clean up cursor objects
        #print "Processed step 41, Area_int field added & area calculated for city:" +str(cityq)
        print "Processed step 41, Area_int field added & area calculated"
        
        arcpy.AddField_management(zipinter,"zip_pct", "DOUBLE","", "","5")                         #line 138   zips_intersect
        expression5 = "(!Area_int!/!Area_zip!)"
        arcpy.CalculateField_management(zipinter, "zip_pct", expression5, "PYTHON_9.3", "")        #line 138
        #print "Processed step 42, Percent Area calculated for zip file of city:" +str(cityq)
        print "Processed step 42, Percent Area calculated for zip layer"
#
#...................................................... .calculate flate area of building rooftop..........................................................Line 142,
#
        bld = (str(dPath)+str(cityq)+"/Summary/summary.gdb/bldg")                      #Input, bldg
        arcpy.AddField_management(bld,"Bldg_Area", "DOUBLE","", "","5")                         #line 141   building layer
        arcpy.AddField_management(bld,"Bldg_FID", "LONG","", "","5")
        CursorFieldNameZ = ["OBJECTID","Bldg_FID"]  #SHAPE@ is a shape field                       #line 129 calculate geometry
        cursor = arcpy.da.UpdateCursor(bld,CursorFieldNameZ)
        for row in cursor:
            AreaValue = row[0] 
            row[1] = AreaValue        
            cursor.updateRow(row)
        del row, cursor 
        #print "complete"    
        CursorFieldNameZ = ["SHAPE@","Bldg_Area"]  #SHAPE@ is a shape field                     #line 141 calculate geometry
        cursor = arcpy.da.UpdateCursor(bld,CursorFieldNameZ)
        for row in cursor:
            AreaValue = row[0].area #Read area value as double
            row[1] = AreaValue #Write area value to field
            cursor.updateRow(row)
        del row, cursor #Clean up cursor objects
        #print "Processed step 43, bldarea field added & area calculated for city:" +str(cityq)
        print "Processed step 43, bldarea field added & area calculated"

#
#..................................................Spatial join... ...... ...........................................................Line 144,      
#
        out_feature_class = (str(dPath)+str(cityq)+"/Summary/summary.gdb/zips_bldg")           #Output, zips_bldg
        fieldmappings = arcpy.FieldMappings() 
        fieldmappings.addTable(zipinter)   #targetFeatures
        fieldmappings.addTable(bld)        #joinFeatures
        areaField = fieldmappings.findFieldMapIndex("Bldg_Area")
        fieldmap = fieldmappings.getFieldMap(areaField)
        field = fieldmap.outputField
        field.name = "F_Area"
        field.aliasName = "Total_area"
        fieldmap.outputField = field
        fieldmap.mergeRule = "sum"
        fieldmappings.replaceFieldMap(areaField, fieldmap)      
        arcpy.SpatialJoin_analysis(zipinter,bld,out_feature_class,"", "",fieldmappings,"")
        deletefields = ["area_zip_1"]
        arcpy.DeleteField_management(out_feature_class,deletefields)
        #print "Processed step 44, spatial join between zip_intersect and city buildings for city:" +str(cityq)
        print "Processed step 44, spatial join between zip_intersect and city buildings"
#
#..................................................Spatial join... ...... ...........................................................Line   148     
#
        
        combew1    = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_slpclip")    #Input, combew_slp_clip
        combs1     = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_slpclip")     #Input, combs_slp_clip
        combew2    = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_slpclip10")  #Input, combew_slp_clip10
        combs2     = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_slpclip10")   #Input, combs_slp_clip10
        #output files
        combew11        = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combew_bldg")    #Output, combew_bldg     
        combs11         = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combs_bldg")    #Output, combs_bldg  
        combew22        = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combew_bldg10")    #Output, combew_bldg10  
        combs22         = (str(dPath)+str(cityq)+"/Summary/summary.gdb/combs_bldg10.")    #Output, combs_bldg10
        arcpy.SpatialJoin_analysis(combew1,   bld, combew11,  "JOIN_ONE_TO_ONE", "KEEP_ALL","#","INTERSECT","","")
        arcpy.SpatialJoin_analysis(combs1,    bld, combs11,   "JOIN_ONE_TO_ONE", "KEEP_ALL","#","INTERSECT","","")
        arcpy.SpatialJoin_analysis(combew2,   bld, combew22,  "JOIN_ONE_TO_ONE", "KEEP_ALL","#","INTERSECT","","")
        arcpy.SpatialJoin_analysis(combs2,    bld, combs22,   "JOIN_ONE_TO_ONE", "KEEP_ALL","#","INTERSECT","","")
        EndTime = time.clock()
        #print "Processed step 45, spatial join between buldings and clip files for city:" +str(cityq)
        print "Processed step 45, spatial join between buldings and cliped layers"
        print
        print "Time taken to process steps 30- 45 %s Minutes:" % ((EndTime - StartTime)/60)
        print "Now running LiDarP46 to processe steps 46 & 47"
        print
        #time.sleep(5)


except Exception as e:
    print e.message
    arcpy.AddError(e.message)
