import arcpy, csv
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
FPath = "C:/LiDAR/FinalSummary/" 
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
                #print "The Part of the City being analyzed is:" +str(qry1)
#........................................................................................................

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
        
        qry1 = '"City_1"'+" ='"+str(cityq)+"'"   
        lyr1 = arcpy.MakeFeatureLayer_management(inTable,"lyr")
        inTable2 = arcpy.SelectLayerByAttribute_management(lyr1,"NEW_SELECTION",qry1)        
        StateName = "STATE"
        State = set()
        states = arcpy.SearchCursor(inTable2)
        for staten in states:
            State.add(staten.getValue(StateName))
            #print "List of State needs to be analyzed:" + str(staten)
            for Val1 in State:
                stateq2 = Val1
                #print "city name is :"+str(cityq)
                qry3 =  '"State"'+" ='"+str(stateq2)+"'"
                #print "The state of the City being analyzed:" +str(qry3) 

        YearName = "Year_"
        YearF = set()
        Years = arcpy.SearchCursor(inTable2)
        for yearn in Years:
            YearF.add(yearn.getValue(YearName))
            #print "List of years needs to be analyzed:" + str(YearF)
            for Val1 in YearF:
                year2 = Val1
                #print "city name is :"+str(cityq)
                qry4 =  '"Year_"'+" ='"+str(year2)+"'"
                #print "The Year being analyzed:" +str(qry4)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Merging input feature class
        print
        print "*********************:  Final Summary    :*********************"
        print
        folderNames    = str(cityq2)+'_'+str(stateq2)        
        folderName1    = str(cityq2)+'_'+str(year2)
        #print folderName1
        #print "the path is" +(str(FPath)+str(cityq2))
        arcpy.env.workspace = (str(FPath)+"/"+str(folderNames)+"/"+str(folderName1))   
        outfolderPath1 = (str(FPath)+str(folderNames)+"/"+str(folderName1))
        folderNamez1    = "Zips"
        arcpy.CreateFolder_management(outfolderPath1,folderNamez1) # creates folder by the name of Zips             
        workspaces = arcpy.ListWorkspaces("*", "FileGDB")
        #print workspaces
        print "Creation of Final sunmmary for the city of:"+str(folderName1)
        #print outfolderPath1
        outFolderP1 = (str(outfolderPath1)+"/Zips")
        outName   =  "Fsummary.gdb"
        arcpy.CreateFileGDB_management(outfolderPath1, outName)
        FN = ["combs.gdb","combs10.gdb","combew.gdb","combew10.gdb"]
        for FN2 in FN:
                arcpy.CreateFileGDB_management(outFolderP1, FN2)
        count = 0
        for WS in workspaces:
                count +=1
                cnt = str(count)
                arcpy.CopyFeatures_management(str(WS)+"/zips_bldg",str(outfolderPath1)+"/Fsummary.gdb/zips_bldg")
                arcpy.CopyFeatures_management(str(WS)+"/zip_combs1", str(outfolderPath1)+"/Zips/combs.gdb/zip_combs"+str(cnt))
                arcpy.CopyFeatures_management(str(WS)+"/zip_combs101", str(outfolderPath1)+"/Zips/combs10.gdb/zip_combs10"+str(cnt))
                arcpy.CopyFeatures_management(str(WS)+"/zip_combew1", str(outfolderPath1)+"/Zips/combew.gdb/zip_combew"+str(cnt))
                arcpy.CopyFeatures_management(str(WS)+"/zip_combew101", str(outfolderPath1)+"/Zips/combew10.gdb/zip_combew10"+str(cnt))

                
