import pandas as pd
import numpy as np
import operator

output = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output'
output_server = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar'
output_storage = r'K:\DEEP_SOLAR'
output_storage2 = r'K:\DEEP_SOLAR_BIG'
output_storage3 = r'K:\DEEP_SOLAR_BIG2'

dsexcel = 'Deep_Solar.xlsx'


TN_a ='\TNadopters.xlsx'
TN_ha = '\TN_high_adopters.xlsx'
TN_ma = '\TN_moderate_adopters.xlsx'
TN_na = '\TN_non_adopters.xlsx'

TVA_service_excel =r'K:\DEEP_SOLAR_BIG2\TVA_Coverage_area.xlsx'
DeepSolar_orig = r'K:\DEEP_SOLAR\deepsolar_tract_orig.xlsx'
DeepSolar_orig_renamed = r'K:\DeepSolarOriginal\deepsolar_tract_renamed.xlsx'
DeepSolar_excel = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\deepsolar_tract.xlsx'
DeepSolarTN_excel = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\TNDS.xlsx'
DeepSolarTN_excel_adopters = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\TN' + TN_a
DeepSolarTN_excel_high_adopters = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\TN' + TN_ha
DeepSolarTN_excel_low_adopters = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\TN' + TN_ma
DeepSolarTN_excel_non_adopters = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\TN' + TN_na
tn_storage_path_analysis = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar'
TNDeepSolar_excel = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\TN\TNDeep_Solar.xlsx'
TNDS_BIG = r'K:\DEEP_SOLAR_BIG\TN\TNDeep_Solar.xlsx'

TN_sheet = r'\TN'
AL_sheet = r'\AL'
AR_sheet = r'\AR'
FL_sheet = r'\FL'
IA_sheet = r'\IA'
IN_sheet = r'\IN'
LA_sheet = r'\LA'
MI_sheet = r'\MI'
OH_sheet = r'\OH'
SC_sheet = r'\SC'
US_sheet = r'\US'
WV_sheet = r'\WV'
GA_sheet = r'\GA'
KY_sheet = r'\KY'
MS_sheet = r'\MS'
NC_sheet = r'\NC'
VA_sheet = r'\VA'

# suffixes into region excel files for
by_state = 'Deep_Solar.xlsx'                    # whole region
adopters = '_adopt_Deep_Solar.xlsx'             # adopers for region
nonadopters = '_nonadopt_Deep_Solar.xlsx'       # non adopters for region

# paths to different regions's excel files
class regions:
    class regions_path_local:
        US_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\US'
        AL_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\AL'
        AR_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\AR'
        FL_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\FL'
        GA_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\GA'
        IA_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\IA'
        IN_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\TN'
        KY_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\KY'
        LA_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\LA'
        MI_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\MI'
        MS_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\MS'
        NC_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\NC'
        OH_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\OH'
        SC_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\SC'
        TN_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\TN'
        VA_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\VA'
        WV_pth = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\DeepSolar_Analysis_output\WV'
    class regions_path_server:
        US_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\US'
        AL_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\AL'
        AR_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\AR'
        FL_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\FL'
        GA_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\GA'
        IA_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\IA'
        IN_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\TN'
        KY_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\KY'
        LA_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\LA'
        MI_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\MI'
        MS_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\MS'
        NC_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\NC'
        OH_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\OH'
        SC_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\SC'
        TN_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\TN'
        VA_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\VA'
        WV_pth = r'K:\LowIncomeSolar\DataNTables\Analysis of Deep Solar\WV'

class US_PV_Stats:
    us_pv_stats={'PV_cnt':{'sum':1466550.00,'avg':20.22,'std':54.23},
                 'PV_cnt_res':{'sum':1277794.00,'avg':17.62,'std':48.97},
                 'PV_res_area':{'sum':33053007.97,'avg':455.67,'std':1321.02},
                 'PV_area':{'sum':96731548.06,'avg':1333.55,'std':6103.44},
                 'PV_area_by_area':{'sum':26076076.28,'avg':359.61,'std':918.88}}



# U.S. over all stats
US_PVavg = 20.22
US_PVresavg = 455
US_PVbyAreaavg = 21.46
US_PV_per_house= 8.08
US_avg_income = 73314
USavg_house_size = 224800
USpov_rate = .35757

# U.S. adopter stats
US_PVavg_adopters = 27
US_PVresavg_adopters = 24
US_PVbyAreaavg_adopters = 487
US_PV_per_house_adopters= -9999
US_avg_income_adopters = 77839
USavg_house_size_adopters = 2.7
USpov_rate_adopters = .118

# U.S. non-adopter stats
US_PVavg_non = 0
US_PVresavg_non = 0
US_PVbyAreaavg_non = 0
US_PV_per_hous_non= 8.08
US_avg_income_non = 73314
USavg_house_size_non = 224800
USpov_rate_non = .35757

class geo:
    fips = 'fips'
    county = 'county'
    lat = 'lat'
    lon = 'lon'
    state='state'
    land_area = 'land_area'
    total_area = 'total_area'
    water_area = 'water_area'
    Geo_attribs = [fips, county, lat, lon, state, land_area, total_area, water_area]
    Geo_attribs_area = [total_area, land_area, water_area]
    Geo_attribs_location = [fips, county, state, lat, lon]
class heating:
    coal = 'heating_fuel_coal_coke'
    electricity = 'heating_fuel_electricity'
    kerosene = 'heating_fuel_fuel_oil_kerosene'
    gas = 'heating_fuel_gas'
    housing_unit = 'heating_fuel_housing_unit_count'
    none = 'heating_fuel_none'
    other = 'heating_fuel_other'
    solar = 'heating_fuel_solar'
    Heating_attribs = [coal, electricity, kerosene, gas, housing_unit, none, other, solar]
class occupation:
    employed = 'employed'
    employ_rate = 'employ_rate'
    unemployed = 'unemployed'
    const_r = 'occupation_construction_rate'
    pub_r = 'occupation_public_rate'
    info_r = 'occupation_information_rate'
    finance_r = 'occupation_finance_rate'
    edu_r = 'occupation_education_rate'
    admin_r = 'occupation_administrative_rate'
    manuf_r = 'occupation_manufacturing_rate'
    wholesale_r = 'occupation_wholesale_rate'
    retail_r = 'occupation_retail_rate'
    trans_r = 'occupation_transportation_rate'
    arts_r = 'occupation_arts_rate'
    argri_r = 'occupation_agriculture_rate'
    Occupation_attribs = [employed, employ_rate, unemployed, const_r, pub_r, info_r, finance_r, edu_r,
                          admin_r, manuf_r, wholesale_r, retail_r, trans_r, arts_r, argri_r]
    Occupation_attribs_employment = [employed, employ_rate, unemployed]
