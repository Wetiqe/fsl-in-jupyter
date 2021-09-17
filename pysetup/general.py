import pandas as pd
import sqlite3
import numpy as np

# sqlite3 db
## connect to sqlite3 db
def db_conn(db_dir=""):
    if db_dir:
        try:
            db = sqlite3.connect(db_dir,timeout=30)
            dbcr = db.cursor()
        
            return db, dbcr
        except:
            print("this func is for sqlite3")
    else:
        print("plz enter a directory")
        
## get arrtributes of a sqlite3 table
def get_columns(table_name, dbcr):
    dbcr.execute("SELECT * FROM {}".format(table_name))
    col_list = [tuple[0] for tuple in dbcr.description]
    return col_list


# Pandas
## set pandas params
def pd_setup():
    pd.set_option('max_columns',1000)
    pd.set_option('max_row',300)
    pd.set_option('display.float_format', lambda x: '%.4f' % x) # set how many decimal places to keep
    pd.options.mode.chained_assignment = None  # default='warn'; disalarm ' SettingWithCopyWarning'


def fill_na_mean(df, rd=2):
    for col in list(df.columns[df.isnull().sum() > 0]):
        mean_val = df[col].mean()
        df[col].fillna(round(mean_val,rd),inplace=True)
        
def save_table(df,name):
    df.to_csv('table/{}.csv'.format(name))
    

# Create report table
def create_t_table(result_df, df1, df2, columns=['Group1', 'Group2'], aconva=True):
    """
    Create a final table for independent t test
    
    args:
        result_df: the t test result table whose columns must contains 'group 1 norm','group 1 norm p', 'group 2 norm', 'group 2 norm p', 'levene', 'levene p', 't value','p value', 'permutation p', 'ancova p' in order.
        df1: the data of the first group
        df2: the data of the second group
        columns: the name of the two groups
        aconva: if set True, the func will append a new columns contains aconva p value at the end
    
    returns:
        ft: means 'final table', contains all necesssary data for report
    """
    # set columns' name
    columns.extend(['t value', 'p value'])
    if aconva:
        columns.append('ancova p value')

    df1_desc = df1.describe()
    df2_desc = df2.describe()
    # create final table
    rows = len(result_df.index)
    cols = len(columns)
    ft = pd.DataFrame(np.zeros(rows*cols).reshape(rows,cols), index = result_df.index, columns=columns)
    # fill ft
    for i, item in enumerate(ft.index):
        # set mean ± std
        ft.loc[item, columns[0]] = '{} ± {}'.format(round(df1_desc.loc['mean', item],2), round(df1_desc.loc['std', item],2))
        ft.loc[item, columns[1]] = '{} ± {}'.format(round(df2_desc.loc['mean', item],2), round(df2_desc.loc['std', item],2))
        # set t value & p value
        ft.loc[item, columns[2]] = round(result_df.iloc[i, 7], 2) # t value
        ft.loc[item, columns[3]] = result_df.iloc[i, 8] # p value
        # 
        if result_df.iloc[i, 1] < 0.05 or result_df.iloc[i, 3] < 0.05:
            ft.loc[item, columns[3]] = result_df.iloc[i, 9] # set to permutaion t test p value if the data does not pass the normality test
        if aconva:
            ft.loc[item, columns[4]] = result_df.iloc[i, -1] # set aconva p value if 
    
    return ft


def create_paired_t_table(result_df, df1, df2, columns=['Group1', 'Group2']):
    """
    Create a final table for paired t test
    
    args:
        result_df: the t test result table whose columns must contains 'group 1 norm','group 1 norm p', 'group 2 norm', 'group 2 norm p',  't value','p value', 'permutation p', 'ancova p' in order.
        df1: the data of the first group
        df2: the data of the second group
        columns: the name of the two groups
        aconva: if set True, the func will append a new columns contains aconva p value at the end
    
    returns:
        ft: means 'final table', contains all necesssary data for report
    """
    columns.extend(['t value', 'p value'])
    df1_desc = df1.describe()
    df2_desc = df2.describe()
    rows = len(result_df.index)
    cols = len(columns)
    ft = pd.DataFrame(np.zeros(rows*cols).reshape(rows,cols), index = result_df.index, columns=columns)
    for i, item in enumerate(ft.index):
        # set mean ± std
        ft.loc[item, columns[0]] = '{} ± {}'.format(round(df1_desc.loc['mean', item],2), round(df1_desc.loc['std', item],2))
        ft.loc[item, columns[1]] = '{} ± {}'.format(round(df2_desc.loc['mean', item],2), round(df2_desc.loc['std', item],2))
        # set t value & p value 
        ft.loc[item, columns[2]] = round(result_df.iloc[i, -3], 2)
        ft.loc[item, columns[3]] = result_df.iloc[i, -2]
        if result_df.iloc[i, 1] < 0.05 or result_df.iloc[i, 3] < 0.05:
            ft.loc[item, columns[3]] = result_df.iloc[i, -1]

    return ft
