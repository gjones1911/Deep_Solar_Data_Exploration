import data_display as dd
import numpy as np
#import sklearn
#from sklearn.decomposition import FactorAnalysis
import pandas as pd
#import statsmodels as sm
from Deep_Solar_aid import *
from  GJ_Utils.util import show_list

path = r'K:\TVA_SVI'

AL = r'\Alabama.csv'
TN = r'\Tennessee.csv'
GA = r'\Georgia.csv'
KY = r'\Kentucky.csv'
MS = r'\Mississippi.csv'
NC = r'\NorthCarolina.csv'
VA = r'\Virginia.csv'


ALdf = pd.read_csv(path+AL)
GAdf = pd.read_csv(path+GA)
KYdf = pd.read_csv(path+KY)
MSdf = pd.read_csv(path+MS)
NCdf = pd.read_csv(path+NC)
TNdf = pd.read_csv(path+TN)
VAdf = pd.read_csv(path+VA)


to_join = [ALdf, GAdf, KYdf, MSdf, NCdf, TNdf, VAdf]

pd.concat(to_join).to_excel(path+'\SVI_tva.xlsx')