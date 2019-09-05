from GJ_Utils.Data_Explorer.Data_Explorer import *
from GJ_Utils.util import *
from Deep_Solar_aid import *
import matplotlib.pyplot as plt

deTN = Data_Explorer(DeepSolarTN_excel)
deUS = Data_Explorer(DeepSolar_excel)

Adopters = deUS.grab_sub_set(PV_res, 'g', 0)
adoptersPct = Adopters.shape[0]/(deUS.df.shape[0])
adpavg = Adopters[PV_res].mean()
adphtot = Adopters[PV_res].sum()
display_basic_data(Adopters, deUS.df.shape[0], PV_res, 'PV adopters')

high = deUS.grab_sub_set(PV_res, 'g', 9)
highPct = high.shape[0]/(deUS.df.shape[0])
havg = high[PV_res].mean()
htot = high[PV_res].sum()
display_basic_data(high, deUS.df.shape[0], PV_res, 'High adoption')

moderate = deUS.grab_sub_set([PV_res,PV_res], 'cmpm&', [9, 1])
modPct = moderate.shape[0]/deUS.N
mavg = moderate[PV_res].mean()
mtot = moderate[PV_res].sum()
display_basic_data(moderate, deUS.df.shape[0], PV_res, 'Moderate adoption')


non = deUS.grab_sub_set(PV_res, 'l', 1)
nonPct = non.shape[0]/deUS.df.shape[0]
navg = non[PV_res].mean()
ntot = non[PV_res].sum()
display_basic_data(non, deUS.df.shape[0], PV_res, 'Non-adoption')

type_list = ['PV', 'Income', 'Housing', 'Solar', 'Poverty']

attribs = create_attrib_que(type_list)

print(attribs)

print('US averages')
deUS.display_stat(deUS.average, attribs)
print()
print('PV adopters')
deUS.display_stranger_stat(Adopters, deUS.average, attribs, thresh=None)
print()
print('High adoption states')
deUS.display_stranger_stat(high, deUS.average, attribs, thresh=None)
print()
print('Moderate adoption states')
deUS.display_stranger_stat(moderate, deUS.average, attribs, thresh=None)
print()
print('Non-adoption states')
deUS.display_stranger_stat(non, deUS.average, attribs, thresh=None)
print()
print('U.S. averages')