class transportation:
    at_home = 'transportation_home_rate'
    car = 'transportation_car_alone_rate'
    walk = 'transportation_walk_rate'
    carpool = 'transportation_carpool_rate'
    motorcycle = 'transportation_motorcycle_rate'
    bike = 'transportation_bicycle_rate'
    public = 'transportation_public_rate'
    travel_10 = 'travel_time_less_than_10_rate'
    travel_10_19 = 'travel_time_10_19_rate'
    travel_20_29 = 'travel_time_20_29_rate'
    travel_30_39 = 'travel_time_30_39_rate'
    travel_40_59 = 'travel_time_40_59_rate'
    travel_60_89 = 'travel_time_60_89_rate'
    travel_avg = 'travel_time_average'
    Transportation_attribs = [at_home, car, walk, carpool, motorcycle, bike, public, travel_10, travel_10_19,
                              travel_20_29, travel_30_39, travel_40_59, travel_60_89, travel_avg]
class health_insurance:
    public_rate = 'health_insurance_public_rate'
    none = 'health_insurance_none_rate'
    Health_insurance_attribs = [public_rate, none]
class pv_attribs:
    # PV attributes
    PV_cnt = 'solar_system_count'
    PV_area_total = 'total_panel_area'
    PV_area_res = 'total_panel_area_residential'
    PV_area_nres = 'total_panel_area_nonresidential'
    PV_area_by_area = 'solar_panel_area_divided_by_area'
    PV_res = 'solar_system_count_residential'
    PV_nres = 'solar_system_count_nonresidential'
    PV_per_house = 'number_of_solar_system_per_household'
    PVarea_by_Harea = 'PVaByHa'
    PV_adopt_non = 'A_o_NA'
    PV_attribs = [PV_cnt, PV_area_res, PV_area_nres, PV_area_by_area, PV_res, PV_nres, PV_per_house]
    PV_attribs_res = [PV_res, PV_area_res, PV_area_by_area, PV_area_total, PV_per_house, PV_adopt_non]
class tiles:
    tile_cnt = 'tile_count'
    Tiles_attribs = [tile_cnt]
class solar:
    # solar potential
    SR = 'daily_solar_radiation'
    Solar_attribs = [SR]
class income:
    avg_inc = 'average_household_income'
    avg_inc_scld = r'avg_inc_scaled'
    pc_inc = 'per_capita_income'
    med_inc = 'median_household_income'
    Income_attribs = [avg_inc, pc_inc, med_inc]
class education:
    edu_B = 'education_bachelor'
    edu_C = 'education_college'
    edu_Dr = 'education_doctoral'
    edu_MS = 'education_master'
    edu_HS = 'education_high_school_graduate'
    edu_LHS = 'education_less_than_high_school'
    edu_pop = 'education_population'
    edu_trd = 'education_professional_school'
    edu_lHS_r = 'education_less_than_high_school_rate'
    edu_HS_r = 'education_high_school_graduate_rate'
    edu_col_r = 'education_college_rate'
    edu_bs_r = 'education_bachelor_rate'
    edu_ms_r = 'education_master_rate'
    edu_trade_r = 'education_professional_school_rate'
    edu_dr_r = 'education_doctoral_rate'
    edu_yrs = 'number_of_years_of_education'
    do16_9_inschool_r = 'dropout_16_19_inschool_rate'

    Education_attribs = [edu_B, edu_C, edu_Dr, edu_MS, edu_HS, edu_LHS, edu_pop, edu_trd, do16_9_inschool_r,
                         edu_lHS_r, edu_HS_r, edu_col_r, edu_bs_r, edu_ms_r, edu_trade_r, edu_dr_r, edu_yrs]
    Education_attribs_basic = [edu_LHS, edu_HS, edu_C, edu_yrs]
    Education_attribs_basic_rate = [edu_lHS_r, edu_HS_r, edu_col_r]
    Education_attribs_basic_and_rate = Education_attribs_basic + Education_attribs_basic_rate
    Education_attribs_higher = [edu_C, edu_B, edu_MS, edu_Dr]
    Education_attribs_higher_rate = [edu_bs_r, edu_ms_r, edu_dr_r, edu_HS_r, edu_yrs]
class energy:
    # energy stats
    elec_prc_r = 'electricity_price_residential'
    elec_cons_r = 'electricity_consume_residential'
    avg_e_rate = 'avg_electricity_retail_rate'
    elect_price_com = 'electricity_price_commercial'
    elect_price_indust = 'electricity_price_industrial'
    elect_price_transpor = 'electricity_price_transportation'
    elect_price_overall = 'electricity_price_overall'
    elect_consume_com = 'electricity_consume_commercial'
    elect_consume_indust = 'electricity_consume_industrial'
    elect_consume_tot = 'electricity_consume_total'

    Energy_attribs = [elec_prc_r, elec_cons_r, avg_e_rate, elect_price_com, elect_price_indust, elect_price_transpor,
                      elect_price_overall, elect_consume_com, elect_consume_indust, elect_consume_tot]
    Energy_attribs_res = [elec_prc_r, elec_cons_r]
class population:
    # population stats
    pop = 'population'
    pop_den = 'population_density'
    Population_attribs = [pop, pop_den]
class poverty:
    # poverty states
    pov_fam_bl = 'poverty_family_below_poverty_level'
    pov_cnt = 'poverty_family_count'
    fam_bl_pov = 'poverty_family_below_poverty_level_rate'
    Poverty_attribs = [pov_fam_bl, pov_cnt, fam_bl_pov]
class housing:
    # housing stats
    Num_units = 'housing_unit_count'
    avg_house_size = 'average_household_size'
    house_val = 'housing_unit_median_value'
    household_type_family_rate = 'household_type_family_rate'
    vacant_r = 'occupancy_vacant_rate'
    owner_r = 'occupancy_owner_rate'
    mortgage_r = 'mortgage_with_rate'
    Housing_attribs = [Num_units, avg_house_size, house_val,household_type_family_rate,
                       vacant_r, owner_r, mortgage_r]
    Housing_attribs_basic = [Num_units, avg_house_size, house_val,  household_type_family_rate, mortgage_r]
