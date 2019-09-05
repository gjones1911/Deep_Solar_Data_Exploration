import data_display as dd
import numpy as np
#import sklearn
#from sklearn.decomposition import FactorAnalysis
import pandas as pd
#import statsmodels as sm
from Deep_Solar_aid import *
from  GJ_Utils.util import show_list


print('hi')

DSf = pd.read_excel(DeepSolar_orig)

TVA = pd.read_excel(TVA_service_excel)

tograb = TVA['fips'].values

show_list(tograb)
quit()

DSf.loc[DSf['fips'].isin(tograb)].to_excel(output_storage3 + '\TVA_DS.xlsx', index=False)



