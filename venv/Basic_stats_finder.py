import data_display as dd
import numpy as np
import pandas as pd
import statsmodels as sm
from Deep_Solar_aid import *
from GJ_Utils.util import show_list

# a collection of states to look at:
sought_st = ['TN','AL','FL','GA','KY', 'MS','NC', 'SC', 'WV']
f_type = ['St', 'adopters', 'nonadopters']
st_pth = None
#create a set of file paths to look for
for st in sought_st:
    if st_pth is None:
        st_pth = get_file_path(st, f_type)
    else:
        st_pth += get_file_path(st, f_type)


print('Created File path: ', st_pth)

#folders = [r'\TN\TNadopters.xlsx', r'\AL\ALadopters.xlsx', r'\GA', r'\NC', r'\MS', r'\WV', r'\SC', r'\KY']
folders = [r'\TN\TNDeep_Solar.xlsx' ,r'\TN\TN_adopt_Deep_solar.xlsx', r'\TN\TN_nonadopt_Deep_Solar.xlsx']
#states = ['TN', 'TN_adopters', 'TN_nonadopters']
states = make_state_labels(sought_st)
print('The States?\n', states)
folders = st_pth

attribs = demo_attribs

new_file = '\TVA_comparision_Basic_Analysis.xlsx'
region = 'US'
output_file = output + new_file
#excel_file = output + region
excel_file = DeepSolar_excel
verbose=True
#state = [, ]
#rd = calculate_PV_stats(pd.read_excel(excel_file), verbose=True, state='US')
#store_stats(rd, output_file)

frd = {}
rd = {}
N = 1
for filef, st in zip(folders, states):
    print('File name: ', filef,'State:', st)
    #rd, frd = store_stats(calculate_stats(pd.read_excel(output + filef), frd, attribs, rd={}, verbose=False, state=st), rd)
    frd, N = calculate_stats(pd.read_excel(output_server + filef), frd, attribs, rd={}, verbose=False, state=st, N=N)
    print()
    print()


rd, frd = store_stats(frd, rd)
pd.DataFrame(rd ).to_excel(output_file, index=False)