import data_display as dd
import numpy as np
import sklearn
from sklearn.decomposition import FactorAnalysis
import pandas as pd
import statsmodels as sm
from Deep_Solar_aid import *
from GJ_Utils.util import show_list


#destination = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output'
#destination = r'C:\Users\Candice\Documents\ArcGIS\Projects\TVA_vs_THERest\_excel'
destination =r'C:\Users\Candice\Documents\ArcGIS\Projects\TVA_vs_THERest\_excel\DEMO_DS'
destination = output_storage
#destination = output

excel = DeepSolar_orig

#usecols = basic_data_set_safe
#usecols = pv_attribs.PV_attribs_res + demographics + ['state']
usecols = almost_full_set

print('Number of Attributes :\n', len(usecols))
print('Attributes :')
#show_list(usecols)

brain = {}


'''
# look at some names I have a changed
for en in usecols:
    if en[:10] not in brain:
        brain[en[:10]] = 1
        print("{:s}  =   {:s}".format(en, en[:10]))
    else:
        str = en[:8] + "_{:d}".format(brain[en[:10]])
        print("{:s}  =  {:s}".format(en, str))
        brain[en[:10]] += 1
print()
'''

state = input('What State would you like to analyze, Note: enter state\'s abbreviation (i.e TN): ' ).lower().strip()
fillna = input('Would you like to fill the na\'s with 0s (y/n):')
select_cols = input('Would you like to use a select set of columns (y/n)')
if select_cols.lower() == 'y':
    select_cols = True
else:
    select_cols = False

if state == '':
    state = 'US'.lower()

folder = r'\{:s}'.format(state.upper())
path = destination + folder

dsexcel = 'Deep_Solar.xlsx'

statep = r'\{:s}'.format('') + state.upper()
print(statep)

file_all = statep + dsexcel
file_adopters = statep + '_' + 'adopt' + '_' + dsexcel
file_nonadopters = statep + '_' + 'nonadopt' + '_' + dsexcel


def check_fip(df):
    fips = df['fips'].tolist()
    length = len("{:d}".format((fips[0])))
    print('the length of a fip:{:d}, {:s}'.format(length, "{:d}".format(fips[0])))
    for fip in range(len(fips)):
            if len(fips[fip]) == 10:
                fips[fip] = ('0'+ "{:s}".format(str(fips[fip])))
            else:
                fips[fip] = str(fips[fip])
    return fips



if state.lower() == 'us':
    print('Gathering {:s} deep solar data'.format(state.upper()))
    if fillna.lower()[0] == 'y':
        DS = pd.read_excel(excel).fillna(0)
    else:
        DS = pd.read_excel(excel)

    DS['avg_house_area'] = DS[housing.house_val].values/121
    DS[PVaByHa] = DS[pv_attribs.PV_area_res].values/DS['avg_house_area']

    DSPVresadopt = DS.loc[DS[pv_attribs.PV_res] > 0]
    DSPVresnonadopt = DS.loc[DS[pv_attribs.PV_res] == 0]

    # right to files
    DS.to_excel(path + file_all, index=False)
    DSPVresadopt.to_excel(path + file_adopters, index=false)
    DSPVresnonadopt.to_excel(path + file_nonadopters, index=false)
else:
    print('Gathering {:s} deep solar data'.format(state.upper()))
    print('writing to path {:s}'.format(path))
    if fillna.lower()[0] == 'y':
        if select_cols:
            DS = pd.read_excel(excel, usecols=usecols).fillna(0)
        else:
            DS = pd.read_excel(excel).fillna(0)
    else:
        if select_cols:
            DS = pd.read_excel(excel, usecols=usecols)
            #l = DS['fips'].tolist()
            #ss = "{:d}".format(l[0])
            #print("stuff: \n", l, '\n', len(ss))
            #quit()
        else:
            DS = pd.read_excel(excel)
    DS = DS.loc[DS['state'] == state.lower()]


    ll = check_fip(DS)
    if len(ll) > 0:
        DS['fips'] = ll
    #quit()
    # add my variables
    DS['avg_house_area'] = DS[housing.house_val].values/121
    DS['PVaByHa'] = DS[pv_attribs.PV_area_res].values/DS['avg_house_area']

    print('Thera are {:d} {:s} ct\'s'.format(DS.shape[0], state))
    DSPVresadopt = DS.loc[DS[pv_attribs.PV_res] > 0]
    print('Thera are {:d} {:s} ct that are PV adopters\'s'.format(DSPVresadopt.shape[0], state))
    DSPVresnonadopt = DS.loc[DS[pv_attribs.PV_res] == 0]
    print('Thera are {:d} {:s} ct that are non PV adopters\'s'.format(DSPVresnonadopt.shape[0], state))
    print('Creating Excel files {:s}, {:s}, and {:s}'.format(file_all, file_adopters, file_nonadopters))
    DS.to_excel(path + file_all, index=False)
    DSPVresadopt.to_excel(path  + file_adopters, index=False)
    DSPVresnonadopt.to_excel(path + file_nonadopters, index=False)
