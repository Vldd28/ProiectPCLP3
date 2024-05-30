import pandas as pd
import matplotlib.pyplot as plt

# load the data
df = pd.read_csv('train.csv')

ages = [0, 20, 40, 60, 140]
labels = ['0-20', '21-40', '41-60', '61+']

df['AgeCategory'] = pd.cut(df['Age'], ages=ages, labels=labels)

# a dataframe that only contains male pasagers
df_males = df[df['Sex'] == 'male']

# count the male category
total_males = df_males['AgeCategory'].value_counts()
survived_males = df_males[df_males['Survived'] == 1]['AgeCategory'].value_counts()

# calculate the survival rate for each age category
survival_rate = survived_males / total_males

# plot the survival rates
survival_rate.sort_index().plot(kind='bar')
plt.xlabel('Age Category')
plt.ylabel('Survival Rate')
plt.title('Survival Rate of Male Passengers by Age Category')
plt.savefig('Cerinta6/male_survival_rate.png')