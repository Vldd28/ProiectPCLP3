import pandas as pd

# Load the data
df = pd.read_csv('train.csv')

# Define a function to fill missing numerical values with the mean
def fill_numerical_na(group):
    return group.fillna(group.mean())

# Define a function to fill missing categorical values with the most frequent value
def fill_categorical_na(group):
    return group.fillna(group.mode()[0])

# For numerical columns like 'Age', fill missing values with the mean age of passengers in the same survival category
df['Age'] = df.groupby('Survived')['Age'].transform(fill_numerical_na)

# For categorical columns, fill missing values with the most frequent value in the same survival category
# Assuming 'Embarked' is a categorical column with missing values
df['Embarked'] = df.groupby('Survived')['Embarked'].transform(fill_categorical_na)

# Save the DataFrame with filled values to a new CSV file
df.to_csv('Cerinta8/train_filled.csv', index=False)