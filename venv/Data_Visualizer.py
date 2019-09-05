import numpy as np
import pandas as pd
from data_display import *
from Deep_Solar_aid import *
from GJ_Utils.util import *

excel_file = DeepSolarTN_excel
current_state = 'TN'
current_state = current_state.lower()
hthresh = 10
lthresh = 1
midrange = [1,9]
bar = True
pie = True
line = True


apt = ''
hapt = ''
mapt = ''
nonapt = ''

# will be used as y values, usually some form of PV information
bary = []       # adopters
cary = []       # non adopters
dary = []       # high adopters
eary = []       # low adopters

# will be used as x values attribues thought to contribute to PV adoptions usually
barx = []       # adopters
carx = []       # non adopters
darx = []       # High adopters
earx = []       # low adopters


# grab all the data you need and store it for plotting later
#USDS = pd.read_excel(DeepSolar_excel)
TNDS = pd.read_excel(excel_file)

N = TNDS.shape[0]

print(TNDS.columns.tolist())

path = complete_path(output, TN_sheet)

adopters, high, low, non = split_data_res_adopt_non(TNDS, hthr=hthresh, midrange=[1,10], lthr=lthresh, verbose=False)

#######################################################################################################
#######################################################################################################
#######################################################################################################
#########################              Adopters                ########################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
adp_cnt = adopters.shape[0]
adp_pct = adp_cnt/N

# residential PV's
apt_sum_PVres = adopters[pv_attribs.PV_res].sum()
apt_avg_PVres = adopters[pv_attribs.PV_res].mean()
apt_std_PVres = adopters[pv_attribs.PV_res].std()
PVreslist = [apt_avg_PVres]
bary += PVreslist

# PV by area
apt_sum_PV_a_a = adopters[pv_attribs.PV_area_by_area].sum()
apt_avg_PV_a_a = adopters[pv_attribs.PV_area_by_area].mean()
apt_std_PV_a_a = adopters[pv_attribs.PV_area_by_area].std()
PVareaStuff = [apt_avg_PV_a_a]
bary += PVareaStuff


# PV residential by area
apt_PVres_a_a = adopters[pv_attribs.PV_area_res ].sum()/adopters[geo.land_area].sum()
apt_PVres_a_a_avg = adopters[pv_attribs.PV_area_res ].mean()/adopters[geo.land_area].sum()
apt_PVres_a_avg = adopters[pv_attribs.PV_area_res ].mean()
bary += [apt_PVres_a_a, apt_PVres_a_a_avg, apt_PVres_a_avg]

# education
avg_col = adopters[education.edu_C].mean()
avg_hs = adopters[education.edu_HS].mean()
avg_lhs = adopters[education.edu_LHS].mean()
avg_edu_pop = adopters[education.edu_pop].mean()
avg_edu_yrs = adopters[education.edu_yrs].mean()
educa = [avg_col, avg_hs, avg_lhs, avg_edu_pop, avg_edu_yrs]
barx += educa


# housing
avg_house_size = adopters[housing.avg_house_size].mean()
avg_house_value = adopters[housing.house_val].mean()
avg_mortgage = adopters[housing.mortgage_r].mean()
avg_owner = adopters[housing.owner_r].mean()
houses = [avg_house_size, avg_house_value, avg_mortgage, avg_owner]
barx += houses

# income
avg_income = [adopters[income.avg_inc].mean()]
barx += avg_income

#politics
dem_16 = adopters[political.dem16].mean()
gop_16 = adopters[political.gop16].mean()
polys = [dem_16, gop_16]
barx += polys


# age
med_age = adopters[age.med_age].mean()
age1824 = adopters[age.age1824].mean()
age2534 = adopters[age.age2534].mean()
age3544 = adopters[age.age3544].mean()
age4554 = adopters[age.age4554].mean()
age5564 = adopters[age.age5564] .mean()
age6574 = adopters[age.age6574].mean()
age7584 = adopters[age.age7584].mean()
age85p = adopters[age.age85p].mean()
ages = [med_age, age1824, age2534, age3544, age4554, age5564, age6574, age7584, age85p]
barx += ages


# pop
avg_pop = adopters[population.pop].mean()
avg_pop_den = adopters[population.pop_den].mean()
popu = [avg_pop, avg_pop_den]
barx += popu

# pov
avg_pov = [adopters[poverty.pov_cnt].mean()]
barx += avg_pov

#######################################################################################################
#######################################################################################################
#######################################################################################################
#########################              Non adopters            ########################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
nadp_cnt = non.shape[0]
nadp_pct = nadp_cnt/N

# residential PV's
napt_sum_PVres = non[pv_attribs.PV_res].sum()
napt_avg_PVres = non[pv_attribs.PV_res].mean()
napt_std_PVres = non[pv_attribs.PV_res].std()
nPVreslist = [napt_avg_PVres]
cary += nPVreslist

