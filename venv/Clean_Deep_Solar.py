import data_display as dd
import numpy as np
import sklearn
from sklearn.decomposition import FactorAnalysis
import pandas as pd
import statsmodels as sm
from Deep_Solar_aid import *
from GJ_Utils.util import show_list

deep_solar_excel = DeepSolar_orig

DS = pd.read_excel(deep_solar_excel)

orig_cols = DS.columns.values

#print(orig_cols)

cnt = 0
for c in orig_cols:
    if cnt == 0:
        print("= ['{:s},'".format(c))
    elif cnt == len(orig_cols)-1:
        print("\t'{:s}]'".format(c))
    else:
        print("\t'{:s}',".format(c))
    cnt += 1
quit()

class DeepSolarCleanear:
    class sought_strings:
        solar = 'solar_system'
        solar_panel = 'solar_panel_area'
        education = 'education_'
        heating = 'heating_fuel'
        coal_coke = 'coal_coke'
        kerosene = '_kerosene'
        per_capita = 'per_capita'
        poverty = 'poverty_family'
        elect = 'electrical_price'
        dolkWh = 'cents_kWh'
        count = 'count'
        race = 'race_'
        africa = '_africa'
        rate = '_rate'
        tile = 'tile_count'
        design_temp = 'design_temperature'
        heating_deg = 'heating_degree'
        heat_dys = 'heat_dys'
        cooling_deg = 'cooling_degree'
        cool_dys = 'cool_dys'
        daily_solar = 'daily_solar'
        dly_solr = 'dly_solr'
        housing_unit = 'housing_unit'
        house = 'home_'
        age = 'age_'
        occupation = 'occupation_'
        household_type_fam = 'household_type_family_rate'
# now clean up names of attribs