#..............................................................................................1
        arcpy.env.workspace = (str(outfolderPath1)+"/Zips/combs.gdb")
        inFC = arcpy.ListFeatureClasses()
        #for inFC in featureclasses:
        inZips1 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combsm")
        arcpy.Merge_management(inFC, inZips1, "")
               
        outFC2 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combs")
        arcpy.Dissolve_management(inZips1, outFC2, "ZIP",[["Join_Count","SUM"],["S_FArea","SUM"]], "", "DISSOLVE_LINES")
        fieldPrecision = 9        
        arcpy.AddField_management(outFC2,"Count_south", "DOUBLE",fieldPrecision)
        countField1 =  "SUM_Join_Count"
        calcField   =  "Count_south"
        arcpy.CalculateField_management(outFC2,calcField,"!"+str(countField1)+"!","PYTHON_9.3","")
        #fieldPrecision = 6       
        arcpy.AddField_management(outFC2,"Flatarea_south", "DOUBLE",fieldPrecision)
        countField1 =  "SUM_S_FArea"  # Alias is "S_Flatarea"
        calcField   =  "Flatarea_south"
        arcpy.CalculateField_management(outFC2,calcField,"!"+str(countField1)+"!","PYTHON_9.3","")      
        dField = ["SUM_Join_Count","TARGET_FID","ZIP_NAME","COUNTY","STATE","ZIP","area_zip","Area_int","zip_pct","Bldg_FID","M_Barea","M_SlP","SUM_S_FArea","M_SCarea","S_Sarea"]
        fList = arcpy.ListFields(outFC2)
        nameList = []        
        for f in fList:
                nameList.append(f.name)
        for f in nameList:
                for f2 in dField:
                        if f == f2:
                           arcpy.DeleteField_management(outFC2,f2)


#................................................................................................2               
        arcpy.env.workspace = (str(outfolderPath1)+"/Zips/combew.gdb")
        inFC = arcpy.ListFeatureClasses()
        #for inFC in featureclasses:
        inZips1 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combewm")
        arcpy.Merge_management(inFC, inZips1, "")
        #fieldPrecision = 6
        outFC2 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combew")
        arcpy.Dissolve_management(inZips1, outFC2, "ZIP",[["Join_Count","SUM"],["S_FArea","SUM"]], "", "DISSOLVE_LINES")

        arcpy.AddField_management(outFC2,"Count_eastwest", "DOUBLE",fieldPrecision)
        countField1 =  "SUM_Join_Count"
        calcField   =  "Count_eastwest"
        arcpy.CalculateField_management(outFC2,calcField,"!"+str(countField1)+"!","PYTHON_9.3","")
        #fieldPrecision = 6       
        arcpy.AddField_management(outFC2,"Flatarea_eastwest", "DOUBLE",fieldPrecision)
        countField1 =  "SUM_S_FArea"  # Alias is "S_Flatarea"
        calcField   =  "Flatarea_eastwest"
        arcpy.CalculateField_management(outFC2,calcField,"!"+str(countField1)+"!","PYTHON_9.3","")      
        dField = ["SUM_Join_Count","TARGET_FID","ZIP_NAME","COUNTY","STATE","ZIP","area_zip","Area_int","zip_pct","Bldg_FID","M_Barea","M_SlP","SUM_S_FArea","M_SCarea","S_Sarea"]
        fList = arcpy.ListFields(outFC2)
        nameList = []        
        for f in fList:
                nameList.append(f.name)
        for f in nameList:
                for f2 in dField:
                        if f == f2:
                           arcpy.DeleteField_management(outFC2,f2)      

