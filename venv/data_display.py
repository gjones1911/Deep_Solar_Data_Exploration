import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
#from sklearn.preprocessing import MinMaxScaler as minmaxscale
from sklearn.preprocessing import minmax_scale as minmaxscale
from sklearn.metrics import confusion_matrix
import statsmodels.api as sm
import statsmodels.discrete.discrete_model as dis_mod
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor as VIF
import sys
pd.options.mode.use_inf_as_na = True

def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    #classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    #print(cm)
    adoption_acc = cm[0][0]/(cm[0][0] + cm[0][1])
    non_adopt_acc = cm[1][1]/(cm[1][0] + cm[1][1])
    overall_acc = (cm[1][1]+cm[0][0])/(cm[1][0] + cm[1][1] + cm[0][0] + cm[0][1])
    print('Adoption Accuracy: {:f}'.format(adoption_acc))
    print('Non Adoption Accuracy: {:f}'.format(non_adopt_acc))
    print('Overall Accuracy: {:f}'.format(overall_acc))
    title = 'Adoption:{:f}, Non: {:f}, Overall:{:f}'.format(adoption_acc, non_adopt_acc, overall_acc)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax

def show_labeled_list(x, labels):
    for l,label in zip(x, labels):
        print('{:s}: {:f}'.format(label, l))
    return


def calculate_log_like(attribs, params):
    #attribs.append('const')
    l = []
    for attrib in attribs:
        l.append(params[attrib])
    return np.exp(l).tolist()

def find_significant(x,pvals):
    cnt = -1
    for e in pvals:
        if cnt > -1:
            print(x[cnt], ":", np.around(e,4))
        cnt += 1


def fix_dataset(dataset, option=1):
    if option == 1:
        dataset.replace(-999, np.NaN)
        return dataset.dropna(axis=0)



def h_regression(dataset, ysets, xsets):

    blocks = list()
    #dataset = fix_dataset(dset[ysets+xsets[0]])
    for y in ysets:
        print('##############################################################################')
        print('\t\t\t\t\t\t',y)
        print('##############################################################################')
        cnt = 0
        for x in xsets:
            blocks += x
            # my method up above to take care of missing or unusable values
            dmodel  = fix_dataset(dataset[[y]+blocks])
            Y = dmodel[y]
            print()
            print()
            print('################################################################################')
            print('#####################################     Block {:d}'.format(cnt+1))
            print('################################################################################')
            print('\t\tX', x)
            print('################################################################################')
            print('################################################################################')
            print('################################################################################')
            print()
            X = dmodel[blocks]
            #print(X['per_capita_income'])
            #X.loc[:, 'per_capita_income'] = (dmodel['per_capita_income'].values - dmodel['per_capita_income'].mean())/dmodel['per_capita_income'].std()
            #print(X['per_capita_income'])
            #X = dataset.loc[:, x]
            X2 = sm.add_constant(X)
            est = sm.OLS(Y, X2)
            est2 = est.fit()
            print(est2.summary())
            cnt += 1
            print()
            print()
    return

def calculate_vif (x):
    return pd.Series([VIF(x.values, i)
                      for i in range(x.shape[1])],
                      index=x.columns)


# performs some for of regression
# either linear or logistic
def analyze_data(dataset, ysets, xsets, type='LinR', normalize=False):
    #dataset = fix_dataset(dset[ysets+xsets[0]])
    regre_type = ''
    if type == 'LinR':
        regre_type = 'Linear Regression'
    elif type == 'LogR':
        regre_type = 'Logistic Regression'
    else:
        print('Error Unknown regression method {:s}'.format(type))
        quit()
    old_rsqr = 0
    old_fstat = 10e20
    del_rsqr = 0
    del_fstat = 0
    num_sig = 0
    for y in ysets:
        print('##############################################################################')
        print('\t\t\t\t\t\t',y)
        print('##############################################################################')
        cnt = 0
        for x in xsets:
            # my method up above to take care of missing or unusable values
            dmodel  = fix_dataset(dataset[[y]+x])
            Y = dmodel[y]
            print()
            print()
            print('################################################################################')
            print('#####################################    Testing x set {:d}'.format(cnt+1))
            print('#####################################    Using {:s} on dependent variable {:s}'.format(regre_type, y))
            print('################################################################################')
            print('\t\tX or dependent variables:\n', x)
            print('################################################################################')
            print('################################################################################')
            print('################################################################################')
            print()
            X = dmodel[x]
            #print('+++++++++++++++++++++++++++++++++++++++++Before: ', X[0,0])
            if normalize:
                #X = pd.DataFrame(minmaxscale(X, axis=1), columns=x)
                X = pd.DataFrame(minmaxscale(X, axis=0), columns=x, index=dmodel.index)
            #print('+++++++++++++++++++++++++++++++++++++++++After: ', X.iloc[0,0])
            #print(X['per_capita_income'])
            #X.loc[:, 'per_capita_income'] = (dmodel['per_capita_income'].values - dmodel['per_capita_income'].mean())/dmodel['per_capita_income'].std()
            #print(X['per_capita_income'])
            #X = dataset.loc[:, x]
            X2 = sm.add_constant(X)
            if type == 'LinR':
                est = sm.OLS(Y, X2)
                print('\n\nThe basic dirs are\n', dir(est))
                est2 = est.fit()
                print('\n\nThe fitted dirs are\n', dir(est2))
                rsqr = est2.rsquared
                if rsqr > old_rsqr:
                    old_rsqr = rsqr
                pvals = est2.pvalues
                fval = est2.fvalue
                ftest = est2.f_test
                print('R-squared:',rsqr)
                print('P-values:\n', pvals)
                find_significant(x, pvals)
                print('Fvalue\n',fval)
                print(est2.summary())
                print('\n\nThe summary dirs are:\n',dir(est2.summary()))
                vif = calculate_vif(X2)
                print('VIF:\n', vif)
            elif type == 'LogR':
                #clf = LogisticRegression(solver='lbfgs',max_iter=1000).fit(X2, Y)
                #params = clf.coef_
                #log_like = np.log(np.abs(params))
                #print(params)
                #print(log_like)
                model = dis_mod.Logit(Y, X2)
                model2 = model.fit()
                loglikly= calculate_log_like(x, model2.params)
                print(dir(model))
                print(model.df_model)
                print(model2.summary())
                print('model 2',dir(model2))
                print('R squared:', model2.prsquared)
                #print(dir(model2.summary().tables))
                print('The log likelyhoods are:')
                show_labeled_list(loglikly, x)
                print('pvalue for {:s}: {:f}'.format(x[0], model2.pvalues.loc[x[0]]))
                y_pred = model2.predict(X2, linear=True)
                #print(y_pred)
                yp = list()
                for e in y_pred:
                    if e > 0:
                        yp.append(1)
                    else:
                        yp.append(0)
                #print(model.loglikeobs(x))
                #df_confusion = pd.crosstab(Y, y_pred, rownames=['Actual'], colnames=['Predicted'], margins=True)
                plot_confusion_matrix(Y, yp, classes=['A', 'NA'],
                                      title='Confusion matrix, without normalization')
                #plot_confusion_matrix(df_confusion)
                #vif = pd.Series([VIF(X2.values, i)
                #           for i in range(X2.shape[1])],
                #          index=X2.columns)
                vif = calculate_vif(X2)
                print('VIF:\n',vif)
                plt.show()
            cnt += 1
            print()
            print()
    return

