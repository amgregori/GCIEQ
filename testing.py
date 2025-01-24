from sqlalchemy import create_engine
import pandas as pd

from config import engine
import pandas


usage_file = 'D:\Python\GCIEQ\TestData\Eq Usage Post - Test.xlsx'
            
df = pd.read_excel(usage_file)

print(df)
