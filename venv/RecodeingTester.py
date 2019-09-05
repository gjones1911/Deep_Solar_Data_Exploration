import data_display as dd
import numpy as np
import sklearn
from sklearn.decomposition import FactorAnalysis
import pandas as pd
import statsmodels as sm
from Deep_Solar_aid import *
from GJ_Utils.util import show_list

excel = TNDS_BIG

df = pd.read_excel(excel)

cols = age.Age_attribs[1:]
#new_names = [x.strip('age_rate') + '_RC' for x in cols ]
#show_list(new_names)

#recode_by_order(df, cols, new_names).to_excel(output_storage + r'\TNtester.xlsx', index=False)


attribs = age.Age_attribs_to_code
pop_label = population.pop
labels = list(['age_more_than_rate']*len(attribs))
labels = ['age_more_than_rate']
splitter='_'
#print(labels)
#for at in attribs:
#    print(strip_label(at, labels, verbose=False))

#print(calculate_mean_array(attribs, labels, splitter, verbose=False))


Xiaojing_range_coder(df, attribs, labels, splitter, verbose=False)