#..................................................................................................3

        arcpy.env.workspace = (str(outfolderPath1)+"/Zips/combs10.gdb")
        inFC = arcpy.ListFeatureClasses()
        #for inFC in featureclasses:
        inZips1 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combs10m")        
        arcpy.Merge_management(inFC, inZips1, "")
        outFC2 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combs10")
        arcpy.Dissolve_management(inZips1, outFC2, "ZIP",[["Join_Count","SUM"],["S_FArea","SUM"]], "", "DISSOLVE_LINES")
        #fieldPrecision = 6       
        arcpy.AddField_management(outFC2,"Count_south10", "DOUBLE",fieldPrecision)
        countField1 =  "SUM_Join_Count"
        calcField   =  "Count_south10"
        arcpy.CalculateField_management(outFC2,calcField,"!"+str(countField1)+"!","PYTHON_9.3","")
        #fieldPrecision = 6       
        arcpy.AddField_management(outFC2,"Flatarea_south10", "DOUBLE",fieldPrecision)
        countField1 =  "SUM_S_FArea"  # Alias is "S_Flatarea"
        calcField   =  "Flatarea_south10"
        arcpy.CalculateField_management(outFC2,calcField,"!"+str(countField1)+"!","PYTHON_9.3","")      
        dField = ["SUM_Join_Count","TARGET_FID","ZIP_NAME","COUNTY","STATE","ZIP","area_zip","Area_int","zip_pct","Bldg_FID","M_Barea","M_SlP","SUM_S_FArea","M_SCarea","S_Sarea"]
        fList = arcpy.ListFields(outFC2)
        nameList = []        
        for f in fList:
                nameList.append(f.name)
        for f in nameList:
                for f2 in dField:
                        if f == f2:
                           arcpy.DeleteField_management(outFC2,f2)

#................................................................................................4
        arcpy.env.workspace = (str(outfolderPath1)+"/Zips/combew10.gdb")
        inFC = arcpy.ListFeatureClasses()
        #for inFC in featureclasses:
        inZips1 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combew10m")
        arcpy.Merge_management(inFC, inZips1, "")
        #fieldPrecision = 6              
        outFC2 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combew10")
        arcpy.Dissolve_management(inZips1, outFC2, "ZIP",[["Join_Count","SUM"],["S_FArea","SUM"]], "", "DISSOLVE_LINES")

        arcpy.AddField_management(outFC2,"Count_eastwest10", "DOUBLE",fieldPrecision)
        countField1 =  "SUM_Join_Count"
        calcField   =  "Count_eastwest10"
        arcpy.CalculateField_management(outFC2,calcField,"!"+str(countField1)+"!","PYTHON_9.3","")
        #fieldPrecision = 6       
        arcpy.AddField_management(outFC2,"Flatarea_eastwest10", "DOUBLE",fieldPrecision)
        countField1 =  "SUM_S_FArea"  # Alias is "S_Flatarea"
        calcField   =  "Flatarea_eastwest10"
        arcpy.CalculateField_management(outFC2,calcField,"!"+str(countField1)+"!","PYTHON_9.3","")      
        dField = ["SUM_Join_Count","TARGET_FID","ZIP_NAME","COUNTY","STATE","ZIP","area_zip","Area_int","zip_pct","Bldg_FID","M_Barea","M_SlP","SUM_S_FArea","M_SCarea","S_Sarea"]
        fList = arcpy.ListFields(outFC2)
        nameList = []        
        for f in fList:
                nameList.append(f.name)
        for f in nameList:
                for f2 in dField:
                        if f == f2:
                           arcpy.DeleteField_management(outFC2,f2)

        Del1 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combsm")
        Del2 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combs10m")
        Del3 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combewm")
        Del4 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combew10m")
        featurelist = [Del1,Del2,Del3,Del4]        
        for feature in featurelist:
                arcpy.Delete_management(feature, "")

        print "Deleted the extra files from:"+str(outfolderPath1)+"/Fsummary.gdb/"
        print "Summarization is in progress.........."
