import data_display as dd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import sklearn.preprocessing.MinMaxScaler as minmaxscale
#import sklearn.preprocessing.OrdinalEncoder as ordinal
import statsmodels as sm
from Deep_Solar_aid import *
from GJ_Utils.util import show_list
pd.options.mode.use_inf_as_na = True

# designed to perform heirarchical linear regression
def Hlinear_regression(df, dependent, independent_blocks, verbose=False, normalize=False,
					   block_labels=()):
	# check for added block labels if there are none create a generic list
	if len(block_labels) == 0:
		block_labels = []
		for i in range(len(independent_blocks)):
			block_labels.append('Block {:d}'.format(i+1))

	block_labels = list(block_labels)
	xsets = []
	# as you go add the different independent blocks to model
	for block, label in zip(independent_blocks, block_labels):
		print('Adding Block {:s}'.format(label))
		xsets += block
		dd.analyze_data(df, dependent, [xsets], normalize=normalize)
		if verbose:
			print('###############################################################')
			print('###############################################################')
			print('###############################################################')
			print('###############################################################')
	return 0


# designed to perform heirarchical logistic regression
def Hlogistic_regression(df, dependent, independent_blocks, verbose=False, normalize=False,
						 block_labels=()):
	# check for added block labels if there are none create a generic list
	if len(block_labels) == 0:
		block_labels = []
		for i in range(len(independent_blocks)):
			block_labels.append('Block {:d}'.format(i + 1))
	block_labels = list(block_labels)
	xsets = []
	# as you go add the different independent blocks to model
	for block, label in zip(independent_blocks, block_labels):
		print('Adding Block {:s}'.format(label))
		xsets += block
		dd.analyze_data(df, dependent, [xsets], type='LogR', normalize=normalize)
		if verbose:
			print('###############################################################')
			print('###############################################################')
			print('###############################################################')
			print('###############################################################')
	return 0

# will go through the given sets of dependent variables and return the set that
# generates the "best" model
def model_optimizer(df, dep, indep_blocks_sets, vif_thrsh=5, sig_thrsh=.05, verbose=False, most_sig=False,
					typ='LinReg', normalize=False, block_labels=('Socio-Economics', 'Neighborhood', 'Geo-Climate', 'Incentives')):

	block_labels = list(block_labels)
	for indep in indep_sets:
		if typ == 'LinReg':
			Hlinear_regression(df, dep,indep_blocks, verbose=False, normalize=normalize, block_labels = block_labels)
		else:
			Hlogistic_regression(df, dep, indep_blocks, verbose=False, normalize=normalize,
								 block_labels=block_labels)

