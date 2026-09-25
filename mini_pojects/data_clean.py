#impoting necessary libraies

import pandas as pd
import numpy as np

#loading the dataset
df = pd.read_csv(
    r'C:\Users\Pc\OneDrive\Desktop\indian_employees_pandas_numpy_practice_1000.csv'
)

print(df.head())
print(df.tail())

#checking the missing values
print('Missing valuesmin in each column')
print(df.isnull().sum())

df['job_Role (INR)'].fillna(df['job_Role (INR)'].mean(),inplace=True)

df['Education  (INR)'].fillna(df['Education  (INR)'].mean(),inplace=True)

df.replace([np.inf, -np.inf], np.nan,inplace=True) 

df.fillna(df.mean(),inplace=True) 

#remove duplicate records

df.drop_duplicates(inplace=True)