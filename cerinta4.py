import pandas as pd

def calculate_missing_mean(x):
    return x.isnull().mean()

df = pd.read_csv('train.csv')

missing_cols = df.columns[df.isnull().any()].tolist()

for col in missing_cols:
    missing_count = df[col].isnull().sum()
    missing_proportion = df[col].isnull().mean()
    print(f'For column {col}, missing count: {missing_count}, missing proportion: {missing_proportion}')

grouped_df = df.groupby('Survived')


missing_per_class = grouped_df.apply(calculate_missing_mean, include_groups=False)
print(missing_per_class)