seeds_use = ["geoid",
			 "gisjoin",
             "area_km2",
             "centroid_x",
             "very_low_mf_own_hh",
             "very_low_mf_rent_hh",
             "very_low_sf_own_hh",
             "very_low_sf_rent_hh",
             "low_mf_own_hh",
             "low_mf_rent_hh",
             "low_sf_own_hh",
             "low_sf_rent_hh",
             "mod_mf_own_hh",
             "mod_mf_rent_hh",
             "mod_sf_own_hh",
             "mod_sf_rent_hh",
             "mid_mf_own_hh",
             "mid_mf_rent_hh",
             "mid_sf_own_hh",
             "mid_sf_rent_hh",
             "high_mf_own_hh",
             "high_mf_rent_hh",
             "high_sf_own_hh",
             "high_sf_rent_hh",
             "very_low_mf_own_bldg_cnt",
             "very_low_mf_rent_bldg_cnt",
             "very_low_sf_own_bldg_cnt",
             "very_low_sf_rent_bldg_cnt",
             "low_mf_own_bldg_cnt",
             "low_mf_rent_bldg_cnt",
             "low_sf_own_bldg_cnt",
             "low_sf_rent_bldg_cnt",
             "mod_mf_own_bldg_cnt",
             "mod_mf_rent_bldg_cnt",
             "mod_sf_own_bldg_cnt",
             "mod_sf_rent_bldg_cnt",
             "mid_mf_own_bldg_cnt",
             "mid_mf_rent_bldg_cnt",
             "mid_sf_own_bldg_cnt",
             "mid_sf_rent_bldg_cnt",
             "high_mf_own_bldg_cnt",
             "high_mf_rent_bldg_cnt",
             "high_sf_own_bldg_cnt",
             "high_sf_rent_bldg_cnt",
			 "very_low_mf_own_devp_cnt",
			 "very_low_mf_rent_devp_cnt",
			 "very_low_sf_own_devp_cnt",
			 "very_low_sf_rent_devp_cnt",
			 "low_mf_own_devp_cnt",
			 "low_mf_rent_devp_cnt",
			 "low_sf_own_devp_cnt",
			 "low_sf_rent_devp_cnt",
			 "mod_mf_own_devp_cnt",
			 "mod_mf_rent_devp_cnt",
			 "mod_sf_own_devp_cnt",
			 "mod_sf_rent_devp_cnt",
			 "mid_mf_own_devp_cnt",
			 "mid_mf_rent_devp_cnt",
			 "mid_sf_own_devp_cnt",
			 "mid_sf_rent_devp_cnt",
			 "high_mf_own_devp_cnt",
			 "high_mf_rent_devp_cnt",
			 "high_sf_own_devp_cnt",
			 "high_sf_rent_devp_cnt",
			 "very_low_mf_own_devp_m2",
			 "very_low_mf_rent_devp_m2",
			 "very_low_sf_own_devp_m2",
			 "very_low_sf_rent_devp_m2",
			 "low_mf_own_devp_m2",
			 "low_mf_rent_devp_m2",
			 "low_sf_own_devp_m2",
			 "low_sf_rent_devp_m2",
			 "mod_mf_own_devp_m2",
			 "mod_mf_rent_devp_m2",
			 "mod_sf_own_devp_m2",
			 "mod_sf_rent_devp_m2",
			 "mid_mf_own_devp_m2",
			 "mid_mf_rent_devp_m2",
			 "mid_sf_own_devp_m2",
			 "mid_sf_rent_devp_m2",
			 "high_mf_own_devp_m2",
			 "high_mf_rent_devp_m2",
			 "high_sf_own_devp_m2",
			 "high_sf_rent_devp_m2",
			 "very_low_mf_own_mw",
			 "very_low_mf_rent_mw",
			 "very_low_sf_own_mw",
			 "very_low_sf_rent_mw",
			 "low_mf_own_mw",
			 "low_mf_rent_mw",
			 "low_sf_own_mw",
			 "low_sf_rent_mw",
			 "mod_mf_own_mw",
			 "mod_mf_rent_mw",
			 "mod_sf_own_mw",
			 "mod_sf_rent_mw",
			 "mid_mf_own_mw",
			 "mid_mf_rent_mw",
			 "mid_sf_own_mw",
			 "mid_sf_rent_mw",
			 "high_mf_own_mw",
			 "high_mf_rent_mw",
			 "high_sf_own_mw",
			 "high_sf_rent_mw",
			 "very_low_mf_own_mwh",
			 "very_low_mf_rent_mwh",
			 "very_low_sf_own_mwh",
			 "very_low_sf_rent_mwh",
			 "low_mf_own_mwh",
			 "low_mf_rent_mwh",
			 "low_sf_own_mwh",
			 "low_sf_rent_mwh",
			 "mod_mf_own_mwh",
			 "mod_mf_rent_mwh",
			 "mod_sf_own_mwh",
			 "mod_sf_rent_mwh",
			 "mid_mf_own_mwh",
			 "mid_mf_rent_mwh",
			 "mid_sf_own_mwh",
			 "mid_sf_rent_mwh",
			 "high_mf_own_mwh",
			 "high_mf_rent_mwh",
			 "high_sf_own_mwh",
			 "high_sf_rent_mwh",
			 "very_low_mf_own_elep_hh",
			 "very_low_mf_rent_elep_hh",
			 "very_low_sf_own_elep_hh",
			 "very_low_sf_rent_elep_hh",
			 "low_mf_own_elep_hh",
			 "low_mf_rent_elep_hh",
			 "low_sf_own_elep_hh",
			 "low_sf_rent_elep_hh",
			 "mod_mf_own_elep_hh",
			 "mod_mf_rent_elep_hh",
			 "mod_sf_own_elep_hh",
			 "mod_sf_rent_elep_hh",
			 "high_mf_own_elep_hh",
			 "high_mf_rent_elep_hh",
			 "high_sf_own_elep_hh",
			 "high_sf_rent_elep_hh",
			 "company_na",
			 "company_ty",
			 "eia_id",
			 "cust_cnt",
			 "avg_monthly_consumption_kwh",
			 "avg_monthly_bill_dlrs",
			 "dlrs_kwh",
			 "avg_pbi_usd_p_kwh",
			 "avg_cbi_usd_p_w",
			 "avg_ibi_pct",
             "hh_gini_index",
             "pop_total",
			 "pop_male",
			 "pop_female",
 			 "pop_over_65",
			 "pop_under_18",
			 "hu_monthly_owner_costs_lessthan_1000dlrs",
			 "hu_monthly_owner_costs_greaterthan_1000dlrs",
			 "hu_own",
			 "hu_rent",
			 "hu_vintage_2010toafter",
			 "hu_vintage_2000to2009",
			 "hu_vintage_1980to1999",
			 "hu_vintage_1960to1970",
			 "hu_vintage_1940to1959",
			 "hu_vintage_1939toearlier",
			 "hu_med_val",
			 "hu_mortgage",
			 "hu_no_mortgage",
             "climate_zone",
             "climate_zone_description",
             "moisture_regime",
             "locale",
             "active_subsidies",
			 "avg_months_tenancy",
             "pct_eli_hh",
			 "lihtc_qualified"]

