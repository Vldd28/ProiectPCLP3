import pandas as pd
import matplotlib.pyplot as plt


### CERINTA 1
# Citirea datelor din fisierul csv
df = pd.read_csv('train.csv')

# Numarul de coloane
num_cols = len(df.columns)
print(f'Numarul de coloane: {num_cols}')

# Tipurile datelor din fiecare coloana
data_types = df.dtypes
print(f'Tipurile datelor din fiecare coloana: \n{data_types}')

# Numarul de valori lipsa pentru fiecare coloana
missing_values = df.isnull().sum()
print(f'Numarul de valori lipsa pentru fiecare coloana: \n{missing_values}')

# Numarul de linii
num_rows = len(df)
print(f'Numarul de linii: {num_rows}')

# Verificarea daca exista linii duplicate
duplicates = df.duplicated().sum()
print(f'Numarul de linii duplicate: {duplicates}')
