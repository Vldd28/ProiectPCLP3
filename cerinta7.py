import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

# function to categorize passengers as children or adults
def categorize_age(age):
    if age < 18:
        return 'Child'
    else:
        return 'Adult'

# apply function to the 'Age' column to create a new column 'AgeGroup'
df['AgeGroup'] = df['Age'].apply(categorize_age)

#cCalculate percentage of passengers who are children
child_percentage = (df['AgeGroup'] == 'Child').mean() * 100
print(f'Percentage of children: {child_percentage}%')

# calculate the survival rate for children and adults
survival_rate = df.groupby('AgeGroup')['Survived'].mean()

# plot the survival rates
survival_rate.plot(kind='bar')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.title('Survival Rate of Children and Adults')

plt.savefig('Cerinta7/survival_rate.png')