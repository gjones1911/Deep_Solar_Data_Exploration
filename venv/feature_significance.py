import data_display as dd
import numpy as np
import pandas as pd
import statsmodels as sm
from Deep_Solar_aid import *
from GJ_Utils.util import show_list
pd.options.mode.use_inf_as_na = True

interactive = False

path = r'K:\TVA_SVI'
TVA_l = 'TVA'
TVA_f = 'TVA_all_full_states'
TVA_path = path + '\South_DS_SVI_merged.xlsx'
TN_l = 'TN'

#region = TVA_l
#region = TVA_f
region = TN_l.lower()

if interactive:

    ans = input('Would you like to use the deepsolar data set or some version of it (d=deep solar/ o = other) ?: ')
    if ans.lower() == 'o':
        DeepSolar_excel = input('Give me the path to the file you would like to use: ')
    excel = DeepSolar_orig
else:
    #excel = DeepSolarTN_excel
    excel = DeepSolar_orig

if interactive:
    state = input('What State would you like to analyze, note: enter state\'s abbreviation (tn): ' ).lower().strip()
else:
    state = region

print()
print('**************************************************    Analyzing {:s}'.format(state.upper()))
print()

#excel = r'K:\DEEP_SOLAR_BIG2\TN\TNDeep_Solar.xlsx'
if region == TVA_l:
    #excel = r'K:\TVA_SVI\TVA_DS_SVI_merged.xlsx'
    excel = r'K:\TVA_SVI\TVA_DS_SVI_merged2.xlsx'
elif region == TVA_f:
    #excel = r'K:\TVA_SVI\TVA_DS_SVI_merged.xlsx'
    excel = TVA_path
else:
    excel = r'K:\TVA_SVI\TN_DS_SVI_merged.xlsx'
    #TNDS = pd.read_excel(excel, index='fips').fillna(0)
    #TNDS = pd.read_excel(excel, index='fips').dropna(axis=0)
TNDS = pd.read_excel(excel, index='fips')
#TNDS = pd.read_excel(excel, index='fips')
#TNDS = TNDS.fillna(TNDS.mean(axis=1))

if region != TVA_l and region != TVA_f:
    print('Getting region {:s}'.format(region))
    TNDS = TNDS.loc[TNDS['ST_ABBR'] == region.upper() ]



print('splitting data')
adopters, high, mod, non = split_data_res_adopt_non(TNDS, hthr=10, midrange=[1,10], lthr=1, verbose=False)
dd.display_percentages(TNDS.shape[0], adopters.shape[0], non.shape[0], high.shape[0], mod.shape[0], area=state.upper() )
#all_cols = list(TNDS.columns)

#print(len(all_cols))