class political:
    dem16 = 'voting_2016_dem_percentage'
    gop16 = 'voting_2016_gop_percentage'
    dem_win16 = 'voting_2016_dem_win'
    dem_pct12 = 'voting_2012_dem_percentage'
    gop_pct12 = 'voting_2012_gop_percentage'
    dem_win12 = 'voting_2012_dem_win'
    Political_attribs = [dem16, gop16, dem_win16, dem_pct12, gop_pct12, dem_win12]
    Political_attribs_basic = [dem16, gop16]
class age:
    # demographics
    med_age = 'age_median'
    age1824 = 'age_18_24_rate'
    age2534 = 'age_25_34_rate'
    age85p = 'age_more_than_85_rate'
    age7584 = 'age_75_84_rate'
    age3544 = 'age_35_44_rate'
    age4554 = 'age_45_54_rate'
    age6574 = 'age_65_74_rate'
    age5564 = 'age_55_64_rate'
    age1014 = 'age_10_14_rate'
    age1517 = 'age_15_17_rate'
    age59 = 'age_5_9_rate'
    Age_attribs = [med_age, age1824, age2534, age85p, age7584, age3544, age4554, age6574, age5564, age1014,
                   age1517, age59]
    Age_attribs_to_code = [age1824, age2534, age3544, age4554, age5564, age6574, age7584, age85p]
class diversity:
    # diversity/ racial statistics
    diversity = 'diversity'
    asian = 'race_asian'
    black = 'race_black_africa'
    indian = 'race_indian_alaska'
    islander = 'race_islander'
    other = 'race_other'
    mixed = 'race_two_more'
    white = 'race_white'
    whiteNonwhite = 'W_o_NW'
    Diversity_attribs = [diversity, asian, black, indian, islander, other, mixed, white]
    Diversity_attribs_coded = [whiteNonwhite, diversity]
class incentives:
    incent_res = 'incentive_count_residential'
    incent_nres = 'incentive_count_nonresidential'
    incent_res_st = 'incentive_residential_state_level'
    incent_nres_st = 'incentive_nonresidential_state_level'
    net_metering = 'net_metering'
    feedin_tariff = 'feedin_tariff'
    corp_tax = 'cooperate_tax'
    prop_tax = 'property_tax'
    sales_tax = 'sales_tax'
    rebate = 'rebate'
    Incentives_attribs = [incent_res, incent_nres, incent_res_st, incent_nres_st, net_metering, feedin_tariff,
                          corp_tax, prop_tax, sales_tax, rebate]
class heatingfuel:
    coal_coke = 'heating_fuel_coal_coke'
    electric = 'heating_fuel_electricity'
    kerosene = 'heating_fuel_oil_kerosene'
    gas = 'heating_fuel_gas'
    none = 'heating_fuel_none'
    other = 'heating_fuel_other'
    solar = 'heating_fuel_solar'
    coal_coke_r = 'heating_fuel_coal_coke_rate'
    electric_r = 'heating_fuel_electricity_rate'
    kerosene_r = 'heating_fuel_fuel_oil_kerosene_rate'
    gas_r = 'heating_fuel_gas_rate'
    none_r = 'heating_fuel_none_rate'
    other_r = 'heating_fuel_other_rate'
    solar_r = 'heating_fuel_solar_rate'
    HeatingFuel_attribs = [coal_coke, coal_coke_r, electric, electric_r, kerosene, kerosene_r, gas, gas_r,
                           none, none_r, other, other_r, solar, solar_r]
class climate:
    heating_temp = 'heating_design_temperature'
    cooling_temp = 'cooling_design_temperature'
    earth_temp_amp = 'earth_temperature_amplitude'
    frost_days = 'frost_days'
    air_temp = 'air_temperature'
    daily_solar = solar.SR
    atmospheric_pres = 'atmospheric_pressure'
    wind_speed = 'wind_speed'
    earth_temp = 'earth_temperature'
    heating_deg_days = 'heating_degree_days'
    cooling_deg_days = 'cooling_degree_days'
    Climate_attribs = [daily_solar, heating_temp, cooling_temp, earth_temp, earth_temp_amp, frost_days, air_temp,
                       atmospheric_pres, wind_speed, earth_temp, heating_deg_days, cooling_deg_days]

# dependents

dependentsY = [pv_attribs.PVarea_by_Harea, pv_attribs.PV_adopt_non, pv_attribs.PV_per_house]

#        demo models
demo_Model1_med_inc = [income.med_inc, age.med_age, education.edu_yrs, 'W_o_NW', political.dem_pct12]
demo_Model1_med_incB = [income.med_inc, age.med_age, education.edu_yrs, diversity.diversity, political.dem_pct12]
demo_Model1_avg_incB = [income.avg_inc, age.med_age, education.edu_yrs, diversity.diversity, political.dem_pct12]
demo_Model1_avg_incB2 = [income.avg_inc, education.edu_yrs, diversity.diversity, political.dem_pct12]
demo_Model1_avg_incB3 = [education.edu_yrs, diversity.diversity, political.dem_pct12]
demo_Model1_avg_incB4 = [education.edu_yrs, diversity.diversity, political.dem_pct12]
demo_Model1_avg_incC = [income.avg_inc, education.edu_pop, 'W_o_NW', political.dem_pct12]
demo_Model1_avg_incCaona = [income.avg_inc, education.edu_pop, 'W_o_NW', political.dem_pct12]
demo_Model1_pc_inc = [income.pc_inc, age.med_age, education.edu_yrs, 'W_o_NW', political.dem_pct12]
demo_Model1_pc_incB = [income.pc_inc, age.med_age, education.edu_yrs, diversity.diversity, political.dem_pct12]
demo_Model1_pc_inc2a_o_na = [income.avg_inc, age.med_age, education.edu_yrs, 'W_o_NW', political.dem_pct12]
demo_Model1_pc_inc2PVper = [income.avg_inc, age.med_age, education.edu_yrs]
# Neighborhood models
neighborhood_modelA = [occupation.employ_rate, housing.house_val, housing.mortgage_r, housing.household_type_family_rate,
                      poverty.fam_bl_pov]

neighborhood_modelB = [occupation.employ_rate, housing.house_val, housing.mortgage_r, poverty.pov_cnt,
                      poverty.fam_bl_pov]

demo_attribs = pv_attribs.PV_attribs_res + income.Income_attribs + geo.Geo_attribs_area + heating.Heating_attribs + occupation.Occupation_attribs
demo_attribs += transportation.Transportation_attribs + age.Age_attribs + housing.Housing_attribs + diversity.Diversity_attribs[:7]
demo_attribs += education.Education_attribs + solar.Solar_attribs + political.Political_attribs_basic + incentives.Incentives_attribs