DS_use = ["solar_system_count",
		  "residential_PVarea_by_land_area",
		  "A_o_NA",
			 "PVaByHa",
			 "ZPVaByHa",
			 "Znumber_of_solar_system_per_household",
			 "number_of_solar_system_per_household",
			 "Ln_PV_per_home",
			 "total_panel_area_residential",
			 "solar_system_count_residential",
			 "Zsolar_system_count_residential",
 			 "average_household_income",
			 "Zaverage_household_income",
			 "diversity",
			 "Zdiversity",
 			 "E_PCI",
			 "EP_PCI",
			 "EPL_PCI",
			 "Zemploy_rate",
			 "Zemployed",
			 "Zunemployed",
			 "unemployed",
			 "employ_rate",
			 "employed",
			 "population",
			 "Zpopulation",
			 "POP_DEN_scaled",
			 "Zpopulation_density",
			 "population_density",
			 "E_TOTPOP",
			 "E_DAYPOP_scaled",
			 "E_DAYPOP",
			 "pct_E_Day_POP",
			 "ZE_DAYPOP",
			 "EP_POV",
			 "EPL_POV",
			 "poverty_family_below_poverty_level_rate",
			 "poverty_family_below_poverty_level",
			 "poverty_family_count",
			 "Years_edu_sqr",
			 "number_of_years_of_education",
			 "Znumber_of_years_of_education",
			 "gini_index",
			 "avg_electricity_retail_rate",
			 "electricity_price_residential",
			 "electricity_consume_residential",
			 "Zavg_electricity_retail_rate",
			 "Zelectricity_price_residential",
			 "Zelectricity_consume_residential",
			 "Zaverage_household_size",
		     "average_household_size",
             "housing_unit_median_value",
			 "household_type_family_rate",
			 "Zhousehold_type_family_rate",
			 "mortgage_with_rate",
			 "Zmortgage_with_rate",
			 "Zheating_fuel_fuel_oil_kerosene_rate",
			 "Zheating_fuel_coal_coke_rate",
			 "heating_fuel_gas_rate",
			 "health_insurance_public_rate",
			 "health_insurance_none_rate",
			 "E_UNINSUR",
			 "EP_UNINSUR",
			 "SPL_THEME1",
			 "RPL_THEME1",
			 "SPL_THEME2",
			 "RPL_THEME2",
			 "SPL_THEME3",
			 "RPL_THEME3",
			 "SPL_THEME4",
			 "RPL_THEME4",
			 "RPL_THEMES",
 			 "state",
			 "county",
			 "fips",
			 "total_area",
			 "Ztotal_area",
			 "land_area",
			 "Zland_area",
			 "water_area",
			 "lat",
			 "lon",
			 "elevation",
			 "Zelevation",
			 "heating_design_temperature",
			 "Zheating_design_temperature",
			 "cooling_design_temperature",
			 "Zcooling_design_temperature",
			 "Zatmospheric_pressure",
			 "Zwind_speed",
			 "Zearth_temperature",
			 "Zheating_degree_days",
			 "Zcooling_degree_days",
			 "earth_temperature_amplitude",
			 "Zearth_temperature_amplitude",
			 "frost_days",
			 "Zfrost_days",
			 "air_temperature",
			 "Zair_temperature",
			 "relative_humidity",
			 "Zrelative_humidity",
			 "Zdaily_solar_radiation",
			 "daily_solar_radiation",
			 "atmospheric_pressure",
			 "wind_speed",
			 "earth_temperature",
			 "heating_degree_days",
			 "cooling_degree_days",
			 "age_recode",
			 "age_median",
			 "age25_65",
 			 "Zage_recode",
			 "Zage_median",
			 "Zeducation_population_over_25",
			 "Zage25_65",
			 "education_population_over_25",
 			 "GOP_dominate_jobs1",
			 "DEM_dominate_jobs1",
 			 "ZDEM_dominate_jobs1",
			 "ZGOP_dominate_jobs1",
			 "Tech_Edu_Info_jobs",
			 "Non_tech_jobs",
			 "ZNon_tech_jobs",
			 "Green_travelers3",
			 "ZGreen_travelers3",
			 "travel_time_average",
			 "Ztravel_time_average",
			 "Zvoting_2016_dem_percentage",
			 "Zvoting_2016_gop_percentage",
			 "Zvoting_2012_dem_percentage",
			 "Zvoting_2012_gop_percentage",
			 "voting_2016_dem_percentage",
			 "voting_2016_gop_percentage",
			 "voting_2012_dem_percentage",
			 "voting_2012_gop_percentage",
		  	 "incentive_count_residential",
			 "Zincentive_count_residential",
			 "net_metering",
			 "feedin_tariff",
			 "cooperate_tax",
			 "property_tax",
			 "sales_tax",
			 "rebate",
			 "incentive_residential_state_level",
			 "Zincentive_residential_state_level",
			 "Znet_metering",
			 "Zfeedin_tariff",
			 "Zproperty_tax"]

