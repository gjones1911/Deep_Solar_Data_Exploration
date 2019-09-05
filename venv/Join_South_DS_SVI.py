#import data_display as dd
#import numpy as np
#import sklearn
#from sklearn.decomposition import FactorAnalysis
import pandas as pd
#import statsmodels as sm
from Deep_Solar_aid import *
#m,from  GJ_Utils.util import show_list

path = r'K:\TVA_SVI'
SVI_south = r'\SVI_tva.xlsx'
DSset = DeepSolar_orig
#TVASVI = path + r'\SVI_tva.xlsx'
#TVASVI = r'K:\TVA_SVI\Tennessee.xlsx'
#TVADS = r'K:\DEEP_SOLAR_BIG2\TVA_DS.xlsx'

#TVADS = r'K:\DEEP_SOLAR_BIG2\TN\TNDeep_Solar.xlsx'

#TVADSdf = pd.read_excel(TVADS)
#TVASVIdf = pd.read_excel(TVASVI)
DSdf = pd.read_excel(DSset)
SVIdf = pd.read_excel(path + SVI_south)


merge = DSdf.merge(SVIdf, left_on='fips', right_on='FIPS')

state_home_sqft = {'tn':136,
                   'al':103,
                   'ga':121,
                   'ky':119,
                   'ms':96,
                   'nc':135,
                   'va':163}

dls = []

for st in merge['state'].values:

    if st in state_home_sqft:
        dls.append(state_home_sqft[st])


dls = np.array(dls, dtype=np.float64)


# recode neede stuff
# make a new var for PV area per house area
merge['avg_house_area'] = merge[housing.house_val].values / dls
merge['PVaByHa'] = merge[pv_attribs.PV_area_res].values / merge['avg_house_area']

#recode for adoption or non adoption
# recode continous variables into ordinal
merge = recode_adoption(merge)            # binary recode 0==pv = 0, 0<PV = 1
merge = recode_diversity(merge)           # recodes into white or not white

attribs = age.Age_attribs_to_code
labels = ['age_more_than_rate']
splitter='_'

# recode age vars
merge = Xiaojing_range_coder(merge, attribs, labels, splitter, verbose=False)

merge.to_excel(path + '\South_DS_SVI_merged.xlsx')