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