def display_percentages(all, adopters, non, high, low, area='TN' ):
    print('Thera are a total of {:d} census tracts in the {:s} area.'.format(all, area))
    print('Of these {:d} census tracts:'.format(all))
    print('\t* {:d} or {:.2f}% have some level of adoption.'.format(adopters, 100* adopters/all))
    print('\t* {:d} or {:.2f}% are non-adopting.'.format(non, 100* non/all))
    print('\t* {:d} or {:.2f}% have a high (> 10) level of adoption.'.format(high, 100* high/all))
    print('\t* {:d} or {:.2f}% have a low (<10, >1) level of adoption.'.format(low, 100* low/all))
    print()
    return

def fancy_scatter_plot(x, y, styl, title, c, xlabel, ylabel, labels, legend,
                               annotate=True, s=.5, show=False):

        for z1, z2, label in zip(x, y, labels):
            plt.scatter(z1, z2, s=s, c=c)
            if annote:
                plt.annotate(label, (z1, z2))

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        leg = plt.legend([legend], loc='best', borderpad=0.3,
                         shadow=False, prop=matplotlib.font_manager.FontProperties(size='small'),
                         markerscale=0.4)
        leg.get_frame().set_alpha(0.4)
        leg.draggable(state=True)

        if show:
            plt.show()

def multi_scatter(xary, yary, titles, cary, xlabels, ylabels, labels, legend, annotate=True,
                  s=.5, show=False):

    for x, y, title, xl, yl, l, lg in zip(xary, yary, titles, xlabels, ylabels, labels, legend):
        fancy_scatter_plot(x, y, styl, title, c, xlabel, ylabel, labels, legend)


def make_pie(percentages, explode='', title='Title', ltitle='legend', autopct='%1.1f%%', shadow=False,
             loc='center left', bbox_to_anchor=(-1,-1,.5,1), use_legend=False, show=False):
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


def multi_pie(percentages, explode, titles, ltitles, autopct='%1.1f%%', shadow=False,
              loc='center left', bbox_to_anchor=(0,0,.5,1), use_legend=False, show=False):
    for percentage, title, ltitle in zip(percentages, titles):
        make_pie(percentage, explode=explode, title=title, ltitle=ltitle, autopct=autopct, shadow=shadow,
                 loc=loc, bbox_to_anchor=bbox_to_anchor, use_legend=use_legend, show=show)


def make_bar(x, w=.08, b=0, align='center', label='label', yl='Y', xl='X', title='Title', show=False,
             xticklabels=(), color=['r']):
    if len(xticklabels) == 0:
        xticklabels = []
        for i in range(len(x)):
            xticklabels.append('X{:d}'.format(i + 1))
        xticklabels = tuple(xticklabels)

    ind = np.arange(len(x))
    fig, ax = plt.subplots()
    xs = ind - w / 2
    rect1 = ax.bar(xs, x, w, label=label, align=align)

    ax.set_title(title)
    ax.set_ylabel(yl)
    ax.set_xticks(ind)
    ax.set_xticklabels(xticklabels)
    ax.legend()

    if show:
        plt.show()


def multi_bar(xary, w, b, align, labels, yls, xls, titles, show=False,
             xticklabels=()):
    for x, label, yl, xl, title in zip(xary, labels, yls, xls, titles):
        make_bar(x, w=w, b=b, align=align, label=label, yl=yl, xl=xl, title=title, show=show, xticklabels=xticklabels)


def fit_models(dataset, ysets, xsets):
    models = dict()
    for y in ysets:
        models[y] = dict()

        for x in xset:
            # store the model fitted to curent x with the key as the current x and the fitte
            models[y]['model'] = LinearRegression().fit(dataset.loc[:, x].values, dataset[y].values)
    return models


def score_models(models, ysets, verbose=False):
    for y in ysets:
        models[y]['model'].score()

def linear_regression(dataset, split_val, ysets, xsets, verbose=False):

    # go through the selected y's and x's fitting a set of models
    models = fit_models(dataset=dataset, ysets=ysets, xsets=xsets)