#........................
        
        inZips1 = (str(outfolderPath1)+"/Fsummary.gdb/zips_bldg") #################
        fields1 = [ "Region", "ZIP_NAME2", "COUNTY2", "STATE2"]
 
        fieldPrecision = 50
        for F in fields1:
                arcpy.AddField_management(inZips1,F, "TEXT",fieldPrecision)

        countField1 =  '"'+str(cityq2)+'_'+str(stateq2)+'_'+str(year2)+'"'
        calcField   =  "Region"
        arcpy.CalculateField_management(inZips1,calcField,countField1,"PYTHON_9.3","")
        countField1 =  "!ZIP_NAME!"
        calcField   =  "ZIP_NAME2"
        arcpy.CalculateField_management(inZips1,calcField,countField1,"PYTHON_9.3","")
        countField1 =  "!COUNTY!"
        calcField   =  "COUNTY2"
        arcpy.CalculateField_management(inZips1,calcField,countField1,"PYTHON_9.3","")
        countField1 =  "!STATE!"
        calcField   =  "STATE2"
        arcpy.CalculateField_management(inZips1,calcField,countField1,"PYTHON_9.3","")
        dField1 = ["ZIP_NAME", "COUNTY", "STATE"]
        for dF in dField1:
                arcpy.DeleteField_management(inZips1,dF)
        fields1 = ["ZIP_NAME", "COUNTY", "STATE"]
        for F in fields1:
                arcpy.AddField_management(inZips1,F, "TEXT",fieldPrecision)
        countField1 =  "!ZIP_NAME2!"
        calcField   =  "ZIP_NAME"
        arcpy.CalculateField_management(inZips1,calcField,countField1,"PYTHON_9.3","")
        countField1 =  "!COUNTY2!"
        calcField   =  "COUNTY"
        arcpy.CalculateField_management(inZips1,calcField,countField1,"PYTHON_9.3","")
        countField1 =  "!STATE2!"
        calcField   =  "STATE"
        arcpy.CalculateField_management(inZips1,calcField,countField1,"PYTHON_9.3","")
        dField1 = ["ZIP_NAME2", "COUNTY2", "STATE2"]
        for dF in dField1:
                arcpy.DeleteField_management(inZips1,dF)

        fieldPrecision = 20
        fields1 = ["Area_zip_meters", "Area_intersect","Zip_percent","Count_total_buildings", "Area_total_buildings"]
        for F in fields1:
                arcpy.AddField_management(inZips1,F, "DOUBLE",fieldPrecision)
        countField1 =  "!area_zip!"
        calcField   =  "Area_zip_meters"
        arcpy.CalculateField_management(inZips1,calcField,countField1,"PYTHON_9.3","")
        countField1 =  "!Area_int!"
        calcField   =  "Area_intersect"
        arcpy.CalculateField_management(inZips1,calcField,countField1,"PYTHON_9.3","")
        countField1 =  "!zip_pct!"
        calcField   =  "Zip_percent"
        arcpy.CalculateField_management(inZips1,calcField,countField1,"PYTHON_9.3","")
        countField1 =  "!Join_Count!"
        calcField   =  "Count_total_buildings"
        arcpy.CalculateField_management(inZips1,calcField,countField1,"PYTHON_9.3","")
        countField1 =  "F_Area"  # Alias is "Total_area"
        calcField   =  "Area_total_buildings"
        arcpy.CalculateField_management(inZips1,calcField,"!"+str(countField1)+"!","PYTHON_9.3","")      
        dField = ["Id","bldgarea","area_zip", "Area_int", "zip_pct","Join_Count","TARGET_FID","FID_zip_utm","FID_minboundgeom","F_Area","BLDGID","Bldg_FID"]
        fList = arcpy.ListFields(inZips1)
        nameList = []        
        for f in fList:
                nameList.append(f.name)
        for f in nameList:
                for f2 in dField:
                        if f == f2:
                           arcpy.DeleteField_management(inZips1,f2)

        #print "Added the required fields"
# intersect
        outZips2 = (str(outfolderPath1)+"/Fsummary.gdb/zip_summary2")
        #print "Output name:"+str(outZips2)
        arcpy.env.workspace = (str(outfolderPath1)+"/Fsummary.gdb")
        fc = ["zips_bldg","zip_combs","zip_combew","zip_combs10","zip_combew10"]
        arcpy.Intersect_analysis(fc, outZips2, "NO_FID", "", "INPUT") 