# PV by area
napt_sum_PV_a_a = non[pv_attribs.PV_area_by_area].sum()
napt_avg_PV_a_a = non[pv_attribs.PV_area_by_area].mean()
napt_std_PV_a_a = non[pv_attribs.PV_area_by_area].std()
nPVareaStuff = [napt_avg_PV_a_a]
cary += nPVareaStuff

# PV residential by area
napt_PVres_a_a = non[pv_attribs.PV_area_res ].sum()/non[geo.land_area].sum()
napt_PVres_a_a_avg = non[pv_attribs.PV_area_res ].mean()/non[geo.land_area].sum()
napt_PVres_a_avg = non[pv_attribs.PV_area_res ].mean()
cary += [napt_PVres_a_a, napt_PVres_a_a_avg, napt_PVres_a_avg]

# education
navg_col = non[education.edu_C].mean()
navg_hs = non[education.edu_HS].mean()
navg_lhs = non[education.edu_LHS].mean()
navg_edu_pop = non[education.edu_pop].mean()
navg_edu_yrs = non[education.edu_yrs].mean()
neduca = [navg_col, navg_hs, navg_lhs, navg_edu_pop, navg_edu_yrs]
carx += neduca


# housing
navg_house_size = non[housing.avg_house_size].mean()
navg_house_value = non[housing.house_val].mean()
navg_mortgage = non[housing.mortgage_r].mean()
navg_owner = non[housing.owner_r].mean()
nhouses = [navg_house_size, navg_house_value, navg_mortgage, navg_owner]
carx += nhouses

# income
navg_income = [non[income.avg_inc].mean()]
carx += navg_income

#politics
ndem_16 = non[political.dem16].mean()
ngop_16 = non[political.gop16].mean()
npolys = [ndem_16, ngop_16]
carx += npolys


# age
nmed_age = non[age.med_age].mean()
nage1824 = non[age.age1824].mean()
nage2534 = non[age.age2534].mean()
nage3544 = non[age.age3544].mean()
nage4554 = non[age.age4554].mean()
nage5564 = non[age.age5564] .mean()
nage6574 = non[age.age6574].mean()
nage7584 = non[age.age7584].mean()
nage85p = non[age.age85p].mean()
nages = [nmed_age, nage1824, nage2534, nage3544, nage4554, nage5564, nage6574, nage7584, nage85p]
carx += nages


# pop
navg_pop = non[population.pop].mean()
navg_pop_den = non[population.pop_den].mean()
npopu = [navg_pop, navg_pop_den]
carx += npopu

# pov
navg_pov = [non[poverty.pov_cnt].mean()]
carx += avg_pov

#######################################################################################################
#######################################################################################################
#######################################################################################################
#########################              High adopters            ########################################
#######################################################################################################
#######################################################################################################
#############################################p##########################################################
hadp_cnt = high.shape[0]
hadp_pct = hadp_cnt/N

# residential PV's
hapt_sum_PVres = high[pv_attribs.PV_res].sum()
hapt_avg_PVres = high[pv_attribs.PV_res].mean()
hapt_std_PVres = high[pv_attribs.PV_res].std()
hPVreslist = [hapt_avg_PVres]
dary += hPVreslist
high_labelsPV = ['Average Residental PV#\'s',
                 'Average PV area by land area',
                 'Residental PV area by land area', 'Average Residental PV area by avg land area',
                 'Average PV area by average land area']

# PV by area
hapt_sum_PV_a_a = high[pv_attribs.PV_area_by_area].sum()
hapt_avg_PV_a_a = high[pv_attribs.PV_area_by_area].mean()
hapt_std_PV_a_a = high[pv_attribs.PV_area_by_area].std()
hPVareaStuff = [hapt_avg_PV_a_a]
dary += hPVareaStuff

# PV residential by area
hapt_PVres_a_a = high[pv_attribs.PV_area_res ].sum()/high[geo.land_area].sum()
hapt_PVres_a_a_avg = high[pv_attribs.PV_area_res ].mean()/high[geo.land_area].mean()
hapt_PVres_a_avg = high[pv_attribs.PV_area_res ].mean()
dary += [hapt_PVres_a_a, hapt_PVres_a_a_avg, hapt_PVres_a_avg]


high_labelsx = ['Averge with College Education', 'Average with High School Education',
                'Average with less than High School Education', 'Average Number of people 25 or older',
                'Average Number of years of education']
# education
havg_col = high[education.edu_C].mean()
havg_hs = high[education.edu_HS].mean()
havg_lhs = high[education.edu_LHS].mean()
havg_edu_pop = high[education.edu_pop].mean()
havg_edu_yrs = high[education.edu_yrs].mean()
heduca = [havg_col, havg_hs, havg_lhs, havg_edu_pop, havg_edu_yrs]
darx += heduca