PV_metrics = [pv_attribs.PVarea_by_Harea, pv_attribs.PV_per_house] + age.Age_attribs + diversity.Diversity_attribs_coded

DemoGraphics_block1 = income.Income_attribs + education.Education_attribs + population.Population_attribs

DSdemographicsY = pv_attribs.PV_attribs_res + [pv_attribs.PVarea_by_Harea] + ['A_o_NA']

DSdemographicsX = income.Income_attribs + [education.edu_yrs] + [population.pop, population.pop_den]
DSdemographicsX += age.Age_attribs + [diversity.diversity] + political.Political_attribs_basic


demo_attribsX = income.Income_attribs + geo.Geo_attribs_area + heating.Heating_attribs + occupation.Occupation_attribs
demo_attribsX += transportation.Transportation_attribs + age.Age_attribs + housing.Housing_attribs + diversity.Diversity_attribs[:7]
demo_attribsX += education.Education_attribs + solar.Solar_attribs + political.Political_attribs_basic + incentives.Incentives_attribs

def create_attrib_que(type_list, ranges=None):
    rl = []
    for type in type_list:
        if type == 'PV':
            rl += pv_attribs.PV_attribs
        elif type == 'PV res':
            rl += pv_attribs.PV_attribs_res
        elif type == 'Income':
            rl += income.Income_attribs
        elif type == 'Education':
            rl += education.Education_attribs
        elif type == 'Education basic':
            rl += education.Education_attribs_basic
        elif type == 'Education basic rate':
            rl += education.Education_attribs_basic_rate
        elif type == 'Energy':
            rl += energy.Energy_attribs
        elif type == 'Age':
            rl += age.Age_attribs
        elif type == 'Solar':
            rl += solar.Solar_attribs
        elif type == 'Housing':
            rl += housing.Housing_attribs
        elif type == 'Poverty':
            rl += poverty.Poverty_attribs
        elif type == 'Population':
            rl += population.Population_attribs
        elif type == 'Diversity':
            rl += diversity.Diversity_attribs
        elif type == 'Political':
            rl += political.Political_attribs
        elif type == 'GEO':
            rl += geo.Geo_attribs
        elif type == 'Incentives':
            rl += incentives.Incentives_attribs
        elif type == 'Occupation emp':
            rl += occupation.Occupation_attribs_employment
        elif type == 'Occupation':
            rl += occupation.Occupation_attribs
        elif type == 'Heating':
            rl += heating.Heating_attribs
        elif type == 'Transportation':
            rl += transportation.Transportation_attribs
        elif type == 'Health Insurance':
            rl += health_insurance.Health_insurance_attribs
        elif type == 'Tiles':
            rl += tiles.tile_cnt
        else:
            print('Unkown type {:s}'.format(str(type)))

    return rl

def display_basic_data(adoption_level, N, attrib, classlabel, verbose=False):
    tot = adoption_level[attrib].sum()
    avg = adoption_level[attrib].mean()
    pct = adoption_level.shape[0]/N
    if verbose:
        print('There are {:d} {:s} adopting census tracts.'.format(adoption_level.shape[0], classlabel))
        print('These have a total of {:d} PV installations with an census tract average of {:f}'.format(tot, avg))
        print('This is {:.2f}% of the TN census tracts'.format(100 * (pct)))
        print()
    return tot, avg, pct

def split_data_res_adopt_non(df, hthr=0, midrange=[1,10], lthr=0, verbose=False):

    print('df', len(df))
    adoptors = df.loc[df[pv_attribs.PV_res] > 0]
    print('adoptors',len(adoptors))

    highadoptors = df.loc[df[pv_attribs.PV_res] > hthr]
    print('High adoptors',len(highadoptors))

    moderateadoptors = df.loc[(df[pv_attribs.PV_res] >= midrange[0]) & (df[pv_attribs.PV_res] <= midrange[1] )]
    print('moderateadoptors',len(moderateadoptors))

    nonadoptors = df.loc[df[pv_attribs.PV_res] == 0]
    print('non-adoptors',len(nonadoptors))
    return adoptors, highadoptors, moderateadoptors, nonadoptors

def calculate_PV_stats(df, frd, verbose=False, state=''):
    rd = {}
    frd[state] = rd
    # go through data frame calculating PV stats
    print('Region: {:s}'.format(state))
    for attrib in PV_dict:
        rd[attrib] = {}
        # get sum
        rd[attrib]['sum'] = df[PV_dict[attrib]].sum()
        # get avg
        rd[attrib]['avg'] = df[PV_dict[attrib]].mean()
        # get std
        rd[attrib]['std'] = df[PV_dict[attrib]].std()
        if verbose:
            print('{:s} sum {:.2f}'.format(attrib, rd[attrib]['sum']))
            print('{:s} avg {:.2f}'.format(attrib, rd[attrib]['avg']))
            print('{:s} std {:.2f}'.format(attrib, rd[attrib]['std']))
            print('################################################################################')
    return frd

def calculate_stats(df, frd, attribs, rd={}, verbose=False, state='', N=1):
    print('Region: {:s}'.format(state))
    # create a dictionary for the given state
    # go through data frame calculating stats
    if state.find('adopters') == -1:
        print('found state {:s}', state)
        N = df.shape[0]

    sizeM = df.shape[0]

    for attrib in attribs:
        #print('Attrib: ', attrib)
        rd[attrib] = {}
        # get sum
        rd[attrib]['count'] =  sizeM
        rd[attrib]['pct'] = sizeM/N
        rd[attrib]['sum'] = df[attrib].sum()
        # get avg
        rd[attrib]['avg'] = df[attrib].mean()
        # get std
        rd[attrib]['std'] = df[attrib].std()
        rd[attrib]['min'] = df[attrib].min()
        rd[attrib]['max'] = df[attrib].max()
        if verbose:
            print('{:s} count {:.2f}'.format(attrib, rd[attrib]['count']))
            print('{:s} pct {:.2f}'.format(attrib, rd[attrib]['pct']))
            print('{:s} sum {:.2f}'.format(attrib, rd[attrib]['sum']))
            print('{:s} avg {:.2f}'.format(attrib, rd[attrib]['avg']))
            print('{:s} std {:.2f}'.format(attrib, rd[attrib]['std']))
            print('{:s} min {:.2f}'.format(attrib, rd[attrib]['min']))
            print('{:s} max {:.2f}'.format(attrib, rd[attrib]['max']))
            print('################################################################################')
    frd[state] = rd
    print()
    print()
    return frd, N

