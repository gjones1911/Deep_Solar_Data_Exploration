import data_display as dd
import numpy as np
import pandas as pd
import statsmodels as sm
from Deep_Solar_aid import *
from GJ_Utils.util import show_list
pd.options.mode.use_inf_as_na = True

path = r'K:\TVA_SVI'
SVI_south = r'\SVI_tva.xlsx'
TVA_path = path + '\South_DS_SVI_merged.xlsx'
excel = r'K:\TVA_SVI\TN_DS_SVI_merged.xlsx'
TNDS = pd.read_excel(TVA_path, index='fips')

DEM = TNDS.loc[TNDS[political.dem16] > .5]
DEM.replace(-999, np.NaN)
DEM.dropna()
print('Therea are {:d} majority {:s} voting census tracts'.format(DEM.shape[0], 'DEM'))
dem_edu = DEM[education.edu_yrs].mean()
dem_avg = DEM[income.avg_inc].mean()
dem_med = DEM[income.med_inc].mean()
dem_pc = DEM[income.pc_inc].mean()
dem_svi_inc = DEM[linear_Model_attribs.SVIdemo.SVI_income_st[0]].mean()
dem_PVres_m = DEM[pv_attribs.PV_res].mean()
dem_PVres_tot = DEM[pv_attribs.PV_res].sum()
dem_PVarea_m = DEM[pv_attribs.PV_area_res].mean()
dem_PVarea_tot = DEM[pv_attribs.PV_area_res].sum()
dem_PVapHa_m = DEM[pv_attribs.PVarea_by_Harea].mean()
dem_PVapHa_tot = DEM[pv_attribs.PVarea_by_Harea].sum()
dem_PVpH_m = DEM[pv_attribs.PV_per_house].mean()
dem_PVpH_tot = DEM[pv_attribs.PV_per_house].sum()

GOP = TNDS.loc[TNDS[political.gop16] > .5]
GOP.replace(-999, np.NaN)
GOP.dropna()
print('Therea are {:d} majority {:s} voting census tracts'.format(GOP.shape[0], 'GOP'))
gop_edu = GOP[education.edu_yrs].mean()
gop_avg = GOP[income.avg_inc].mean()
gop_med = GOP[income.med_inc].mean()
gop_pc = GOP[income.pc_inc].mean()
gop_svi_inc = GOP[linear_Model_attribs.SVIdemo.SVI_income_st[0]].mean()
gop_PVres_m = GOP[pv_attribs.PV_res].mean()
gop_PVres_tot = GOP[pv_attribs.PV_res].sum()
gop_PVarea_m = GOP[pv_attribs.PV_area_res].mean()
gop_PVarea_tot = GOP[pv_attribs.PV_area_res].sum()
gop_PVapHa_m = GOP[pv_attribs.PVarea_by_Harea].mean()
gop_PVapHa_tot = GOP[pv_attribs.PVarea_by_Harea].sum()
gop_PVpH_m = GOP[pv_attribs.PV_per_house].mean()
gop_PVpH_tot = GOP[pv_attribs.PV_per_house].sum()

print('Income for GOP vs. DEM voting census tracts for 2016 election:')
print('{:s} avg: {:.3f}, median: {:.3f}, pc: {:.3f}, svi: {:.3f} incomes'.format('DEM', dem_avg, dem_med, dem_pc, dem_svi_inc) )
print('{:s} avg: {:.3f}, median: {:.3f}, pc: {:.3f}, svi: {:.3f} incomes'.format('GOP', gop_avg, gop_med, gop_pc, gop_svi_inc) )
print('Education GOP vs. DEM')
print('{:s} avg: {:.3f}'.format('DEM', dem_edu) )
print('{:s} avg: {:.3f}'.format('GOP', gop_edu) )
print('Residential Solar:')
print('PV count: {:s} avg: {:.3f}, total: {:d}, PV residential stats'.format('DEM', dem_PVres_m, dem_PVres_tot) )
print('PV count: {:s} avg: {:.3f}, total: {:d}, PV residential stats'.format('GOP', gop_PVres_m, gop_PVres_tot) )
print('PV area: {:s} avg: {:.3f}, total: {:.3f}, PV residential stats'.format('DEM', dem_PVarea_m, dem_PVarea_tot) )
print('PV area: {:s} avg: {:.3f}, total: {:.3f}, PV residential stats'.format('GOP', gop_PVarea_m, gop_PVarea_tot) )
print('PV area per home ft^2: {:s} avg: {:.3f}, total: {:.3f}, PV residential stats'.format('DEM', dem_PVapHa_m, dem_PVapHa_tot) )
print('PV area per home ft^2: {:s} avg: {:.3f}, total: {:.3f}, PV residential stats'.format('GOP', gop_PVapHa_m, gop_PVapHa_tot) )
print('PV per home: {:s} avg: {:.3f}, total: {:.3f}, PV residential stats'.format('DEM', dem_PVpH_m, dem_PVpH_tot) )
print('PV per home: {:s} avg: {:.3f}, total: {:.3f}, PV residential stats'.format('GOP', gop_PVpH_m, gop_PVpH_tot) )


