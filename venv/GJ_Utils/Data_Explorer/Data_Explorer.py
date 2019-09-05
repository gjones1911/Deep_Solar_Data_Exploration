"""Purpose:    To allow for easy analysis of a data set
   Created by: Gerald Jones, Summer 2019
"""

#import sklearn
import matplotlib.pyplot as plt
import numpy  as np
import pandas as pd
from ..datadisplay import data_display as ddis
from ..IO import file_assistant as fa
from ..util import *

class Data_Explorer:

    average = 'avg'
    std = 'std'
    median = 'med'
    var = 'var'
    max = 'max'
    min = 'min'
    dsum = 'sum'

    def __init__(self, data=None, df=None, name='', cls=[]):
        if data is not None:
            self.name = data
            self.df = self.get_data(data)
        else:
            self.name=name
            self.df = df
        self.N = self.df.shape[0]
        self.d = self.df.shape[1]
        self.nrows = self.df.shape[0]
        self.ncols = self.df.shape[1]
        self.attribs = self.df.columns.tolist()
        self.indices = self.df.index.tolist()
        self.attrib_avg = self.df.mean(axis=0).tolist()
        self.attrib_std = self.df.std(axis=0).tolist()
        self.attrib_med = self.df.median(axis=0) .tolist()
        self.attrib_max = self.df.max().tolist()
        self.attrib_min = self.df.min().tolist()
        self.Classes = cls

    # creates and returns the dataframe from given file name (data)
    def get_data(self, data, index=0, usecols=''):
        return fa.file_assistant(data).Process_DataFrame()

    def display_stat(self, stat, attribs, thresh=None):
        for attrib in attribs:
            val = self.process_stat_request(stat, attrib, thresh)
            print('The {:s} is {:s} for {:s}'.format(stat, str(val), attrib))

    def display_stranger_stat(self, df, stat, attribs, thresh=None):
        for attrib in attribs:
            val = self.process_stranger_stat_request(df, stat, attrib, attribs, thresh)
            print('The {:s} is {:s} for {:s}'.format(stat, str(val), attrib))

    def process_stranger_stat_request(self, df, stat, attrib, attribs, thresh):
        if attrib not in attribs:
            print('Sought attribute {:s} not found'.format(attrib))
            quit(-98)
        if stat == self.average:
            return df[attrib].mean()
        elif stat == self.std:
            return df[attrib].std()
        elif stat == self.median:
            return df[attrib].median()
        elif stat == self.max:
            return df[attrib].max()
            #return self.max[attrib]
        elif stat == self.min:
            return df[attrib].min()

    def process_stat_request(self, stat, attrib, thresh):
        if attrib not in self.attribs:
            print('Sought attribute {:s} not found'.format(attrib))
            quit(-98)
        if stat == self.average:
            return self.attrib_avg[self.attribs.index(attrib)]
        elif stat == self.std:
            return self.attrib_std[self.attribs.index(attrib)]
        elif stat == self.median:
            return self.attrib_med[self.attribs.index(attrib)]
        elif stat == self.max:
            return self.max[self.attribs.index(attrib)]
            #return self.max[attrib]
        elif stat == self.min:
            return self.min[self.attribs.index(attrib)]

    def grab_sub_set(self, attrib, cond, val, label='high'):
        if cond == 'g':
            return self.df.loc[self.df[attrib] > val]
        elif cond == 'l':
            return self.df.loc[self.df[attrib] < val]
        elif cond == 'cmpm&':
            return self.complex_subset(attrib, cond, val)
        else:
            print('unknown command: {:s}'.format(cond))
            quit(-78)

    def complex_subset(self, attribs, conds, vals):
        if len(attribs) != len(vals):
            print('attrib, vals must have same length')
            quit(-90)
        if len(attribs) == 2:
            if conds == 'cmpm&':
                return self.df.loc[(self.df[attribs[0]] <= vals[0]) & (self.df[attribs[1]] >= vals[1])]
        elif len(attribs) == 3:
            pass
        elif len(attribs) == 4:
            pass
        elif len(attribs) == 5:
            pass
        elif len(attribs) == 6:
            pass
        return

    def display_attribs(self, numbered=True, vec_prnt=False):
        show_list(self.attribs, numbered=numbered, vec_prnt=vec_prnt)


    def sort(self, scols, ascending = False, na_pos='last'):
        return self.df.sort_values(by=scols, ascending=ascending, na_position= na_pos)


    def make_pie(self, percentages, explode='', title='Title', ltitle='legend', autopct='%1.1f%%', shadow=False,
                 loc='center left', bbox_to_anchor=(0,0,.5,1), use_legend=False, show=False):
        fig1, ax1 = plt.subplots()
        if len(explode) == 0:
            explode = []
            for i in range(len(percentages)):
                explode.append(0)
        wedges, texts, autotexts = ax1.pie(list(percentages.values()), labels=list(percentages.keys()), explode=explode,
                                           autopct=autopct, shadow=shadow)

        if use_legend:
            ax1.legend(wedges, list(percentages.keys()), title=ltitle, loc=loc, bbox_to_anchor=bbox_to_anchor)

        plt.setp(autotexts, size=14, weight='bold')

        ax1.set_title(title)

        if show:
            plt.show()


    def make_bar(self, x, w=.08, b=0, align='center', label='label', yl='Y', xl='X', title='Title', show=False,
                 xticklabels=()):
        if len(xticklabels) == 0:
            xticklabels = []
            for i in range(len(x)):
                xticklabels.append('X{:d}'.format(i+1))
            xticklabels = tuple(xticklabels)

        ind = np.arange(len(x))
        fig, ax = plt.subplots()
        xs = ind - w/2
        rect1 = ax.bar(xs, x, w, label=label)

        ax.set_title(title)
        ax.set_ylabel(yl)
        ax.set_xticks(ind)
        ax.set_xticklabels(xticklabels)
        ax.legend()

        if show:
            plt.show()

    def make_multi_bar(self, xar, h, w=.08, b=0, align='center'):
        pass

    def make_scatter(self, x, y, colors, markers=('o-'), verbose=False, annote=False, ations=[], title='Title',
                     x_label='x labels', y_label='y labels', show=False, line=False):

        markers_s = list(['o', '^', 's', '*'])

        fig = plt.figure(figsize=(8, 5))
        ax = fig.add_subplot(111)

        idx = 0
        clim = len(colors)

        i = 0
        mlim = len(markers)
        alim = len(ations)

        for xi, yi in zip(x,y):
            ax.scatter(xi, yi, s=20, c=[colors[idx%clim]], marker=markers[i%mlim])
            if annote:
                ax.annotate(ations[i%alim], (xi, yi))
            i += 1
            idx += 1
        if line:
            ax.plot(x,y)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        if show:
            plt.show()