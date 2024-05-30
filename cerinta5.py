import pandas as pd
import matplotlib.pyplot as plt

# load the data
df = pd.read_csv('train.csv')

# define the age categories and labels
bins = [0, 20, 40, 60, df['Age'].max()]
labels = ['0-20', '21-40', '41-60', '61+']

# create a new column 'AgeCategory' in the DataFrame
df['AgeCategory'] = pd.cut(df['Age'], bins=bins, labels=labels)

# count the number of passengers in each age category
age_counts = df['AgeCategory'].value_counts()

# plot the results
age_counts.sort_index().plot(kind='bar')
plt.xlabel('Age Category')
plt.ylabel('Number of Passengers')
plt.title('Number of Passengers in Each Age Category')

# save the plot to a file
plt.savefig('Cerinta5/age_categories.png')