def store_stats(statsd, rd={}):
    print('\n\nStoring vals:\n\n')
    countl = '_count'
    pctl = '_pct'
    suml = '_sum'
    avgl = '_avg'
    stdl = '_std'
    minl = '_min'
    maxl = '_max'
    if 'region' not in rd:
        rd['region'] = list()
    # grab regions stat dict
    for region in statsd:
        #print('\n\n\nThis shoud be a state:', region)
        region_d = statsd[region]
        print(region_d)
        #regions.append(region)
        # each regional dict has keys of attributs and at each attribute val is a dictionary
        # where keys are sum, avg, and std and each stores that value for that attrib in current
        # region id. statsd[region][]
        if region not in rd['region']:
            rd['region'].append(region)
        for attrib in region_d:
            if attrib+suml not in rd:
                rd[attrib+countl] = list()
                rd[attrib+pctl] = list()
                rd[attrib+suml] = list()
                rd[attrib+avgl] = list()
                rd[attrib+stdl] = list()
                rd[attrib+minl] = list()
                rd[attrib+maxl] = list()
            #print('Attrib:', attrib)
            #print('sum', region_d[attrib]['sum'])
            rd[attrib+countl].append(region_d[attrib][countl.strip('_')])
            rd[attrib+pctl].append(region_d[attrib][pctl.strip('_')])
            rd[attrib+suml].append(region_d[attrib][suml.strip('_')])
            #print()
            #print('length of sum array:', len(rd[attrib+suml]))
            #print()
            rd[attrib+avgl].append(region_d[attrib][avgl.strip('_')])
            rd[attrib+stdl].append(region_d[attrib][stdl.strip('_')])
            rd[attrib+minl].append(region_d[attrib][minl.strip('_')])
            rd[attrib+maxl].append(region_d[attrib][maxl.strip('_')])
    print('resulting dataframe:\n',rd)
    return rd, statsd
##################################################################################################################
#######################      sets of arrays for grabbing sets of attributes     ##################################
##################################################################################################################

#Basic_data_set = pv_attribs.PV_attribs_res + income.Income_attribs + geo.Geo_attribs_area + education.Education_attribs_basic + education.Education_attribs_basic_rate

def get_file_path(state, file_types):
    st = ''
    st_adopters = ''
    st_nonadopters = ''

    if 'adopters' in file_types:
        st_adopters = '\\{:s}\\{:s}{:s}'.format(state, state, adopters)
    if 'nonadopters' in file_types:
        st_nonadopters = '\\{:s}\\{:s}{:s}'.format(state, state, nonadopters)
    if 'St' in file_types:
        st = '\\{:s}\\{:s}{:s}'.format(state,state, by_state)

    return [st, st_adopters, st_nonadopters]


def make_state_labels(states):
    rl = []
    for st in states:
        rl.append(st)
        rl.append(st+'_adopters')
        rl.append(st+'_nonadopters')

    return rl

#check the length of a fips number incase the
# first part is a single digit
def check_fip_ds(df):
    fips = df['fips'].tolist()
    length = len("{:d}".format((fips[0])))
    print('the length of a fip:{:d}, {:s}'.format(length, "{:d}".format(fips[0])))
    if length == 10:
        rl = []
        for fip in fips:
            rl.append('0'+ "{:d}".format(fip))
        return rl
    return []

#used to process user input for slicing method
def process_user_slicing():
    state = input('What State would you like to analyze, Note: enter state\'s abbreviation (i.e TN): ' ).lower().strip()
    fillna = input('Would you like to fill the na\'s with 0s (y/n): ').lower()
    select_cols = input('Would you like to use a select set of columns (y/n) ').lower()

    if select_cols.lower() == 'y':
        select_cols = True
    else:
        select_cols = False

    return state, fillna, select_cols

def process_df_options(excel, fillna):
    if fillna.lower()[0] == 'y':
        DS = pd.read_excel(excel).fillna(0)
    else:
        DS = pd.read_excel(excel)
    return


def process_df_rename(df, newnames):
        return df.rename(newnames, axis=1, inplace=True)  # new method

def generate_PVareabyHouseArea(DS, dol_ft2=121, PVaByHa='PVaByHMa'):
    DS['avg_house_area'] = DS[housing.house_val].values / dol_ft2
    DS[PVaByHa] = DS[pv_attribs.PV_area_res].values / DS['avg_house_area']
    return DS

def recode_adoption(df):
    rl = list()
    for cnt in df[pv_attribs.PV_res]:
        if cnt > 0:
            rl.append(2)
        else:
            rl.append(1)
    df['A_o_NA'] = rl
    return df

def recode_diversity(df):
    rl = list()
    suml = df[diversity.other].values + df[diversity.mixed].values + df[diversity.asian].values +df[diversity.indian].values + df[diversity.black].values + df[diversity.islander].values
    wlist = df[diversity.white].values

    rl = []
    for nw, w, in zip(suml, wlist):
        if nw >= w:
            rl.append(1)
        else:
            rl.append(0)
    df['W_o_NW'] = rl
    return df

def recode_by_order(df, cols, new_names):
    d = {}
    # for each row in the dataframe
    for i in df.index.values:
        dtmp = {}
        # go through columns comparing the values
        for c in cols:
            if c not in d:
                d[c] = list()
            dtmp[c] = df.loc[i, c]
        # now sort the dict by values
        dtmp_srtd = dict(sorted(dtmp.items(), key=operator.itemgetter(1)))
        #print(dtmp_srtd)

        cnt = 1
        for attrib in dtmp_srtd:
            d[attrib].append(cnt)
            cnt += 1
    newcols = []
    for attrib, name in zip(d, new_names):
        print('attrib:', attrib)
        df[name] = d[attrib]
    print(df.loc[0:5, new_names])
    return df


def check_fip(df):
    fips = df['fips'].tolist()
    length = len("{:d}".format((fips[0])))
    print('the length of a fip:{:d}, {:s}'.format(length, "{:d}".format(fips[0])))
    if length == 10:
        rl = []
        for fip in fips:
            rl.append('0'+ "{:d}".format(fip))
        return rl
    return []


def collect_range(val, splitter, verbose=False):
    return [int(d) for d in val.split(splitter)]

def strip_label(val, labels, verbose=False):
    for label in labels:
        val = val.strip(label)
    return val

def calculate_mean_array(attribs, labels, splitter, verbose=False):
    rl = []
    for at in attribs:
        rl.append(collect_range(strip_label(at, labels, verbose=verbose), splitter, verbose=verbose))
    ra = [np.median(r) for r in rl]
    ra[ra.index(85)] = np.median([85, 94])
    return ra

