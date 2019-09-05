#import GJ_Utils.Data_Explorer
from GJ_Utils.Data_Explorer.Data_Explorer import *
from GJ_Utils.util import *
from Deep_Solar_aid import *
import matplotlib.pyplot as plt

DeepSolarTN_excel = r'C:\Users\Candice\Desktop\research_stuff\DataSpreadSheets\TNDS.xlsx'

cols = [PV_res]

de = Data_Explorer(DeepSolarTN_excel)
#de.display_attribs(vec_prnt=True)

de.display_stat(de.average, ['solar_system_count'])
de.display_stat(de.average, ['solar_system_count_residential'])
de.display_stat(de.average, ['total_panel_area_residential'])
#de.display_stat(de.max, ['solar_panel_area_divided_by_area'])
de.display_stat(de.average, ['solar_panel_area_divided_by_area'])
de.display_stat(de.average, [PV_per_house])
#print("Head of sorted:\n", de.sort(cols, ascending=False).loc[:, ['fips', PV_res, 'county']].head(5))
#print('Max values:\n',de.attrib_max)
print()
high = de.grab_sub_set(PV_res, 'g', 9)
highPct = high.shape[0]/de.df.shape[0]
havg = high[PV_res].mean()
htot = high[PV_res].sum()
print('There are {:d} high adoption areas based on pure PV numbers'.format(high.shape[0]))
print('These have a total of {:d} PV installations with an census tract average of {:f}'.format(htot, havg))
print('This is {:.2f}% of the TN census tracts'.format(100*(highPct)))
print()
moderate = de.grab_sub_set([PV_res,PV_res], 'cmpm&', [9, 1])
modPct = moderate.shape[0]/de.df.shape[0]
mavg = moderate[PV_res].mean()
mtot = moderate[PV_res].sum()
print('There are {:d} moderate adopting census tracts.'.format(moderate.shape[0]))
print('These have a total of {:d} PV installations with an census tract average of {:f}'.format(mtot, mavg))
print('This is {:.2f}% of the TN census tracts'.format(100*(modPct)))
print()
non = de.grab_sub_set(PV_res, 'l', 1)
nonPct = non.shape[0]/de.df.shape[0]
navg = non[PV_res].mean()
ntot = non[PV_res].sum()
print('There are {:} non adopting census tracts.'.format(non.shape[0]))
print('These have a total of {:d} PV installations with an census tract average of {:f}'.format(ntot, navg))
print('This is {:.2f}% of the TN census tracts'.format(100*(nonPct)))
print()

print('')

total_adoption = sum(high[PV_res].tolist()) + sum(moderate[PV_res].tolist())
avg_adopt = total_adoption/(high.shape[0]+moderate.shape[0])
print('Among PV adopting census tracts there are a total of {:d} PV\'s'.format(total_adoption),'\n',
      'With an average of {:f} per census tract.'.format(avg_adopt))

percentages = {'High Adopting ( >= 10)':highPct,
               'Moderate Adopting (1 >= PV < 10)':modPct,
               'Non Adopting':nonPct}

'''
fig1, ax1 = plt.subplots()

explode = [0,0,0]

wedges, texts, autotexts = ax1.pie(list(percentages.values()), labels=list(percentages.keys()), explode=explode,
                                   autopct='%1.1f%%', shadow=True)

# ax1.legend(wedges, list(percentages.keys()), title='Level of Adoption', loc='center left')

plt.setp(autotexts, size=8, weight='bold')

ax1.set_title('Title')
'''
ltitle='Adoption level'
title = 'Percentages of Adoptions levels in TN census tracts'

show=False

de.make_pie(percentages, explode='', title=title, ltitle=ltitle, autopct='%1.1f%%', shadow=False,
                 loc='center left', bbox_to_anchor=(0,0,.5,1), use_legend=True, show=show)


x = [high[PV_res].mean(), moderate[PV_res].mean()]
btitle = 'PV averages across adoption levels'
pv_xtick = ('High', 'Moderate')
de.make_bar(x, w=.08, b=0, align='center', label='Level of PV adoption', yl='PV numbers',
            xl='Level of PV adoption', title=btitle, show=show, xticklabels=pv_xtick)


x_inc = [high[avg_inc].mean(), moderate[avg_inc].mean(), non[avg_inc].mean()]
inc_btitle = 'PV adoption Annual Mean Income '
inc_xticks = ('High', 'Moderate', 'None')
de.make_bar(x_inc, w=.08, b=0, align='center', label='Average Annual Income across various levels of Adoption', yl='Average income',
            xl='Level of PV adoption', title=inc_btitle, show=show, xticklabels=inc_xticks)


#attribx, attriby = house_val, PV_res
attribx, attriby = house_val, PV_area_by_area

hvx = high[attribx].mean()
mvx = moderate[attribx].mean()
nvx = non[attribx].mean()

hvy = high[attriby].mean()
mvy = moderate[attriby].mean()
nvy = non[attriby].mean()


xvals = [hvx, mvx, nvx]
yvals = [hvy, mvy, nvy]

colors = [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]]

markers = ['o']

x_label = '{:s}'.format(attribx)
y_label = '{:s}'.format(attriby)

ations=['High', 'Moderate', 'Non-adopting']

title = '{:s} vs. {:s}'.format(attribx, attriby)

de.make_scatter(xvals, yvals, colors, markers=markers, verbose=False, annote=True, ations=ations, title=title,
                     x_label=x_label, y_label=y_label, show=False, line=True)


if not show:
    plt.show()