high_labelsx += ['Avergage House size', 'Average house value', 'Average Number of homes with a Mortgage',
                 'Average Number of Home owners', 'Average Ratio of family homes']
# housing
havg_house_size = high[housing.avg_house_size].mean()
havg_house_value = high[housing.house_val].mean()
havg_mortgage = high[housing.mortgage_r].mean()
havg_owner = high[housing.owner_r].mean()
havg_fam = high[housing.household_type_family_rate].mean()
hhouses = [havg_house_size, havg_house_value, havg_mortgage, havg_owner, havg_fam]
darx += hhouses

high_labelsx += ['Average Annual Income']
# income
havg_income = [high[income.avg_inc].mean()]
darx += havg_income

high_labelsx += ['Percentage of Democratic voters in 2016 election',
                 'Percentage of GOP voters in 2016 election']
#politics
hdem_16 = high[political.dem16].mean()
hgop_16 = high[political.gop16].mean()
hpolys = [hdem_16, hgop_16]
darx += hpolys


high_labelsx += ['Median Age', 'Average population between 18 and 24', 'Average population between 25 and 34',
                 'Average population between 35 and 44', 'Average population between 45 and 54',
                 'Average population between 55 and 64', 'Average population between 65 and 74',
                 'Average population between 75 and 84', 'Average population 85 and above']
# age
hmed_age = high[age.med_age].mean()
hage1824 = high[age.age1824].mean()
hage2534 = high[age.age2534].mean()
hage3544 = high[age.age3544].mean()
hage4554 = high[age.age4554].mean()
hage5564 = high[age.age5564] .mean()
hage6574 = high[age.age6574].mean()
hage7584 = high[age.age7584].mean()
hage85p = high[age.age85p].mean()
hages = [hmed_age, hage1824, hage2534, hage3544, hage4554, hage5564, hage6574, hage7584, hage85p]
darx += hages


high_labelsx += ['Average Poplulation', 'Average Population Density']

# pop
havg_pop = high[population.pop].mean()
havg_pop_den = high[population.pop_den].mean()
hpopu = [havg_pop, havg_pop_den]
darx += hpopu

high_labelsx += ['Average Number of families in poverty']
# pov
havg_pov = [high[poverty.pov_cnt].mean()]
darx += havg_pov

#######################################################################################################
#######################################################################################################
#######################################################################################################
#########################              Low high            ########################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
ladp_cnt = low.shape[0]
ladp_pct = ladp_cnt/N

# residential PV's
lapt_sum_PVres = low[pv_attribs.PV_res].sum()
lapt_avg_PVres = low[pv_attribs.PV_res].mean()
lapt_std_PVres = low[pv_attribs.PV_res].std()
lPVreslist = [lapt_avg_PVres]
eary += lPVreslist
low_labelsPV = ['Average Residental PV#\'s',
                 'Average PV area by land area',
                 'Residental PV area by land area', 'Average Residental PV area by avg land area',
                 'Average PV area by average land area']

# PV by area
lapt_sum_PV_a_a = low[pv_attribs.PV_area_by_area].sum()
lapt_avg_PV_a_a = low[pv_attribs.PV_area_by_area].mean()
lapt_std_PV_a_a = low[pv_attribs.PV_area_by_area].std()
lPVareaStuff = [lapt_avg_PV_a_a]
eary += lPVareaStuff

# PV residential by area
lapt_PVres_a_a = low[pv_attribs.PV_area_res ].sum()/low[geo.land_area].sum()
lapt_PVres_a_a_avg = low[pv_attribs.PV_area_res ].mean()/low[geo.land_area].mean()
lapt_PVres_a_avg = low[pv_attribs.PV_area_res ].mean()
eary += [lapt_PVres_a_a, hapt_PVres_a_a_avg, hapt_PVres_a_avg]


low_labelsx = ['Averge with College Education', 'Average with High School Education',
                'Average with less than High School Education', 'Average Number of people 25 or older',
                'Average Number of years of education']
# education
lavg_col = low[education.edu_C].mean()
lavg_hs = low[education.edu_HS].mean()
lavg_lhs = low[education.edu_LHS].mean()
lavg_edu_pop = low[education.edu_pop].mean()
lavg_edu_yrs = low[education.edu_yrs].mean()
leduca = [lavg_col, lavg_hs, lavg_lhs, lavg_edu_pop, lavg_edu_yrs]
earx += leduca

low_labelsx += ['Avergage House size', 'Average house value', 'Average Number of homes with a Mortgage',
                 'Average Number of Home owners', 'Average Ratio of family homes']