def Xiaojing_range_coder(df, attribs, labels, splitter, new_label='age_recode', verbose=False, write=False, newfile='Testfiel.xlsx'):

    attrib_med = pd.DataFrame()
    mn = calculate_mean_array(attribs, labels, splitter, verbose=False)
    # get number values of rate attribs using population
    for at, meds in zip(attribs, mn):

        print(df[at].values)
        attrib_med[at] = (df[at].values * meds)
        print(attrib_med[at].values)
        print('###############################################################################')
        print('###############################################################################')
        print('###############################################################################')
        print('###############################################################################')
    df[new_label] = attrib_med.sum(axis=1)

    if write:
        df.to_excel(output_storage2+r"\{:s}".format(newfile))
    else:
        return df


def Deep_Solar_slice(path, excel, state, select_cols, fillna, rename=True, verbose=False, Interactive=False):
    statep = r'\{:s}'.format('') + state.upper()
    file_all = statep + dsexcel
    file_adopters = statep + '_' + 'adopt' + '_' + dsexcel
    file_nonadopters = statep + '_' + 'nonadopt' + '_' + dsexcel

    if state.lower() == '':
        state = 'us'
    if state.lower() == 'us':
        print('Gathering {:s} deep solar data'.format(state.upper()))
        if fillna.lower()[0] == 'y':
            DS = pd.read_excel(excel).fillna(0)
        else:
            DS = pd.read_excel(excel)

        DS['avg_house_area'] = DS[housing.house_val].values / 121
        DS['PVaByHa'] = DS[pv_attribs.PV_area_res].values / DS['avg_house_area']

        # recode continous variables into ordinal
        DS = recode_adoption(DS)            # binary recode 0==pv = 0, 0<PV = 1
        DS = recode_diversity(DS)           # recodes into white or not white

        # grab adoptors and nonadoptors
        DSPVresadopt = DS.loc[DS[pv_attribs.PV_res] > 0]
        DSPVresnonadopt = DS.loc[DS[pv_attribs.PV_res] == 0]


        # check to make sure the fips is set up correctly
        ll = check_fip(DS)
        if len(ll) > 0:
            DS['fips'] = ll
        if rename:
            DS = process_df_rename(DS, re_label)

        # right to files
        DS.to_excel(path + file_all, index=False)
        DSPVresadopt.to_excel(path + file_adopters, index=false)
        DSPVresnonadopt.to_excel(path + file_nonadopters, index=false)
    else:
        print('Gathering {:s} deep solar data'.format(state.upper()))
        print('writing to path {:s}'.format(path))
        if fillna.lower()[0] == 'y':
            if select_cols:
                DS = pd.read_excel(excel).fillna(0)
            else:
                DS = pd.read_excel(excel).fillna(0)
        else:
            if select_cols:
                DS = pd.read_excel(excel)
            else:
                DS = pd.read_excel(excel)

        DS = DS.loc[DS['state'] == state.lower()]

        # code for PV area by house area
        DS['avg_house_area'] = DS[housing.house_val].values / 121
        DS['PVaByHa'] = DS[pv_attribs.PV_area_res].values / DS['avg_house_area']

        DS = recode_adoption(DS)
        DS = recode_diversity(DS)

        DSPVresadopt = DS.loc[DS[pv_attribs.PV_res] > 0]
        DSPVresnonadopt = DS.loc[DS[pv_attribs.PV_res] == 0]

        if rename:
            print('attempting rename:')
            print(DS.columns)
            #DS =i process_df_rename(DS, re_label)
            DS.rename(re_label, axis=1, inplace=True)
            #DS = process_df_rename(DS, re_label)
            print('After the alleged renaming')
            print(DS.columns)

        ll = check_fip(DS)
        if len(ll) > 0:
            DS['fips'] = ll

        print()
        print('Thera are {:d} {:s} ct\'s'.format(DS.shape[0], state))
        print('Thera are {:d} {:s} ct that are PV adopters\'s'.format(DSPVresadopt.shape[0], state))
        print('Thera are {:d} {:s} ct that are non PV adopters\'s'.format(DSPVresnonadopt.shape[0], state))
        print('Creating Excel files {:s}, {:s}, and {:s}'.format(file_all, file_adopters, file_nonadopters))
        print()
        DS.to_excel(path + file_all, index=False)
        DSPVresadopt.to_excel(path + file_adopters, index=False)
        DSPVresnonadopt.to_excel(path + file_nonadopters, index=False)


def A_o_NA_attrib_list_gen(attrib_sets, verbose=False):
    #range_a = [0]
    #for attrib_set in attrib_sets:
    #    range_a.append(len(attrib_set))
    rl = list()
    for inc in attrib_sets[0]:
        for ed in attrib_sets[1]:
            for ag in attrib_sets[2]:
                for pol in attrib_sets[3]:
                    for ep in attrib_sets[4]:
                        for pv in attrib_sets[5]:
                            for dv in attrib_sets[6]:
                                rl.append([inc, ed, ag, pol, ep, pv, dv])
    return rl



###############################################################################################################
###############################################################################################################
###############################################################################################################