'''
#print(TNDS.loc[:,Basic_data_set].values)
pv_by_total = 'PV_by_total'
TNDS.loc[:, pv_by_total] = pd.Series(TNDS[pv_attribs.PV_cnt].values / TNDS[geo.land_area].values, index=TNDS.index)
print(1)
adopters.loc[:, pv_by_total] = pd.Series(adopters[pv_attribs.PV_cnt].values / adopters[geo.land_area].values, index=adopters.index)
print(2)
high.loc[:, pv_by_total] = pd.Series(high[pv_attribs.PV_cnt].values / high[geo.land_area].values, index=high.index)
print(3)
mod.loc[:, pv_by_total] = pd.Series(mod[pv_attribs.PV_cnt].values / mod[geo.land_area].values, index=mod.index)
print(4)
non.loc[:, pv_by_total] = pd.Series(non[pv_attribs.PV_cnt].values / non[geo.land_area].values, index=non.index)
print('after assignemnts')
'''
#row = 0
#print('PV by land area\n', TNDS.loc[row, pv_by_total], TNDS.loc[row, pv_attribs.PV_cnt]/ TNDS.loc[row, geo.land_area])
#print('PV by land area\n', TNDS.columns)
'''
print()
print()
print('Average PV_cnt {:s}: {:f}'.format(state, TNDS[pv_attribs.PV_cnt].mean()))
print('Stdev PV_cnt {:s}: {:f}'.format(state, TNDS[pv_attribs.PV_cnt].std()))
print('Average PV_cnt Adopters: {:f}'.format(high[pv_attribs.PV_cnt].mean()))
print('Average PV_cnt Moderate Adopters: {:f}'.format(mod[pv_attribs.PV_cnt].mean()))
print('Average PV_cnt Non Adopters: {:f}'.format(non[pv_attribs.PV_cnt].mean()))

print()
print()
print('Average PV_area_res {:s}: {:f}'.format(state, TNDS[pv_attribs.PV_area_res].mean()))
print('Std PV_area_res {:s}: {:f}'.format(state, TNDS[pv_attribs.PV_area_res].std()))
print('Average PV_area_res Adopters: {:f}'.format(high[pv_attribs.PV_area_res].mean()))
print('Average PV_area_res Moderate Adopters: {:f}'.format(mod[pv_attribs.PV_area_res].mean()))
print('Average PV_area_res Non Adopters: {:f}'.format(non[pv_attribs.PV_area_res].mean()))

print()
print()
print('Average PV_area_by_area {:s}: {:f}'.format(state, TNDS[pv_attribs.PV_area_by_area].mean()))
print('Stdev PV_area_by_area {:s}: {:f}'.format(state, TNDS[pv_attribs.PV_area_by_area].std()))
print('Average PV_area_by_area Adopters: {:f}'.format(high[pv_attribs.PV_area_by_area].mean()))
print('Average PV_area_by_area Moderate Adopters: {:f}'.format(mod[pv_attribs.PV_area_by_area].mean()))
print('Average PV_area_by_area Non Adopters: {:f}'.format(non[pv_attribs.PV_area_by_area].mean()))

print()
print()
print('Average PV_area_total {:s}: {:f}'.format(state, TNDS[pv_attribs.PV_area_total ].mean()))
print('Stdev PV_area_total {:s}: {:f}'.format(state, TNDS[pv_attribs.PV_area_total ].std()))
print('Average PV_area_total Adopters: {:f}'.format(high[pv_attribs.PV_area_total ].mean()))
print('Average PV_area_total Moderate Adopters: {:f}'.format(mod[pv_attribs.PV_area_total ].mean()))
print('Average PV_area_total Non Adopters: {:f}'.format(non[pv_attribs.PV_area_total].mean() ))

print()
print()

print('Average pv_by_total {:s}: {:f}'.format(state, TNDS[pv_by_total ].mean()))
print('Stdev pv_by_total {:s}: {:f}'.format(state, TNDS[pv_by_total ].std()))
print('Average pv_by_total Adopters: {:f}'.format(high[pv_by_total ].mean()))
print('Average pv_by_total Moderate Adopters: {:f}'.format(mod[pv_by_total ].mean()))
print('Average pv_by_total Non Adopters: {:f}'.format(non[pv_by_total].mean() ))
'''
print()
print()

#quit()
#ysets = pv_attribs.PV_attribs_res + [pv_by_total]
ysets = dependentsY[0:1]
#xsets = [income.Income_attribs + housing.Housing_attribs + population.Population_attribs]
#xsets[0] += poverty.Poverty_attribs + education.Education_attribs_basic_and_rate + energy.Energy_attribs_res + age.Age_attribs
xsets= []
#xsets_from_analysis = [poverty.pov_cnt] + [education.edu_LHS] + [education.edu_HS_r] + energy.Energy_attribs_res + [age.age7584] + [age.age3544]
#xsets_from_analysis3 = poverty.Poverty_attribs[1:] + education.Education_attribs_basic_and_rate[0:3] + education.Education_attribs_basic_and_rate[4:] + energy.Energy_attribs_res + age.Age_attribs[1:3]
#xsets_from_analysis2 = [education.edu_LHS] + [education.edu_HS_r] + energy.Energy_attribs_res + [age.age3544]


