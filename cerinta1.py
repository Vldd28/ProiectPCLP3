import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

# num of columns
num_cols = len(df.columns)
print(f'Number of columns: {num_cols}')

# data types of each column
data_types = df.dtypes
print(f'Data types of each column: \n{data_types}')

# num of missing values for each column
missing_values = df.isnull().sum()
print(f'Number of missing values for each column: \n{missing_values}')

num_rows = len(df)
print(f'Number of rows: {num_rows}')

duplicates = df.duplicated().sum()
print(f'Number of duplicate rows: {duplicates}')