class linear_Model_attribs:
    class DSdemo:
        DS_income = [income.avg_inc, income.med_inc, income.pc_inc]
        DS_age = ['age_recode', age.med_age, education.edu_pop]
        DS_pov = [poverty.fam_bl_pov]
        DS_div = [diversity.diversity]
        DS_wnw = ['W_o_NW']
        DS_edu = [education.edu_yrs]
        DS_emp = [occupation.employ_rate]
        DS_pol = [political.dem_pct12, political.gop_pct12, political.dem16, political.gop16]
    class SVIdemo:
        SVI_income = ['EPL_PCI']
        SVI_income_st = ['EP_PCI']
        SVI_emp = ['EPL_UNEMP']
        SVI_pov = ['EPL_POV']
        SVI_edu = ['EPL_NOHSDP']
        SVI_age = ['EPL_AGE17']
        SVI_mnrty = ['EPL_MINRTY']
        SVI_disabl = ['EPL_DISABL']
        SVI_socio_index = ['RPL_THEME1']
    class models:
        class socio_econ:
            # per capita group
            a_or_na1 = [income.pc_inc, education.edu_yrs, age.med_age, political.dem16, occupation.employ_rate,
                    poverty.fam_bl_pov, diversity.diversity]
            a_or_na2 = [income.pc_inc, education.edu_yrs, age.med_age, political.dem16, occupation.employ_rate,
                    poverty.fam_bl_pov, diversity.whiteNonwhite]
            a_or_na6 = [income.pc_inc, education.edu_yrs, age.med_age, political.gop16, occupation.employ_rate,
                        poverty.fam_bl_pov, diversity.whiteNonwhite]
            a_or_na5 = [income.pc_inc, education.edu_yrs, age.med_age, political.gop16, occupation.employ_rate,
                        poverty.fam_bl_pov, diversity.diversity]

            a_or_na3 = [income.pc_inc, education.edu_pop, age.med_age, political.dem16, occupation.employ_rate,
                        poverty.fam_bl_pov, diversity.diversity]
            a_or_na4 = [income.pc_inc, education.edu_pop, age.med_age, political.dem16, occupation.employ_rate,
                        poverty.fam_bl_pov, diversity.whiteNonwhite]
            a_or_na7 = [income.pc_inc, education.edu_pop, age.med_age, political.gop16, occupation.employ_rate,
                        poverty.fam_bl_pov, diversity.diversity]
            a_or_na8 = [income.pc_inc, education.edu_pop, age.med_age, political.gop16, occupation.employ_rate,
                        poverty.fam_bl_pov, diversity.whiteNonwhite]
    class DShouse:
        DS_val = [housing.house_val]
        DS_mr = [housing.mortgage_r]
        DS_fam_r = [housing.household_type_family_rate]
        DS_h_cnt = [housing.Num_units]
        DS_pop = [population.pop, population.pop_den]
        DShome_sz = [housing.avg_house_size]
        DS_energy = [energy.elec_cons_r, energy.elec_prc_r]
        DS_heating = [heatingfuel.kerosene_r, heatingfuel.electric_r, heatingfuel.coal_coke_r]
        DS_home = [DS_val, DS_mr, DS_fam_r, DS_h_cnt] + DS_pop
    class SVIhouse:
        SVI_disable = ['EP_DISABL']
        SVI_insur = ['EP_UNINSUR']
        SVI_lang = ['EP_LIMENG']



basic_data_set_safe = pv_attribs.PV_attribs_res + income.Income_attribs + geo.Geo_attribs + [education.edu_yrs]
basic_data_set_safe += age.Age_attribs + political.Political_attribs_basic

Basic_data_set = pv_attribs.PV_attribs_res + income.Income_attribs + geo.Geo_attribs_area + education.Education_attribs
#Basic_data_set += occupation.Occupation_attribs_employment + age.Age_attribs + energy.Energy_attribs_res + political.Political_attribs_basic
Basic_data_set += occupation.Occupation_attribs + age.Age_attribs + energy.Energy_attribs_res + political.Political_attribs_basic



almost_full_set = pv_attribs.PV_attribs + income.Income_attribs + [education.edu_yrs] + poverty.Poverty_attribs
almost_full_set += age.Age_attribs + [diversity.diversity] + housing.Housing_attribs_basic + political.Political_attribs + incentives.Incentives_attribs
almost_full_set += transportation.Transportation_attribs + energy.Energy_attribs
almost_full_set += heating.Heating_attribs + climate.Climate_attribs + [geo.fips, geo.state] + geo.Geo_attribs_area


#Basic_set = Basic_data_set[3:] + housing.Housing_attribs + diversity.Diversity_attribs + poverty.Poverty_attribs + heating.Heating_attribs
Basic_set = Basic_data_set[4:] + solar.Solar_attribs + [geo.water_area, geo.total_area] + housing.Housing_attribs + [diversity.diversity, diversity.black, diversity.white, diversity.indian, diversity.islander, diversity.mixed, diversity.other] + heating.Heating_attribs + transportation.Transportation_attribs + incentives.Incentives_attribs + political.Political_attribs_basic

demographics = income.Income_attribs + population.Population_attribs + education.Education_attribs_higher_rate + political.Political_attribs_basic
#demographics += [diversity.diversity]
demographics += diversity.Diversity_attribs + age.Age_attribs + poverty.Poverty_attribs + housing.Housing_attribs_basic

PV_dict = {'PV_cnt':pv_attribs.PV_cnt,
           'PV_cnt_res':pv_attribs.PV_res,
           'PV_res_area':pv_attribs.PV_area_res,
           'PV_area':pv_attribs.PV_area_total,
           'PV_area_by_area':pv_attribs.PV_area_by_area}

energy_model = []




re_label = { "Avg_Inc":income.avg_inc,                  #Average Income
             "Med_Inc":income.med_inc,
             "PC_Inc":income.pc_inc,
             "Yrs_edu":education.edu_yrs,
             "DR_edu":education.edu_Dr,
             "MS_edu":education.edu_MS,
             "BS_edu":education.edu_B,
             "COL_edu":education.edu_C,
             "HS_edu":education.edu_HS,
             "LHS_edu":education.edu_LHS,
             "Pop_edu":education.edu_pop,
             "Prof_edR":education.edu_trade_r,
             "DR_edR":education.edu_dr_r,
             "MS_edR":education.edu_ms_r,
             "BS_edR":education.edu_bs_r,
             "COL_edR":education.edu_col_r,
             "HS_edR":education.edu_HS_r,
             "LHS_edR":education.edu_lHS_r,
             "Prf_edR":education.edu_trd,
             "Emp":occupation.employ_rate,
             "Unemp":occupation.unemployed,
             "OC_Cnstr":occupation.const_r,
             "OC_Info":occupation.info_r,
             "OC_Ed":occupation.edu_r,
             "OC_Admin":occupation.admin_r,
             "OC_Trnp":occupation.trans_r,
             "OC_Arts":occupation.trans_r,
             "Fam_cnt":poverty.pov_cnt}