# housing
lavg_house_size = low[housing.avg_house_size].mean()
lavg_house_value = low[housing.house_val].mean()
lavg_mortgage = low[housing.mortgage_r].mean()
lavg_owner = low[housing.owner_r].mean()
lavg_fam = low[housing.household_type_family_rate].mean()
hhouses = [lavg_house_size, lavg_house_value, lavg_mortgage, lavg_owner, lavg_fam]
earx += hhouses

low_labelsx += ['Average Annual Income']
# income
lavg_income = [low[income.avg_inc].mean()]
earx += lavg_income

low_labelsx += ['Percentage of Democratic voters in 2016 election',
                 'Percentage of GOP voters in 2016 election']
#politics
ldem_16 = low[political.dem16].mean()
lgop_16 = low[political.gop16].mean()
lpolys = [hdem_16, hgop_16]
earx += hpolys


low_labelsx += ['Median Age', 'Average population between 18 and 24', 'Average population between 25 and 34',
                 'Average population between 35 and 44', 'Average population between 45 and 54',
                 'Average population between 55 and 64', 'Average population between 65 and 74',
                 'Average population between 75 and 84', 'Average population 85 and above']
# age
lmed_age = low[age.med_age].mean()
lage1824 = low[age.age1824].mean()
lage2534 = low[age.age2534].mean()
lage3544 = low[age.age3544].mean()
lage4554 = low[age.age4554].mean()
lage5564 = low[age.age5564] .mean()
lage6574 = low[age.age6574].mean()
lage7584 = low[age.age7584].mean()
lage85p = low[age.age85p].mean()
lages = [lmed_age, lage1824, lage2534, lage3544, lage4554, lage5564, lage6574, lage7584, lage85p]
earx += lages


low_labelsx += ['Average Poplulation', 'Average Population Density']

# pop
lavg_pop = low[population.pop].mean()
lavg_pop_den = low[population.pop_den].mean()
lpopu = [lavg_pop, lavg_pop_den]
earx += lpopu

low_labelsx += ['Average Number of families in poverty']
# pov
lavg_pov = [low[poverty.pov_cnt].mean()]
earx += lavg_pov



#######################################################################################################
#######################################################################################################

display_percentages(N, adp_cnt, nadp_cnt, hadp_cnt, ladp_cnt, current_state)


#xary = [nmed_age, lmed_age, hmed_age, med_age]
xary = [nage1824, lage1824, hage1824, age1824]
label='Average ratio of 18 to 24 year olds'
Title = 'Non Adoptors vs. Low, High and all Adoptors average ration of 18 to 24 year olds:'
xticklabels = ['Nonadopting', 'Moderate Adopting', 'High Adopting', 'Adopting']
make_bar(xary, w=.08, b=0, align='center', label=label, yl='Ratio of 25 to 34 year olds', xl='Level of Adoption', title=Title, show=False,
             xticklabels=xticklabels,)

#xary = [nmed_age, lmed_age, hmed_age, med_age]
xary = [nage2534, lage2534, hage2534, age2534]
label='Average ratio of 25 to 34 year olds'
Title = 'Non Adoptors vs. Low, High and all Adoptors average ration of 25 to 34 year olds:'
xticklabels = ['Nonadopting', 'Moderate Adopting', 'High Adopting', 'Adopting']
make_bar(xary, w=.08, b=0, align='center', label=label, yl='Ratio of 25 to 34 year olds', xl='Level of Adoption', title=Title, show=False,
             xticklabels=xticklabels,)


#xary = [nmed_age, lmed_age, hmed_age, med_age]
xary = [nage3544, lage3544, hage3544, age3544]
label='Average ratio of 35 to 44 year olds'
Title = 'Non Adoptors vs. Low, High and all Adoptors average ration of 35 to 44 year olds:'
xticklabels = ['Nonadopting', 'Moderate Adopting', 'High Adopting', 'Adopting']
make_bar(xary, w=.08, b=0, align='center', label=label, yl='Ratio of 35 to 44 year olds', xl='Level of Adoption', title=Title, show=False,
             xticklabels=xticklabels,)


#xary = [nmed_age, lmed_age, hmed_age, med_age]
xary = [nage4554, lage4554, hage4554, age4554]
label='Average ratio of 45 to 54 year olds'
Title = 'Non Adoptors vs. Low, High and all Adoptors average ration of 45 to 54 year olds:'
xticklabels = ['Nonadopting', 'Moderate Adopting', 'High Adopting', 'Adopting']
make_bar(xary, w=.08, b=0, align='center', label=label, yl='Ratio of 45 to 44 year olds', xl='Level of Adoption', title=Title, show=False,
             xticklabels=xticklabels,)




plt.show()


print()

#low.to_excel(path+apt)
#low.to_excel(path+lapt)
#mod.to_excel(path+mapt)
#low.to_excel(path+nolapt)
