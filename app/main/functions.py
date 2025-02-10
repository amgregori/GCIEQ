from datetime import datetime
from datetime import date
import os
import pandas as pd

from config import engine
from openpyxl import load_workbook
from sqlalchemy import create_engine


def eq_usage_file_check(eq_usage_file):

      
    df = pd.read_excel(eq_usage_file, nrows=2)

      
    col_00 = df.columns[0]
    col_06 = df.columns[6]
    col_08 = df.columns[8]
    col_09 = df.columns[9]
    col_17 = df.columns[17]

    check_columns = (col_00 == 'sort_order_no' and col_06 == 'equipment_no'
                             and col_08 == 'date_booked' and col_09 == 'job_no' 
                             and col_17 == 'equipment_units')
            
    if check_columns:
        check = 'OK'
    else:
        check = "No"

    return check


def eq_usage_import(eq_usage_file):
    # 01 - Import Equipment Usage Data
    eq_usage_df_raw = pd.read_excel(eq_usage_file)
    eq_usage_df = eq_usage_df_raw[[ 'equipment_no', 'transaction_no','date_booked', 'job_no', 'equipment_units', 'cost_code_no']].copy()

    today = date.today()
    eq_usage_df['date_modified'] = today


    # 02 - Clean Up & Format Import Data
    eq_usage_df['job_no'] = eq_usage_df['job_no'].astype(str)
    eq_usage_df['cost_code_no'] = eq_usage_df['cost_code_no'].astype(str)
    eq_usage_df['cost_code_no'] = eq_usage_df['cost_code_no'].apply(lambda x: x.replace(' ', ''))
    eq_usage_df['equipment_no'] = eq_usage_df['equipment_no'].apply(lambda x: x.replace(' ', ''))
    eq_usage_df['date_booked'] = eq_usage_df['date_booked'].dt.date


    # 03 - Query Transaction Numbers that Exist in the DB
    transaction_df_raw = pd.read_sql_table('eq_usage', engine)
    transaction_df = transaction_df_raw[['transaction_no']].copy()
    transaction_list = transaction_df['transaction_no'].unique()


    #05 - Remove import_df Rows with Transaction Numbers that Appear in the Database
    rows_to_drop = eq_usage_df['transaction_no'].isin(transaction_df.loc[:, 'transaction_no'])
    eq_usage_df = eq_usage_df[~rows_to_drop]

    eq_usage_df.to_excel('eq_import.xlsx')


    #06 - Add New Transactions to Database

    #eq_usage_df.to_sql('eq_usage', engine, if_exists='append', index=False)

    return(len(eq_usage_df))






    