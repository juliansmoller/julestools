import decimal
import datetime
import pandas as pd
import numpy as np
import os
import shutil
from matplotlib import pyplot as plt

# ============================================================ Basic stuff

def money(x,include_decimal=True):
    '''Convert a number to a properly formatted currency string, e.g. 1.234 => $1.23'''
    formatted = '${:,.2f}'.format(x) if include_decimal else '${:,.0f}'.format(x)
    formatted = f'-{formatted}' if x<0 else formatted
    return formatted
def space(x,n=30):
    '''Apply padding to a string such that the output string has a fixed length, e.g. 30 characters'''
    return str(x) + ' '*max(0,n-len(str(x)))
def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]
def get_one(values):
    '''Given a series of values, return the first one if all are the same'''
    return values.iloc[0] if values.nunique()==1 else None
def get_short_name(name):
    return ''.join([c for c in name if c.isalnum()])

# ============================================================ File stuff  

def get_subdirs(path):
    '''Get subdirectories in parent directory (direct children only, not all descendants)'''
    return [x for x in [y for y in os.walk(path)][0][1]]
def make_subdirs(path):
    '''Make nested folders (subdirs) as need to make sure that the full path exists'''
    folders = path.split('/')
    partial_path = ''
    for folder in folders:
        partial_path = folder if partial_path=='' else f'{partial_path}/{folder}'
        if not os.path.exists(partial_path):
            os.mkdir(partial_path)
    return path
def walk_directory_tree(path, level=0):
    '''Recursively walk a file/folder structure and return the tree structure'''
    tree = []
    node = {
        'level':level,
        'path':path,
        'is_dir':os.path.isdir(path),
        'is_file':os.path.isfile(path)
    }
    tree.append(node)
    if node['is_dir']:
        children = os.listdir(path)
        for child in children:
            child_path = os.path.join(path, child)
            tree += walk_directory_tree(child_path, level+1)
    return tree
def get_directory_tree(root):
    '''Recursively walk a file/folder structure, return the tree structure 
    as a dataframe, and then fill out with additional info'''
    df = pd.DataFrame(walk_directory_tree(root))
    df['rel_path'] = df.path.map(lambda x: x[len(root):]) # relative to root
    df['name'] = df.path.map(lambda x: x.split('/')[-1])
    return df
def copy_files_from_folder_to_folder(folder1, folder2, replace_existing=False):
    files1 = [f for f in os.listdir(folder1) if os.path.isfile(folder1+'/'+f)]
    files2 = [f for f in os.listdir(folder2) if os.path.isfile(folder2+'/'+f)]
    files_to_copy = files2 if replace_existing else [f for f in files1 if f not in files2]
    for fname in files_to_copy:
        shutil.copyfile(f'{folder1}/{fname}', f'{folder2}/{fname}')
    return files_to_copy

# ============================================================ Date stuff

def today():
    return datetime.date.today()
def today_str():
    return datetime.date.today().strftime('%Y_%m_%d')
def date_to_str(date):
    return date.strftime('%Y_%m_%d')
def date_to_month_id(date):
    return date.year*12 + date.month-1
def date_to_ym(date):
    return (date.year, date.month)
def date_to_qtr_id(date):
    return date.year*4 + (date.month-1)//3
