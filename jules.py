def money(x):
    '''Convert a number to a properly formatted currency string, e.g. 1.234 => $1.23'''
    return '${:,.2f}'.format(x) if x>=0 else '-${:,.2f}'.format(-x)

def space(x,n=30):
    return str(x) + ' '*max(0,n-len(str(x)))

def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

def recast_decimals(df):
    for c in df.columns:
        if decimal.Decimal in df[c].map(type).unique():
            df[c] = df[c].map(lambda x: float(x) if x else np.nan)
    return df

def render_amts(x):
    '''For all columns that start with "amt_", replace with money strings'''
    if type(x)==pd.DataFrame:
        rendered = x.copy()
        for c in rendered.columns:
            if c.startswith('amt_'):
                rendered[c] = rendered[c].map(money)
    elif type(x)==pd.Series or type(x)==dict:
        rendered = {}
        for c in x:
            if type(c)==str and c.startswith('amt_'):
                rendered[c] = money(rendered[c])
    return rendered

def get_one(values):
    '''Given a series of values, return the first one if all are the same'''
    return values.iloc[0] if values.nunique()==1 else None

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

def traverse_file_tree(root):
    tree = []
    for (path,dirs,files) in os.walk(root, topdown=True): 
        tree.append({
            'path':path,
            'n_dirs':len(dirs),
            'n_files':len(files)
        })
    return pd.DataFrame(tree)

def copy_files_from_folder_to_folder(folder1, folder2, replace_existing=False):
    files1 = [f for f in os.listdir(folder1) if os.path.isfile(folder1+'/'+f)]
    files2 = [f for f in os.listdir(folder2) if os.path.isfile(folder2+'/'+f)]
    files_to_copy = files2 if replace_existing else [f for f in files1 if f not in files2]
    for fname in files_to_copy:
        shutil.copyfile(f'{folder1}/{fname}', f'{folder2}/{fname}')
    return files_to_copy


    
