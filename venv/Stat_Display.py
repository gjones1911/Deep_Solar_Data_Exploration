from GJ_Utils.Data_Explorer.Data_Explorer import *
from GJ_Utils.util import *
from Deep_Solar_aid import *
import matplotlib.pyplot as plt

deTN = Data_Explorer(DeepSolarTN_excel)
#deUS = Data_Explorer(DeepSolar_excel)

Adopters = deTN.grab_sub_set(PV_res, 'g', 0)
adoptersPct = Adopters.shape[0]/(deTN.df.shape[0])
adpavg = Adopters[PV_res].mean()
adptot = Adopters[PV_res].sum()
display_basic_data(Adopters, deTN.df.shape[0], PV_res, 'PV')

adp_d = {}
adp_d[PV_res] = {}
adp_d[PV_res][deTN.average] = adpavg
adp_d[PV_res][deTN.dsum] = adptot


high = deTN.grab_sub_set(PV_res, 'g', 9)
highPct = high.shape[0]/(deTN.df.shape[0])
havg = high[PV_res].mean()
htot = high[PV_res].sum()
display_basic_data(high, deTN.df.shape[0], PV_res, 'High adoption')

moderate = deTN.grab_sub_set([PV_res,PV_res], 'cmpm&', [9, 1])
modPct = moderate.shape[0]/deTN.N
mavg = moderate[PV_res].mean()
mtot = moderate[PV_res].sum()
display_basic_data(moderate, deTN.df.shape[0], PV_res, 'Moderate adoption')


non = deTN.grab_sub_set(PV_res, 'l', 1)
nonPct = non.shape[0]/deTN.df.shape[0]
navg = non[PV_res].mean()
ntot = non[PV_res].sum()
display_basic_data(non, deTN.df.shape[0], PV_res, 'Non-adoption')

type_list = ['PV', 'Income', 'Housing', 'Solar', 'Poverty']

attribs = create_attrib_que(type_list)

print(attribs)

print('TN averages')
deTN.display_stat(deTN.average, attribs)
print()
print('PV adopters')
deTN.display_stranger_stat(Adopters, deTN.average, attribs, thresh=None)
print()
print('High adoption states')
deTN.display_stranger_stat(high, deTN.average, attribs, thresh=None)
print()
print('Moderate adoption states')
deTN.display_stranger_stat(moderate, deTN.average, attribs, thresh=None)
print()
print('Non-adoption states')
deTN.display_stranger_stat(non, deTN.average, attribs, thresh=None)
print()
print('U.S. averages')