def month_id_to_ym(x):
    return (x//12, x%12+1)
def ym_to_str(ym):
    return str(ym[0])+'_'+str(ym[1]).zfill(2)
def ym_to_qtr_id(ym):
    return ym[0]*4 + (ym[1]-1)//3
def ym_to_month_id(ym):
    return ym[0]*12 + ym[1]-1
def qtr_id_to_yq(x):
    return (x//4,x%4+1)
def yq_to_str(yq):
    return str(yq[0])+'_Q'+str(yq[1])
def yq_to_qtr_id(yq):
    return yq[0]*4 + (yq[1]-1)
def qtr_id_to_yq(x):
    return (x//4,x%4+1)
def yq_to_date(yq):
    return datetime.date(yq[0], yq[1]*3-2, 1) # first day of quarter
# ----------------------------- Composed date functions
def date_to_yq(date):
    return qtr_id_to_yq(date_to_qtr_id(date))
def date_to_yq_str(date):
    return yq_to_str(date_to_yq(date))
def date_to_ym_str(date):
    return ym_to_str(date_to_ym(date))
def qtr_id_to_yq_str(x):
    return yq_to_str(qtr_id_to_yq(x))
def month_id_to_ym_str(month_id):
    return ym_to_str(month_id_to_ym(month_id))
# ----------------------------- Complex date functions
def get_p_quarter_elapsed():
    '''Given todays date, determine the percent of the current quarter that has elapsed'''
    yq = date_to_yq(today()) # (year, month) for current quarter
    d0 = yq_to_date(yq) # first day of quarter 
    days_elapsed = (today()-d0).days
    days_in_quarter = 365/4 # about 91
    return days_elapsed/days_in_quarter
def get_projection_multiplier_for_quarter():
    yq_str = date_to_yq_str(today())
    p_elapsed = get_p_quarter_elapsed()
    multiplier = 1/p_elapsed
    return multiplier
def get_date_range(date0, date1):
    return [date0 + datetime.timedelta(n) for n in range(int((date1 - date0).days))]
def get_qtr_range_from_dates(dates):
    date_min = dates.min()
    date_max = dates.max()
    qtr_min = date_to_qtr_id(date_min)
    qtr_max = date_to_qtr_id(date_max)
    qtr_range = range(qtr_min, qtr_max+1)
    return qtr_range
def is_in_or_before_month(date,year,month):
    return date.year<year or (date.year==year and date.month<=month)
def get_month_range(dates):
    '''Return a list of (year,month) tuples spanning the first date to the last'''
    year_months = []
    dmin = dates.min()
    dmax = dates.max()
    xmin = dmin.year*12 + dmin.month - 1
    xmax = dmax.year*12 + dmax.month
    for x in range(xmin,xmax):
        year_months.append((x//12,x%12+1))
    return year_months
def get_month_id_range(dates):
    '''Return a list of month IDs spanning the first date to the last'''
    year_months = get_month_range(dates)
    month_ids = [ym_to_month_id(x) for x in year_months]
    return month_ids
def days360(date0,date1):
    '''Calculate the number of days between 2 dates based on Excel 30/360 function'''
    y0,m0,d0 = (date0.year,date0.month,date0.day)
    y1,m1,d1 = (date1.year,date1.month,date1.day)
    d0 = min(d0,30) # replace 31 with 30
    d1 = min(d1,30) # replace 31 with 30
    n_days = (y1-y0)*360 + (m1-m0)*30 + (d1-d0)
    return n_days
def group_dates_by_month_id(dates):
    '''Given an indexed set of dates, return a dataframe sorted and indexed by month ID 
    (including months with no values), and a column for the group of indexes corresponding to that month'''
    groups = dates.groupby(dates.map(date_to_month_id)).groups
    mmin = date_to_month_id(dates.min())
    mmax = date_to_month_id(dates.max())
    months = []
    for i in range(mmin, mmax+1):
        group = groups.get(i,[])
        months.append({'month_id':i,'group':group})
    months = pd.DataFrame(months).set_index('month_id')
    return months
def count_months(dates):
    '''Given a series of dates, return a series of value counts for each month ID,
    including months with 0 values; the month ID is the index'''
    date_months = dates.dropna().map(date_to_month_id)
    month_counts = date_months.value_counts()
    months = pd.DataFrame(index=range(date_months.min(), date_months.max()+1))
    months['n'] = months.index.map(lambda x: month_counts.get(x,0))
    return months.n

# ============================================================ Data stuff

def recast_decimals(df):
    for c in df.columns:
        if decimal.Decimal in df[c].map(type).unique():
            df[c] = df[c].map(lambda x: float(x) if x else np.nan)
    return df
def get_boolean_counts(data):
    '''Return a string with the number and relative percent of true/false values in a series'''
    vc = data.value_counts()
    n = len(data)
    n_true = vc[True]
    p_true = round(n_true/n,2)
    n_false = vc[False]
    p_false = round(n_false/n,2)
    y = f'True: \t {n_true} \t ({p_true})' + '\n' + f'False: \t {n_false} \t ({p_false})'
    return y
def convert_list_to_query_string(items):
    '''Convert list to properly formatted string for SQL query: ['a','b'] => ('a','b') '''
    query_string = '('+','.join([f'\'{x}\'' for x in items])+')'
    return query_string
def get_query_string_for_list(python_list):
    return '(' + ','.join([f"'{x}'" for x in python_list]) + ')'

# ============================================================ Plot stuff

def plot_bar_chart_from_series(data, 
    figsize=(16,6), bar_width=0.2, title=None, grid=True):
    '''Create a bar chat from a pandas series using the index as the bar labels (x) 
    and the values as the bar heights (y)'''
    fig = plt.figure(figsize=figsize)
    X = np.arange(len(data))
    Y = data.values
    bars = plt.bar(X, Y, bar_width, zorder=3)
    plt.xticks(X, data.index, rotation='vertical')
    if title is not None:
        plt.title(title)
    if grid:
        plt.grid(zorder=0)
def plot_stacked_bar_chart_from_dataframe(data, 
    figsize=(16,6), bar_width=0.2, title=None, grid=True, xticks_rotation='horizontal'):
    '''Create a stacked bar chart from a pandas dataframe using the index as the bar labels (x) 
    and the values per column as the bar heights (y), with the first column on the bottom'''
    fig = plt.figure(figsize=figsize)
    X = np.arange(len(data))
    bottoms = pd.Series([0 for _ in range(len(data))], index=data.index)
    for c in data.columns:
        Y = data[c].values
        bars = plt.bar(X, Y, bar_width, bottom=bottoms, label=c, zorder=3)
        bottoms = bottoms.add(data[c])
    plt.xticks(X, data.index, rotation=xticks_rotation)
    plt.legend()
    if title is not None:
        plt.title(title)
    if grid:
        plt.grid(zorder=0)
def plot_multi_bar_chart_from_dataframe(data, 
    figsize=(16,6), bar_width=0.2, title=None, grid=True, xticks_rotation='horizontal'):
    '''Create a multi bar chart -- with parallel bars of different colors -- from a pandas dataframe,
    using the index as the X labels for each bar group and the columns as the color-coded bar sets'''
    fig = plt.figure(figsize=figsize)
    X = np.arange(len(data)) # initial X positions
    for c in data.columns:
        Y = data[c].values
        bars = plt.bar(X, Y, bar_width, label=c, zorder=3)
        X = [x+bar_width for x in X]
    # Set x ticks at midpoint of each bar cluster
    X_ticks = [x + ((len(data.columns)-1)*bar_width)/2.0 for x in np.arange(len(data))]
    plt.xticks(X_ticks, data.index, rotation=xticks_rotation)
    plt.legend()
    if title is not None:
        plt.title(title)
    if grid:
        plt.grid(zorder=0)