# create new layer of selected records to delete the fields with Null values
        outZips3 = (str(outfolderPath1)+"/Fsummary.gdb/zip_summary")
        inTablezs2 = (str(outfolderPath1)+"/Fsummary.gdb/zip_summary2")
        qry = '"Count_total_buildings" > 0'                   ## Changed for second round
        lyr1 = arcpy.MakeFeatureLayer_management(inTablezs2,"lyr")
        inTable2 = arcpy.SelectLayerByAttribute_management(lyr1,"NEW_SELECTION",qry)
        arcpy.CopyFeatures_management(lyr1, outZips3)
        arcpy.Delete_management(outZips2, "") 
        fieldPrecision = 9  
        newFields = ["Pct_Count_south","Pct_Flatarea_south","Pct_Count_eastwest","Pct_Flatarea_eastwest","Pct_Count_south10"\
                     ,"Pct_Flatarea_south10","Pct_Count_eastwest10","Pct_Flatarea_eastwest10","Check_s10_count","Check_s10_area"\
                     ,"Check_ew10_count","Check_ew10_area","Check_south_count","Check_south_area","Check_ew_count","Check_ew_area"\
                     ,"Check_10_count","Check_10_area"]
        for NF in newFields:
                arcpy.AddField_management(outZips3,NF, "DOUBLE",fieldPrecision)


        expression1 = "(float(!Count_south!)/float(!Count_total_buildings!))"
        arcpy.CalculateField_management(outZips3, "Pct_Count_south", expression1, "PYTHON_9.3", "")

        expression2 = "(!Flatarea_south!/!Area_total_buildings!)"
        arcpy.CalculateField_management(outZips3, "Pct_Flatarea_south", expression2, "PYTHON_9.3", "")

        expression3 = "(float(!Count_eastwest!)/float(!Count_total_buildings!))"
        arcpy.CalculateField_management(outZips3, "Pct_Count_eastwest", expression3, "PYTHON_9.3", "")

        expression4 = "(!Flatarea_eastwest!/!Area_total_buildings!)"
        arcpy.CalculateField_management(outZips3, "Pct_Flatarea_eastwest", expression4, "PYTHON_9.3", "")

        expression5 = "(float(!Count_south10!)/float(!Count_total_buildings!))"
        arcpy.CalculateField_management(outZips3, "Pct_Count_south10", expression5, "PYTHON_9.3", "")

        expression6 = "(!Flatarea_south10!/!Area_total_buildings!)"
        arcpy.CalculateField_management(outZips3, "Pct_Flatarea_south10", expression6, "PYTHON_9.3", "")

        expression7 = "(float(!Count_eastwest10!)/float(!Count_total_buildings!))"
        arcpy.CalculateField_management(outZips3, "Pct_Count_eastwest10", expression7, "PYTHON_9.3", "")

        expression8 = "(!Flatarea_eastwest10!/!Area_total_buildings!)"
        arcpy.CalculateField_management(outZips3, "Pct_Flatarea_eastwest10", expression8, "PYTHON_9.3", "")

        expression9 = "(!Count_south!-!Count_south10!)"
        arcpy.CalculateField_management(outZips3, "Check_s10_count", expression9, "PYTHON_9.3", "")

        expression10 = "(!Flatarea_south!-!Flatarea_south10!)"
        arcpy.CalculateField_management(outZips3, "Check_s10_area", expression10, "PYTHON_9.3", "")

        expression11 = "(!Count_eastwest!-!Count_eastwest10!)"
        arcpy.CalculateField_management(outZips3, "Check_ew10_count", expression11, "PYTHON_9.3", "")

        expression12 = "(!Flatarea_eastwest!-!Flatarea_eastwest10!)"
        arcpy.CalculateField_management(outZips3, "Check_ew10_area", expression12, "PYTHON_9.3", "")

        expression13 = "(!Count_eastwest!-!Count_south!)"
        arcpy.CalculateField_management(outZips3, "Check_south_count", expression13, "PYTHON_9.3", "")
        
        expression14 = "(!Flatarea_eastwest!-!Flatarea_south!)"
        arcpy.CalculateField_management(outZips3, "Check_south_area", expression14, "PYTHON_9.3", "")

        expression15 = "(!Count_total_buildings!-!Count_eastwest!)"
        arcpy.CalculateField_management(outZips3, "Check_ew_count", expression15, "PYTHON_9.3", "")

        expression16 = "(!Area_total_buildings!-!Flatarea_eastwest!)"
        arcpy.CalculateField_management(outZips3, "Check_ew_area", expression16, "PYTHON_9.3", "")

        expression17 = "(!Count_eastwest10!-!Count_south10!)"
        arcpy.CalculateField_management(outZips3, "Check_10_count", expression17, "PYTHON_9.3", "")

        expression18 = "(!Flatarea_eastwest10!-!Flatarea_south10!)"
        arcpy.CalculateField_management(outZips3, "Check_10_area", expression18, "PYTHON_9.3", "")
        

        Del1 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combs")
        Del2 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combs10")
        Del3 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combew")
        Del4 = (str(outfolderPath1)+"/Fsummary.gdb/zip_combew10")
        Del5 = (str(outfolderPath1)+"/Fsummary.gdb/zips_bldg")
        Del6 = (str(outfolderPath1)+"/Zips")
        featurelist = [Del1,Del2,Del3,Del4,Del5,Del6]        
        for feature in featurelist:
                arcpy.Delete_management(feature, "")
      
        print "Final Summary feature classes created successfully"

        arcpy.env.workspace = (str(outfolderPath1))   
        outfolderPath1 = (str(outfolderPath1))
        outZips3 = (str(outfolderPath1)+"/Fsummary.gdb/zip_summary")
        fc = str(outZips3)
        rows = arcpy.SearchCursor(fc)
        CSVFile = (str(outfolderPath1)+"/"+str(folderName1)+"_"+str(stateq2)+".csv")
        fields = [f.name for f in arcpy.ListFields(fc) if f.type <> "Geometry" and f.name.lower() not in ['objectid','shape','shape_length','shape_area']]
