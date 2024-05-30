import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('train.csv')

# List of numeric columns in the Titanic dataset
numeric_cols = ['PassengerId','Survived','Pclass','Age', 'Fare', 'SibSp', 'Parch']

# Generate a histogram for each numeric column
for col in numeric_cols:
    df[col].hist(bins=30)
    plt.title(f'Histogram for {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.savefig(f'Cerinta3/{col}_histogram.png')
    plt.clf()
