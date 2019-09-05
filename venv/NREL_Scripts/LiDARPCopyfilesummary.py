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
        print
        print "*********************:  Copying for Final Summarization    :*********************"
        print

# Step 1: Creation of folders and sub folders
#       Crearion of Folder "FinalSummary"
        outfolderPath1 = str(dPath)#+str(cityq)
        folderName1    = "FinalSummary"
        arcpy.CreateFolder_management(outfolderPath1,folderName1) # creates folder by the name of FinalSummary
        #print "Folder created:"+str(dPath)+"/FinalSummary"
# Step 2: Creation of sub folders
# Query by city name
        FPath = "C:/LiDAR/FinalSummary/"
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


        
#Step 5: Copy all the required files from the summary.gdb to the new gedatabases (the one just created).
        FPath2 = (str(dPath)+str(cityq)+"/summary/summary.gdb/")
        inFC1  = (str(FPath2)+"zip_combew")       
        inFC2  = (str(FPath2)+"zip_combew10")         
        inFC3  = (str(FPath2)+"zip_combs")      
        inFC4  = (str(FPath2)+"zip_combs10")
        inFC5  = (str(FPath2)+"zips_bldg")
        FPath6 = (str(FPath5)+str(cityq)+".gdb/")
        #print "Database Folder:"+str(FPath6)
        outFC1 = (str(FPath6)+"zip_combew1")       
        outFC2 = (str(FPath6)+"zip_combew101")         
        outFC3 = (str(FPath6)+"zip_combs1")      
        outFC4 = (str(FPath6)+"zip_combs101")
        outFC5 = (str(FPath6)+"zips_bldg")
#
        inFC   = [inFC1,inFC2,inFC3,inFC4,inFC5]
        outFC   = [outFC1,outFC2,outFC3,outFC4,outFC5]
        for FC1,FC2 in zip (inFC,outFC):
            arcpy.Copy_management(FC1, FC2)#,{data_type})




#..............................................................................................................






        print "Features classes copied successfully for Final Summary"# to Folder."+str(FPath6)
        print

        #print "Please, run the 'LiDarPDelete' script ."



except Exception as e:
    print e.message
    arcpy.AddError(e.message)

 