#        for i,f in enumerate(fields):
#            if f == 'OBJECTID' or f == 'Shape' or f == 'Shape_Length' or f == 'Shape_Area':
#                del fields[i]
        with open(CSVFile, 'w') as f:
            f.write(','.join(fields)+'\n') #csv headers
            with arcpy.da.SearchCursor(fc, fields) as cursor:
                for row in cursor:
                    f.write(','.join([str(r) for r in row])+'\n')
        print "Final sunmmary feature class exported as CSV file for the city of:"+str(folderName1)
        print "now updating the Altitude feature class"
        qryInTab2  =  '"City_1"'+" ='"+str(cityq2)+"'"
        print qryInTab2
 
       # qryInTab  =  '"'+str(cityq2)+ '" AND "'+str(year2)+  '" AND "' +str(stateq2)+'"'
        qryInTab  =  str(qry2)+ ' AND '+str(qry3)+  ' AND ' +str(qry4)   
        #print qryInTab
        lyrInTab1 = arcpy.MakeFeatureLayer_management(inTable,"lyrInTab")
        inTableA = arcpy.SelectLayerByAttribute_management(lyrInTab1,"NEW_SELECTION",qryInTab)
        rows = arcpy.UpdateCursor(inTableA)
        for row in rows:
                row.setValue("Analyzed",'Y')
                rows.updateRow(row)
        print "Analyzed field in Altitude feature class updated for the city of: "+str(folderName1)
#...........................................



except Exception as e:
    print e.message
    arcpy.AddError(e.message)

##        fieldnames = ['ZIP','Region','ZIP_NAME','COUNTY','STATE','area_zip_meters','Area_intersect',\
##                      'zip_pct','Count_total_builidngs','Area_total_buildings','Count_south',\
##                      'Flatarea_south',	'Count_eastwest','Flatarea_eastwest','Count_south10','Flatarea_south10',\
##                      'Count_eastwest10','Flatarea_eastwest10','Pct_Count_south','Pct_Flatarea_south',\
##                      'Pct_Count_eastwest','Pct_Flatarea_eastwest','Pct_Count_south10','Pct_Flatarea_south10',\
##                      'Pct_Count_eastwest10','Pct_Flatarea_eastwest10','Check_south_count','Check_south_area',\
##                      'Check_ew_count','Check_ew_area','Check_s10_count','Check_s10_area','Check_ew10_count',\
##                      'Check_ew10_area','Check_10_count','Check_10_area']