exFile = r'K:\TVA_SVI\TVA_DS_SVI_NREL_beta.xlsx'


test_data = pd.read_excel(exFile)

adopter_data = test_data.loc[test_data['solar_system_count'] > 0]

age_attribs = []

gender_attribs = []

occupation_attribs = []

energy_attribs = []



# socio-economic block
soc_econ = ["average_household_income",             # 1 income
            "number_of_years_of_education",         # 2 education
            "diversity",                            # 3 racial makeup
            "education_population_over_25",         # 4 age ()
            "pct_Female",                           # 5 gender
            "Non_tech_jobs"]                        # 6 % occupations adverse to adoption

soc_econA = ["average_household_income",             # 1 income
            "number_of_years_of_education",         # 2 education
            "diversity",                            # 3 racial makeup
            "age25_65",         # 4 age ()
            "pct_Female",                           # 5 gender
            "Non_tech_jobs"]                        # 6 % occupations adverse to adoption

soc_econB = ["average_household_income",             # 1 income
            "number_of_years_of_education",         # 2 education
            "diversity",                            # 3 racial makeup
			"age_median",       # 4 age ()
            "pct_Female",                           # 5 gender
            "Non_tech_jobs"]                        # 6 % occupations adverse to adoption


hood = ["population_density",
        "E_DAYPOP",
        "gini_index",
        "household_type_family_rate",
        "hu_own",
        "avg_monthly_bill_dlrs",
        "voting_2016_gop_percentage",
        "Green_travelers3"]

hoodA = ["population_density",
        "E_DAYPOP",
        "gini_index",
        "household_type_family_rate",
        "Zheating_fuel_coal_coke_rate",
        "hu_built_since_80",
        "voting_2016_gop_percentage",
        "Green_travelers3"]

hoodB = ["population_density",
        "E_DAYPOP",
        "hu_monthly_owner_costs_lessthan_1000dlrs",
        "household_type_family_rate",
        "Zheating_fuel_coal_coke_rate",
        "hu_built_since_80",
        "voting_2016_gop_percentage",
        "Green_travelers3"]


geo_climate = ["land_area",
               "atmospheric_pressure",
               'coded_locale']

incent = ["net_metering",
		  "incentive_count_residential",
		  "incentive_residential_state_level",]

incentA = []

