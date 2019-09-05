import data_display as dd
import numpy as np
import sklearn
from sklearn.decomposition import FactorAnalysis
import pandas as pd
import statsmodels as sm
from Deep_Solar_aid import *
from GJ_Utils.util import show_list

destination = output_storage3

states = ['tn', 'al', 'ky', 'ms', 'ga', 'va', 'nc']
#states = ['']
#folder = r'\{:s}'.format(states[0].upper())

excel = DeepSolar_orig

for state in states:
    path = destination + r'\{:s}'.format(state.upper())
    Deep_Solar_slice(path, excel, state, select_cols='n', fillna='n', rename=False, verbose=False, Interactive=False)