#show_list(xsets_from_analysis[0], numbered=True)

feature_selected=[ 'per_capita_income',
                    'median_household_income',
                    'employ_rate',
                    'occupation_education_rate',
                    'occupation_manufacturing_rate',
                    'occupation_transportation_rate',
                    'age_median',
                    'age_10_14_rate',
                    'age_15_17_rate',
                    'electricity_consume_residential',
                    'transportation_home_rate',
                    'transportation_walk_rate',
                    'transportation_carpool_rate',
                    'transportation_bicycle_rate',
                    'transportation_public_rate',
                    'diversity',
                    'voting_2016_dem_percentage',
                    'voting_2016_gop_percentage',
                    'travel_time_less_than_10_rate',
                    'travel_time_10_19_rate',
                    'travel_time_20_29_rate',
                    'travel_time_30_39_rate',
                    'travel_time_40_59_rate',
                    'travel_time_60_89_rate']

feature_selected2=['per_capita_income',
                   'employ_rate',
                   'occupation_education_rate',
                   'occupation_manufacturing_rate',
                    'occupation_transportation_rate',
                    'electricity_consume_residential',
                    'transportation_home_rate',
                    'transportation_walk_rate',
                    'transportation_carpool_rate',
                    'transportation_bicycle_rate',
                    'transportation_public_rate',
                   'diversity']

feature_selected3=['per_capita_income',
                    'transportation_home_rate',
                    'transportation_walk_rate',
                    'transportation_bicycle_rate',
                    'transportation_public_rate']

#xsets.append(xsets_from_analysis)
#xsets.append(xsets_from_analysis2)
#xsets.append(xsets_from_analysis3)

# xsets.append(demo_attribsX)
# xsets.append(demo_Model1_med_inc)
#xsets.append(demo_Model1_med_incB)
# xsets.append(demo_Model1_avg_inc)
# xsets.append(demo_Model1_avg_incB3)           # *********a or nona
#xsets.append(demo_Model1_avg_incC)
#xsets.append(demo_Model1_pc_inc)
#xsets.append(demo_Model1_pc_incB)
# xsets.append(demo_Model1_avg_inc + neighborhood_modelA )

#xsets.append(linear_Model_attribs.DSdemo.DS_income[0:1])
#xsets.append(linear_Model_attribs.DSdemo.DS_income[1:2])
#xsets.append(linear_Model_attribs.DSdemo.DS_income[2:3])
#xsets.append(linear_Model_attribs.DSdemo.DS_age[0:1])
#xsets.append(linear_Model_attribs.DSdemo.DS_age[1:2])

#xsets.append(linear_Model_attribs.DSdemo.DS_pov)
#xsets.append(linear_Model_attribs.DSdemo.DS_edu[0:1])
#xsets.append(linear_Model_attribs.DSdemo.DS_edu[1:2])

#xsets.append(linear_Model_attribs.DSdemo.DS_pol[0:1])
#xsets.append(linear_Model_attribs.DSdemo.DS_pol[1:2])
#xsets.append(linear_Model_attribs.DSdemo.DS_pol[2:3])
#xsets.append(linear_Model_attribs.DSdemo.DS_pol[3:4])

#xsets.append(linear_Model_attribs.DSdemo.DS_emp)
#xsets.append(linear_Model_attribs.DSdemo.DS_div)
#xsets.append(linear_Model_attribs.DSdemo.DS_wnw)



#xsets.append(neighborhood_modelB )
#xsets.append(linear_Model_attribs.SVIdemo.SVI_socio_index )
#xsets.append(linear_Model_attribs.SVIdemo.SVI_age)

