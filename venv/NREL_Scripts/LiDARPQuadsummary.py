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
        #inTablez = r"C:/LiDAR/Base_map/LDR.gdb/Azimuth"

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
                #print "The Part of City being analyzed:" +str(qry1)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Step 1: Creation of folders and sub folders
#       Crearion of Folder "FinalSummary"
        outfolderPath1 = str(dPath)#+str(cityq)
        folderName1    = "QuadSummary"
        arcpy.CreateFolder_management(outfolderPath1,folderName1) # creates folder by the name of FinalSummary
        #print "Folder created:"+str(dPath)+"/FinalSummary"
# Step 2: Creation of sub folders
# Query by city name
        FPath = "C:/LiDAR/QuadSummary/"
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
# Query for the state name
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
                #print "Name of the State of the City being analyzed:" +str(qry3)
# Create a sub folder by City name and State (CityName_State) with in FinalSummary Folder. 
        folderName3    = str(cityq2)+'_'+str(stateq2)
        outfolderPath3 = str(FPath)
        arcpy.CreateFolder_management(outfolderPath3,folderName3) 
#Step 4: Creation of Folder by City Name and Year
# Query by year
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
# Create a sub folder by City name and year (CityName_Year) with in CityName_State        
        folderName4    = str(cityq2)+'_'+str(year2)
        FPath4      = str(FPath)+str(folderName3)
        #print "Sub_Folder 1:"+str(FPath4)
        outfolderPath4 = str(FPath4)
        # c:/LiDAR/FinalSummary/CityName_State
        arcpy.CreateFolder_management(outfolderPath4,folderName4) 




#Step 4: Creation of a geodatabase by name of city section.
        FPath5 = (str(outfolderPath4)+"/"+str(folderName4)+"/")
        #print "Sub_Folder 2:"+str(FPath5)
        outName1   =  str(cityq)
        arcpy.CreateFileGDB_management(FPath5, outName1)
        print FPath5




# Quad SUMMARY *****************************************************************************
        print
        print "*********************:  Quad Summary    :*********************"
        print
#Step 5: Creation of a geodatabase by name of city quad summary.
        QPath7 = (str(FPath5))
        #print FPath5
        #print QPath7       
        arcpy.CreateFileGDB_management(QPath7, outName1)
#Step 6: Copy all the required files from the summary.gdb to the new gedatabases (the one just created).
        FPath2 = (str(dPath)+str(cityq)+"/summary/summary.gdb/")
        inFC1  = (str(FPath2)+"zip_combew")       
        inFC2  = (str(FPath2)+"zip_combew10")         
        inFC3  = (str(FPath2)+"zip_combs")      
        inFC4  = (str(FPath2)+"zip_combs10")
        inFC5  = (str(FPath2)+"zips_bldg")
        QPath8 = (str(QPath7)+str(cityq)+".gdb/")
        #print "Database Folder:"+str(QPath8)
        outFC1 = (str(QPath8)+"zip_combew1")       
        outFC2 = (str(QPath8)+"zip_combew101")         
        outFC3 = (str(QPath8)+"zip_combs1")      
        outFC4 = (str(QPath8)+"zip_combs101")
        outFC5 = (str(QPath8)+"zips_bldg")
#
        inFC   = [inFC1,inFC2,inFC3,inFC4,inFC5]
        outFC   = [outFC1,outFC2,outFC3,outFC4,outFC5]
        for FC1,FC2 in zip (inFC,outFC):
            arcpy.Copy_management(FC1, FC2)#,{data_type})
#.............................................1
        inZips1 = (str(QPath8)+"zip_combs1")
        outFC2 = (str(QPath8)+"zip_combs")
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



#.............................................2
        inZips1 = (str(QPath8)+"zip_combew1")
        outFC2 = (str(QPath8)+"zip_combew")

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


#.............................................3
        inZips1 = (str(QPath8)+"zip_combs101")
        outFC2 = (str(QPath8)+"zip_combs10")
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

#.............................................4
        inZips1 = (str(QPath8)+"zip_combew101")
        outFC2 = (str(QPath8)+"zip_combew10")

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

#........................
        
        inZips1 = (str(QPath8)+"zips_bldg") #################
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
        outZips2 = (str(QPath8)+"zip_summary2")
        #print "Output name:"+str(outZips2)
        arcpy.env.workspace = (str(QPath8))
        fc = ["zips_bldg","zip_combs","zip_combew","zip_combs10","zip_combew10"]
        arcpy.Intersect_analysis(fc, outZips2, "NO_FID", "", "INPUT") 
# create new layer of selected records to delete the fields with Null values
        outZips3 = (str(QPath8)+"zip_summary")
        inTablezs2 = (str(QPath8)+"zip_summary2")
        qry = '"Count_south" > 0'                   ## Changed for second round
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

        #print "Final Summary feature classes created successfully"

        arcpy.env.workspace = (str(QPath7))   
        outfolderPath1 = (str(QPath7))
        outZips3 = (str(QPath8)+"zip_summary")
        fc = str(outZips3)
        rows = arcpy.SearchCursor(fc)
        CSVFile = (str(QPath7)+"/"+str(cityq)+".csv")
        fields = [f.name for f in arcpy.ListFields(fc) if f.type <> "Geometry" and f.name.lower() not in ['objectid','shape','shape_length','shape_area']]
        with open(CSVFile, 'w') as f:
            f.write(','.join(fields)+'\n') #csv headers
            with arcpy.da.SearchCursor(fc, fields) as cursor:
                for row in cursor:
                    f.write(','.join([str(r) for r in row])+'\n')
        print "Quad sunmmary feature class exported as CSV file"# for the city of:"+str(folderName1)


        Del1 = (str(QPath8)+"zip_combs1")
        Del2 = (str(QPath8)+"zip_combs101")
        Del3 = (str(QPath8)+"zip_combew1")
        Del4 = (str(QPath8)+"zip_combew101")
  
    
        featurelist = [Del1,Del2,Del3,Del4]        
        for feature in featurelist:
                arcpy.Delete_management(feature, "")



#..............................................................................................................






        #print "Features classes copied successfully for Quad Summary to Folder."+str(QPath8)
        print
        print"******************************************************************"
        print"*                  CONGRATULATIONS                               *"
        print"******************************************************************"
        print
        print "Please, run the 'LiDarPDelete' script ."



except Exception as e:
    print e.message
    arcpy.AddError(e.message)

 
