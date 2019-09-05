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

#excelfile = input("Give me the absolute path to the file you would like to analyze: ")
#excelfile = TNDeepSolar_excel
excelfile = TNDS_BIG
#state = input('Would you like to analyze the entire US or a particular state Note:\n'
#              '                                                             For US: just press enter or enter US\n'
#              '                                                             For a particular state: enter the abreviation of the state, i.e. tn: ')

state = 'tn'
state = state.lower()


print('Opening data file.....')

#DS = pd.read_excel(excelfile).fillna(0)
DS = pd.read_excel(excelfile).dropna(axis=0)
#DS = pd.read_excel(excelfile)

if state == '':
    state = 'us'

if state != 'us':
    DS = DS.loc[DS['state'] == state]

DS_Adopters = DS.loc[DS[pv_attribs.PV_res] > 0]
DS_Nonadopters = DS.loc[DS[pv_attribs.PV_res] == 0]

def display_cor_dict(rd):
    tau_score = ''
    pscore = ""
    for pval in rd:
        print("PV attribute: {:s}".format(pval))
        print()
        for attrib in rd[pval]:
            tau = rd[pval][attrib]['tau']
            p = rd[pval][attrib]['pval']
            print('\t\t\t\tAttribute: {:s}'.format(attrib))
            if abs(tau) > .230:
                tau_score = '**'
            elif abs(tau) > .30:
                tau_score = '***'
            else:
                tau_score = ''
            if p < .001:
                pscore = '***'
            elif p < .05:
                pscore = "**"
            else:
                pscore = ""
            print('\t\t\t\t\t\t\t\t\ttau: {:.3f}{:s}'.format(tau, tau_score))
            print('\t\t\t\t\t\t\t\t\tpval: {:.3f}{:s}'.format(p, pscore))

def correlation2(df, attribs, indis, nan_policy='omit', type='pearson'):
    rl = {}
    rd = {}

    #del attribs[attribs.index('population')]
    #del attribs[attribs.index('population_density')]
#    print(dx.head())
#    print(dy.head())
    for indi in indis:
        rl[indi] = list()
        for attrib in attribs:
            rd[attrib] = {}
            #dn = df.loc[:, [attrib, indi]].loc[df[attrib].notna()]
            dn = df.loc[:, [attrib, indi]].fillna(df.loc[:, attrib].mean())
            print(dn.columns)
            if type == 'pearson':
                rd[attrib]['tau'], rd[attrib]['pval'] = scipy.stats.pearsonr(dn[attrib].values, dn[indi].values)
            elif type == 'kendalltau':
                rd[attrib]['tau'], rd[attrib]['pval'] = scipy.stats.kendalltau(dn[attrib].values, dn[indi].values, nan_policy=nan_policy)
        rl[indi] = rd

    return rl

def correlation(dx, dy, attribs, indis, nan_policy='omit', type='pearson'):
    rl = {}
    rd = {}
    print(dx.head())
    print(dy.head())
    for indi in indis:
        rl[indi] = list()
        for attrib in attribs:
            rd[attrib] = {}
            if type == 'pearson':
                rd[attrib]['tau'], rd[attrib]['pval'] = scipy.stats.pearsonr(dx[attrib].values, dy[indi].values)
            elif type == 'kendalltau':
                rd[attrib]['tau'], rd[attrib]['pval'] = scipy.stats.kendalltau(dx[attrib].values, dy[indi].values, nan_policy=nan_policy)
        rl[indi] = rd

    return rl

attribs = DSdemographicsX + ['W_o_NW'] + []
yvals = DSdemographicsY
print('Independent Variables:')
show_list(attribs)
print()
print('Dependents Variables:')
show_list(yvals)
print('columns:\n', DS.columns.values)
#adopters, high, mod, non = split_data_res_adopt_non(DS, hthr=10, midrange=[1,10], lthr=1, verbose=False)

yvals= ['A_o_NA']

#rd = correlation(DS.loc[:, attribs].fillna(0), DS.loc[:,yvals].fillna(0), attribs, yvals)
#rd = correlation(DS_Adopters.loc[:, attribs], DS_Adopters.loc[:,yvals], attribs, yvals, type='pearson')
rd = correlation2(DS, attribs, yvals, type='pearson')
#rd = correlation2(DS, attribs, yvals, type='kendalltau')
#rd = correlation(DS.loc[:, attribs].fillna(0), DS.loc[:,yvals].fillna(0), attribs, yvals)
display_cor_dict(rd)

# write it to an excel file


'''
for pval in rd:
    print("PV attribute: {:s}".format(pval))
    print()
    for attrib in rd[pval]:
        print('\t\t\t\tAttribute: {:s}'.format(attrib))
        print('\t\t\t\t\t\t\t\t\ttau: ', rd[pval][attrib]['tau'])
        print('\t\t\t\t\t\t\t\t\tpval: ', rd[pval][attrib]['pval'])
'''

