import arcpy
import os.path
from arcpy import env
from arcpy import da
from arcpy.sa import *
import time
# Set environment settings
arcpy.env.overwriteOutput = True
#arcpy.env.workspace  = "C:/LiDAR/Reflective_surface"
# Set Snap Raster environment
#arcpy.env.snapRaster = "C:/LiDAR/reflective_surface/refsurf"
#inRaster             = "C:/LiDAR/reflective_surface/refsurf"                              #LiDAR Raster
# Check out the ArcGIS Spatial Analyst extension license
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
                print "The City being analyzed:" +str(qry1)


        print
        print "*********************:  Deleting Extra Layers    :*********************"
        print
        arcpy.env.workspace  = (str(dPath)+str(cityq))

        Del1  = (str(dPath)+str(cityq)+"/Slope/"+str("slpbldg"))
        Del2  = (str(dPath)+str(cityq)+"/Slope/"+str("slpfmean"))
        Del3  = (str(dPath)+str(cityq)+"/Slope/"+str("slpfmean2"))
        Del4  = (str(dPath)+str(cityq)+"/Aspect/"+str("aspbldg"))
        Del5  = (str(dPath)+str(cityq)+"/Aspect/"+str("aspflat"))
        Del6  = (str(dPath)+str(cityq)+"/Aspect/"+str("aspvar"))
        Del7  = (str(dPath)+str(cityq)+"/Aspect/"+str("aspvarext"))
        Del8  = (str(dPath)+str(cityq)+"/Aspect/"+str("aspflatmk"))
        Del9  = (str(dPath)+str(cityq)+"/Aspect/"+str("aspmaj"))
        Del10  = (str(dPath)+str(cityq)+"/Aspect/"+str("aspid"))
        Del11 = (str(dPath)+str(cityq)+"/Aspect/"+str("aspcomb"))
        Del12 = (str(dPath)+str(cityq)+"/Combine/"+str("slpzmean"))
        Del13 = (str(dPath)+str(cityq)+"/Combine/"+str("combs"))
        Del14 = (str(dPath)+str(cityq)+"/Combine/"+str("combew"))
        Del15 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_poly")
        Del16 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_poly")
        Del17 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_poly2")
        Del18 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_poly2")
        Del19 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_slppoly")
        Del20 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_slppoly")
        #Del21 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_slpclip")
        #Del22 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_slpclip")
        Del23 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combs_slpclip10")
        Del24 = (str(dPath)+str(cityq)+"/Combine/combine.gdb/combew_slpclip10")
        Del25 = (str(dPath)+str(cityq)+"/Combine/combs_poly.shp")
        featurelist = [Del1,Del2,Del3,Del4,Del5,Del6,Del7,Del8,Del9,Del10,Del11,Del12,Del13,Del14,Del15,Del16,Del17,Del18,Del19,Del20,Del23,Del24,Del25]        
        for feature in featurelist:
                arcpy.Delete_management(feature, "")       
#........................................................................................................

        print "23 Unnecessary files deleted for the city of: "+str(cityq)


except Exception as e:
    print e.message
    arcpy.AddError(e.message)

