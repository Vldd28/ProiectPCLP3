import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('train.csv')

# Define the age categories and labels
bins = [0, 20, 40, 60, 140]
labels = ['0-20', '21-40', '41-60', '61+']

# Create a new column 'AgeCategory' in the DataFrame
df['AgeCategory'] = pd.cut(df['Age'], bins=bins, labels=labels)

# Filter the DataFrame to include only male passengers
df_males = df[df['Sex'] == 'male']

# Count the total number of male passengers in each age category
total_males = df_males['AgeCategory'].value_counts()

# Count the number of male passengers who survived in each age category
survived_males = df_males[df_males['Survived'] == 1]['AgeCategory'].value_counts()

# Calculate the survival rate for each age category
survival_rate = survived_males / total_males

# Plot the survival rates
survival_rate.sort_index().plot(kind='bar')
plt.xlabel('Age Category')
plt.ylabel('Survival Rate')
plt.title('Survival Rate of Male Passengers by Age Category')
plt.savefig('Cerinta6/male_survival_rate.png')