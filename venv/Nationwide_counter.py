import data_display as dd
import numpy as np
import pandas as pd
import statsmodels as sm
import matplotlib.pyplot as plt
import sklearn
from sklearn.decomposition import FactorAnalysis
from sklearn.decomposition import PCA
import scipy.stats
import scipy.optimize
import scipy.spatial
from Deep_Solar_aid import *
from GJ_Utils.util import show_list
pd.options.mode.use_inf_as_na = True


excel = DeepSolar_orig

US = pd.read_excel(excel).loc[:, pv_attribs.PV_attribs_res[:2]+["state"]]

states = set(US['state'].values)
states = list(states)

show_list(states)

sl = []
pvcntr = []
pvareares = []



for state in states:
    df = US.loc[US['state'] == state]
    count = df.shape[0]
    adopt = df.loc[df[pv_attribs.PV_res] > 0].shape[0]
    nonadopt = df.loc[df[pv_attribs.PV_res] == 0].shape[0]
    sl.append(state)
    pvcntr.append(df[pv_attribs.PV_attribs_res[0]].sum())
    pvareares.append(df[pv_attribs.PV_attribs_res[1]].sum())
    print("\t\t\t\t\t**************{:s}************".format(state))
    print('Total residential PV installations: {:f}'.format(pvcntr[-1]))
    print('Total area m^2 residential PV installations: {:f}'.format(pvareares[-1]))
    print('The {:s} has a census tract adoption percentage of {:.2f}%'.format(state, adopt/count))


pd.DataFrame({"":sl, "# PV residential":pvcntr, "Total PV area":pvareares}).to_excel("NationWidePVCounts.xlsx")