import numpy as np
import pandas as pd
from Deep_Solar_aid import *

file = DeepSolar_excel
options =[mean, std, median]
sel = 1
option = options[sel]

#attrib = PV_res
#attrib =PV_per_house
attrib = PV_area_res

_message = 'The {:s} for the attribute {:s} is {:.2f}'


def pm(message):
    print(message)

if option == mean:
    print('Mean:')
    val = pd.read_excel(DeepSolar_excel, usecols=[attrib]).mean()
    pm(_message.format(option, attrib, val[attrib]))
elif option == std:
    print('Standard Deviation:')
    val = pd.read_excel(DeepSolar_excel, usecols=[attrib]).std()[attrib]
    pm(_message.format(option, attrib, val))
elif option == median:
    print('Median:')
    val = pd.read_excel(DeepSolar_excel, usecols=[attrib]).median()[attrib]
    pm(_message.format(option,attrib, val))