# =============================================================================================================
# soc_econ: rsqr: , Sig:
# soc_econ + hood: rsqr: , Sig: hVIF:
# soc_econ + hood + geo: rsqr: .296, Sig:  hVIF:
# soc_econ + hood + geo + ince: rsqr: Sig: hVIF:
#
# --------------------------------------------------------------------------------------------------------------
# Soc_econ: 										A: % NA: % Acc:  high VIF:
# Soc_econ + Hood: 									A: % NA: % Acc:  high VIF:
# Soc_econ + Hood + geo_climate: 					A: % NA:% Acc:%  high VIF:
# Soc_econ + Hood + geo_climate + incentives: 		A: % NA:% Acc:%  high VIF:
blocks1 = [soc_econ, hood, geo_climate, incent]  # 70, 74.5, 76.4, 75.9

# =============================================================================================================
# soc_econ: rsqr: , Sig:
# soc_econ + hood: rsqr: , Sig: hVIF:
# soc_econ + hood + geo: rsqr: Sig:  hVIF:
# soc_econ + hood + geo + ince: rsqr: Sig: hVIF:
#
# --------------------------------------------------------------------------------------------------------------
# Soc_econ: 										A: % NA: % Acc:  high VIF:
# Soc_econ + Hood: 									A: % NA: % Acc:  high VIF:
# Soc_econ + Hood + geo_climate: 					A: % NA:% Acc:%  high VIF:
# Soc_econ + Hood + geo_climate + incentives: 		A: % NA:% Acc:%  high VIF:
blocks2 = [soc_econ, hoodA, geo_climate, incent] # 70.7, 74.9, 75.6, 75.7

# =============================================================================================================
# soc_econ: rsqr: , Sig:
# soc_econ + hood: rsqr: , Sig: hVIF:
# soc_econ + hood + geo: rsqr: Sig:  hVIF:
# soc_econ + hood + geo + ince: rsqr: Sig: hVIF:
#
# --------------------------------------------------------------------------------------------------------------
# Soc_econ: 										A: % NA: % Acc:  high VIF:
# Soc_econ + Hood: 									A: % NA: % Acc:  high VIF:
# Soc_econ + Hood + geo_climate: 					A: % NA:% Acc:%  high VIF:
# Soc_econ + Hood + geo_climate + incentives: 		A: % NA:% Acc:%  high VIF:
blocks3 = [soc_econ, hoodB, geo_climate, incent] # 70.7, 75.2, 75.7, 75.6 vhigh cor cost less than and edu > 25


# =============================================================================================================
# soc_econ: rsqr: .083, Sig: yr_edu, div, age25_65, pct_female
# soc_econ + hood: rsqr: .297, Sig: yr_edu, age25_65, pop_den, e_daypop, fam_rt, hu_own, vot_dem, grn_trav, hVIF: avg_inc, yr_edu
# soc_econ + hood + geo: rsqr: .296, Sig: yr_edu, age25_65, non_tech, pop_den, e_daypop, fam_rt, hu_own, vot_dem, grn_trav  hVIF: avg_inc, yr_edu
# soc_econ + hood + geo + ince: rsqr: .297, Sig: div, age25_65, non_tech, pop_den, e_daypop, fam_rt, hu_own, vot_dem, grn_trav   hVIF: avg_inc, yr_edu
#
# --------------------------------------------------------------------------------------------------------------
# Soc_econ: 										A: 63.7% NA:71.3% Acc: 67.9 high VIF:none
# Soc_econ + Hood: 									A: 71.9% NA:76.8% Acc: 74.6 high VIF: avg_inc=5.23, yr_edu=4.97
# Soc_econ + Hood + geo_climate: 					A: 72.9% NA:79.2% Acc: 76.4% high VIF: avg_inc=5.25, yr_edu=4.98
# Soc_econ + Hood + geo_climate + incentives: 		A: 72.6% NA:79.8% Acc:76.5%  high VIF: avg_inc=5.25, yr_edu=5.00
blocks4 = [soc_econA, hood, geo_climate, incent]  #
# =============================================================================================================