Arc_cols = ['idx',
            'tile_count',
            'solar_system_count',
            'total_panel_area',
            'fips',
            'average_household_income',
            'county',
            'edu_bachelor',
            'edu_college',
            'edu_doctoral',
            'edu_high_school_graduate',
            'edu_less_than_high_school',
            'edu_master',
            'edu_population',
            'edu_professional_school',
            'employed',
            'gini_index',
            'heat_coal_coke',
            'heat_electricity',
            'heat_kerosene',
            'heat_gas',
            'heat_housing_unit_count',
            'heat_none',
            'heat_other',
            'heat_solar',
            'land_area',
            'pc_income',
            'population',
            'population_density',
            'fam_in_poverty',
            'family_count',
            'asian',
            'black',
            'indian_alaska',
            'islander',
            'other',
            'mixed',
            'white',
            'state',
            'total_area',
            'unemployed',
            'water_area',
            'edu_<HS_rate',
            'edu_HS_rate',
            'edu_COL_rate',
            'edu_BS_rate',
            'edu_MS_rate',
            'edu_professional_school_rate',
            'edu_doctoral_rate',
            'white_rate',
            'black_rate',
            'indian_rate',
            'asian_rate',
            'island_rate',
            'Rother_rate',
            'Mixed_rate',
            'employ_rate',
            'fam_pov_rate',
            'gas_rate',
            'elect_rate',
            'kerosene_rate',
            'coke_rate',
            'solar_rate',
            'other_rate',
            'none_rate',
            'PVarBarea',
            'PVareaPC',
            'tile_count_residential',
            'tile_count_nonresidential',
            'PVcnt_residential',
            'PVcntNonresidential',
            'PVareaResidential',
            'PVareaNonresidential',
            'med_income',
            'e_prc_residential',
            'e_prc_commercial',
            'e_prc_industrial',
            'e_prc_transportation',
            'e_price_overall',
            'e_con_residential',
            'e_con_commercial',
            'e_con_industrial',
            'e_con_total',
            'house_count',
            'avg_household_size',
            'house_unit_count',
            'house_occupied_count',
            'house_med_value',
            'hous_med_gross_rent',
            'lat',
            'lon',
            'elevation',
            'heating_design_temperature',
            'cooling_design_temperature',
            'earth_temperature_amplitude',
            'frost_days',
            'air_temperature',
            'relative_humidity',
            'daily_solar_radiation',
            'atmospheric_pressure',
            'wind_speed',
            'earth_temperature',
            'heating_degree_days',
            'cooling_degree_days',
            'age_18_24_rate',
            'age_25_34_rate',
            'age_more_than_85_rate',
            'age_75_84_rate',
            'age_35_44_rate',
            'age_45_54_rate',
            'age_65_74_rate',
            'age_55_64_rate',
            'age_10_14_rate',
            'age_15_17_rate',
            'age_5_9_rate',
            'household_type_family_rate',
            'dropout_16_19_inschool_rate',
            'occ_construction_rate',
            'occ_public_rate',
            'occ_information_rate',
            'occ_finance_rate',
            'occ_education_rate',
            'occ_administrative_rate',
            'occ_manufacturing_rate',
            'occ_wholesale_rate',
            'occ_retail_rate',
            'occ_transportation_rate',
            'occ_arts_rate',
            'occ_agriculture_rate',
            'occp_vacant_rate',
            'occp_owner_rate',
            'mortgage_with_rate',
            'tran_home_rate',
            'tran_car_alone_rate',
            'tran_walk_rate',
            'tran_carpool_rate',
            'tran_motorcycle_rate',
            'tran_bicycle_rate',
            'tran_public_rate',
            'trv_<10_rate',
            'trv10_19_rate',
            'trv20_29_rate',
            'trv30_39_rate',
            'trv40_59_rate',
            'trv60_89_rate',
            'hlth_ins_public_rate',
            'hlth_ins_none_rate',
            'age_median',
            'trv_average',
            'vot16_dem_percentage',
            'vot16_gop_percentage',
            'vot16_dem_win',
            'vot12_dem_percentage',
            'vot12_gop_percentage',
            'vot12_dem_win',
            'yrs__education',
            'diversity',
            'PVper_household',
            'inct_residential',
            'inct_nonresidential',
            'inctResSt_level',
            'inctNonSt_level',
            'net_metering',
            'feedin_tariff',
            'Inct_cooperate_tax',
            'prop_tx',
            'sales_tx',
            'rebate',
	        'avg_e_ret_rate']




#PV attributes
PV_cnt = 'solar_system_count'
PV_area_res = 'total_panel_area_residential'
PV_area_by_area = 'solar_panel_area_divided_by_area'
PV_res = 'solar_system_count_residential'
PV_per_house = 'number_of_solar_system_per_household'

PV_attribs = [PV_cnt, PV_area_res, PV_area_by_area, PV_res, PV_per_house]

# income stats
avg_inc = 'average_household_income'
pc_inc = 'per_capita_income'
med_inc = 'median_household_income'
Income_attribs = [avg_inc, pc_inc, med_inc]


# education stats
edu_B = 'education_bachelor'
edu_C = 'education_college'
edu_Dr = 'education_doctoral'
edu_MS = 'education_master'
edu_HS = 'education_high_school_graduate'
edu_LHS = 'education_less_than_high_school'
ed_pop = 'education_population'
ed_trd = 'education_professional_school'
ed_lHS_r = 'education_less_than_high_school_rate'
ed_HS_r = 'education_high_school_graduate_rate'
ed_col_r = 'education_college_rate'
ed_bs_r = 'education_bachelor_rate'
ed_ms_r = 'education_master_rate'
ed_trade_r = 'education_professional_school_rate'
ed_dr_r = 'education_doctoral_rate'
ed_yrs = 'number_of_years_of_education'
Education_attribs = [edu_B, edu_C, edu_Dr, edu_MS, edu_HS, edu_LHS, ed_pop, ed_trd,
                     ed_lHS_r, ed_HS_r, ed_col_r, ed_bs_r, ed_ms_r, ed_trade_r, ed_dr_r, ed_yrs]

#energy stats
elec_prc_r = 'electricity_price_residential'
elec_cons_r = 'electricity_consume_residential'
avg_e_rate = 'avg_electricity_retail_rate'
Energy_attribs = [elec_prc_r, elec_cons_r, avg_e_rate]


# population stats
pop = 'population'
pop_den = 'population_density'
Population_attribs = [pop, pop_den]


# poverty states
pov_fam_bl = 'poverty_family_below_poverty_level'
pov_cnt = 'poverty_family_count'
fam_bl_pov = 'poverty_family_below_poverty_level_rate'
Poverty_attribs = [pov_fam_bl, pov_cnt, fam_bl_pov]

# housing stats
Num_units = 'housing_unit_count'
avg_house_size = 'average_household_size'
house_val = 'housing_unit_median_value'
Housing_attribs = [Num_units, avg_house_size, house_val]


# demographics
med_age = 'age_median'
Age_attribs = [med_age]

# diversity/ racial statistics
Diversity = 'diversity'
Diversity_attribs = [Diversity]



# solar potential
SR = 'daily_solar_radiation'
Solar_attribs = [SR]

# useful strings
mean = 'mean'
std = 'standard deviation'
median = 'median'


