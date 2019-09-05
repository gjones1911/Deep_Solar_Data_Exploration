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
TVA_path = path + '\South_DS_SVI_merged.xlsx'

w_tva = pd.read_excel(TVA_path)

print(set(w_tva.columns.values))
print(set(w_tva['STATE'].values))