# Model a
#xsets.append(linear_Model_attribs.SVIdemo.SVI_age + linear_Model_attribs.SVIdemo.SVI_pov)
#xsets.append(linear_Model_attribs.SVIdemo.SVI_edu )
#xsets.append(linear_Model_attribs.SVIdemo.SVI_income)
#xsets.append(linear_Model_attribs.SVIdemo.SVI_emp )
#xsets.append(linear_Model_attribs.SVIdemo.SVI_pov)
#xsets.append(linear_Model_attribs.SVIdemo.SVI_mnrty)
#xsets.append(linear_Model_attribs.SVIdemo.SVI_disabl )

#xsets.append(linear_Model_attribs.models.socio_econ.a_or_na1)
#xsets.append(linear_Model_attribs.models.socio_econ.a_or_na2)
#xsets.append(linear_Model_attribs.models.socio_econ.a_or_na3)
#xsets.append(linear_Model_attribs.models.socio_econ.a_or_na4)
#xsets.append(linear_Model_attribs.models.socio_econ.a_or_na5)
#xsets.append(linear_Model_attribs.models.socio_econ.a_or_na6)
#xsets.append(linear_Model_attribs.models.socio_econ.a_or_na7)
#xsets.append(linear_Model_attribs.models.socio_econ.a_or_na8)

'''
attrib_s = [linear_Model_attribs.DSdemo.DS_income[2:],
            linear_Model_attribs.DSdemo.DS_edu,
            linear_Model_attribs.DSdemo.DS_age[1:],
            linear_Model_attribs.DSdemo.DS_pol[2:],
            linear_Model_attribs.DSdemo.DS_emp,
            linear_Model_attribs.DSdemo.DS_pov,
            linear_Model_attribs.DSdemo.DS_div+linear_Model_attribs.DSdemo.DS_wnw]
'''

attrib_s = [linear_Model_attribs.DShouse.DS_val+\
            #linear_Model_attribs.DShouse.DS_mr+\
            linear_Model_attribs.DShouse.DS_fam_r+\
            linear_Model_attribs.DShouse.DS_h_cnt+\
            linear_Model_attribs.DShouse.DS_pop[1:]+\
            linear_Model_attribs.DShouse.DShome_sz+\
            linear_Model_attribs.DShouse.DS_energy[1:]+\
            linear_Model_attribs.DShouse.DS_heating[1:3]+\
            #linear_Model_attribs.SVIhouse.SVI_disable+\
            linear_Model_attribs.SVIhouse.SVI_insur]
            #linear_Model_attribs.SVIhouse.SVI_lang]

soc_block = [income.avg_inc_scld, education.edu_yrs, ]
hood_block = []
geo_climate_block = []
poli_green_block = []
incentives_block = []


#xsets = A_o_NA_attrib_list_gen(attrib_s)

xsets = attrib_s


#xsets.append(Basic_set)
#xsets.append(feature_selected)
#xsets.append(feature_selected2)
#xsets.append(feature_selected3)
#show_list(xsets[0], numbered=True)

print()
print()
print('##########################################################################################################')
print('##########################################################################################################')
print('                                     Entire State of {:s}'.format(state.upper()))
print('##########################################################################################################')
print('##########################################################################################################')
print()
print()
dd.analyze_data(TNDS, ysets, xsets)

print()
print()
print('##########################################################################################################')
print('##########################################################################################################')
print('                                        Adoptors')
print('##########################################################################################################')
print('##########################################################################################################')
print()
print()
dd.analyze_data(adopters, ysets, xsets)

'''
print()
print()
print('##########################################################################################################')
print('##########################################################################################################')
print('                                        High Adoption')
print('##########################################################################################################')
print('##########################################################################################################')
print()
print()
dd.analyze_data(high, ysets, xsets)
'''

print()
print()
print('##########################################################################################################')
print('##########################################################################################################')
print('                                        Low Adoption')
print('##########################################################################################################')
print('##########################################################################################################')
print()
print()
#          dd.analyze_data(mod, ysets, xsets)

print()
print()
#print('##########################################################################################################')
#print('##########################################################################################################')
#print('                                        Non Adoption')
#print('##########################################################################################################')
#print('##########################################################################################################')
#print()
#print()
#dd.analyze_data(non, ysets, xsets)