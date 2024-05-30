import pandas as pd

df = pd.read_csv('train.csv')

# function to fill missing numerical values with the mean
def fill_numerical_na(group):
    return group.fillna(group.mean())

# function to fill missing categorical values with the most frequent value
def fill_categorical_na(group):
    return group.fillna(group.mode()[0])

numerical_columns = ['Age']
categorical_columns = ['Embarked']

for col in numerical_columns:
    df[col] = df.groupby('Survived')[col].transform(fill_numerical_na)

for col in categorical_columns:
    df[col] = df.groupby('Survived')[col].transform(fill_categorical_na)

# ataframe with filled values to a new CSV file
df.to_csv('Cerinta8/train_filled.csv', index=False)