# =============================================================================================================
# soc_econ: rsqr: .083, Sig:
# soc_econ + hood: rsqr: .303, Sig: avg_inc, age25_65, pop_den, e_daypop, fam_rt, since_80, vot_dem, green_trv Sig: hVIF:a_inc, yr_edu
# soc_econ + hood + geo: rsqr: .302, Sig: yr_edu, 25-65, pop_den, e_daypop, fam_rt, since_80, vot_gop,   hVIF:a_inc, yr_edu
# soc_econ + hood + geo + ince: rsqr: .304 Sig: yr_edu, 25-65, pop_den, e_daypop, fam_rt, since_80, vot_gop,   hVIF:a_inc, yr_edu
#
# --------------------------------------------------------------------------------------------------------------
# Soc_econ: 										A: 63.7% NA: 71.3% Acc: 67.9 high VIF:
# Soc_econ + Hood: 									A: 70.6% NA: 78.4% Acc: 74.9 high VIF: avg_inc, yr_edu
# Soc_econ + Hood + geo_climate: 					A: 72.1% NA: 79.6% Acc: 76.2%  high VIF: avg_inc, yr_edu
# Soc_econ + Hood + geo_climate + incentives: 		A: 72.3% NA: 79.9% Acc: 76.5%  high VIF: avg_inc, yr_edu
blocks5 = [soc_econA, hoodA, geo_climate, incent] #
# =============================================================================================================

# =============================================================================================================
# soc_econ: rsqr: .083, Sig: yr_edu, div, age25_65, pct_female see above
# soc_econ + hood: rsqr: , Sig: hVIF:
# soc_econ + hood + geo: rsqr: Sig:  hVIF:
# soc_econ + hood + geo + ince: rsqr: Sig: hVIF:
#
# --------------------------------------------------------------------------------------------------------------
# Soc_econ: 										A: % NA: % Acc:  high VIF:
# Soc_econ + Hood: 									A: % NA: % Acc:  high VIF:
# Soc_econ + Hood + geo_climate: 					A: % NA:% Acc:%  high VIF:
# Soc_econ + Hood + geo_climate + incentives: 		A: % NA:% Acc:%  high VIF:
blocks6 = [soc_econA, hoodB, geo_climate, incent] #

# =============================================================================================================
# soc_econ: rsqr: , Sig:
# soc_econ + hood: rsqr: , Sig: hVIF:
# soc_econ + hood + geo: rsqr: Sig:  hVIF:
# soc_econ + hood + geo + ince: rsqr: Sig: hVIF:
#
# --------------------------------------------------------------------------------------------------------------
# Soc_econ: 										A: % NA: % Acc:  high VIF:
# Soc_econ + Hood: 									A: % NA: % Acc:  high VIF:
# Soc_econ + Hood + geo_climate: 					A: % NA:% Acc:%  high VIF:
# Soc_econ + Hood + geo_climate + incentives: 		A: % NA:% Acc:%  high VIF:
blocks7 = [soc_econB, hood, geo_climate, incent]

# =============================================================================================================
# soc_econ: rsqr: , Sig:
# soc_econ + hood: rsqr: , Sig: hVIF:
# soc_econ + hood + geo: rsqr: Sig:  hVIF:
# soc_econ + hood + geo + ince: rsqr: Sig: hVIF:
#
# --------------------------------------------------------------------------------------------------------------
# Soc_econ: 										A: % NA: % Acc:  high VIF:
# Soc_econ + Hood: 									A: % NA: % Acc:  high VIF:
# Soc_econ + Hood + geo_climate: 					A: % NA:% Acc:%  high VIF:
# Soc_econ + Hood + geo_climate + incentives: 		A: % NA:% Acc:%  high VIF:
blocks8 = [soc_econB, hoodA, geo_climate, incent]



# =============================================================================================================
# soc_econ: rsqr: , Sig:
# soc_econ + hood: rsqr: , Sig: hVIF:
# soc_econ + hood + geo: rsqr: Sig:  hVIF:
# soc_econ + hood + geo + ince: rsqr: Sig: hVIF:
#
# --------------------------------------------------------------------------------------------------------------
# Soc_econ: 										A: % NA: % Acc:  high VIF:
# Soc_econ + Hood: 									A: % NA: % Acc:  high VIF:
# Soc_econ + Hood + geo_climate: 					A: % NA:% Acc:%  high VIF:
# Soc_econ + Hood + geo_climate + incentives: 		A: % NA:% Acc:%  high VIF:
blocks9 = [soc_econB, hoodB, geo_climate, incent]


deplr = ["number_of_solar_system_per_household"]
deplgr = ["A_o_NA"]

test_data[deplgr] = test_data[deplgr] - 1
#print(test_data[deplgr])

#nrmz = True
nrmz = False
blocks = blocks6
Hlinear_regression(adopter_data, deplr, blocks, verbose=False, normalize=nrmz)
print('\n\nNow for the logistic regression\n\n')
Hlogistic_regression(test_data, deplgr, blocks, verbose=False, normalize=nrmz)
#plt.show()