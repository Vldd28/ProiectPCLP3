import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

df['IsAlone'] = (df['SibSp'] == 0) & (df['Parch'] == 0)

# first histogram
# a catplot showing the relationship between fare, class, and survival for the first 100 records
sns.catplot(data=df.head(100), x="Fare", y="Pclass", hue="Survived", kind="strip")
plt.title('Relationship between fare, class, and survival for the first 100 records')
plt.savefig('Cerinta10/fareClassSurvival.png')


# second histogram
plt.figure(figsize=(15, 10))
sns.histplot(data=df, x="Survived", hue="IsAlone", multiple="stack")
plt.title('Survival rates for alone vs not alone passengers')
plt.xlabel('Survived')
plt.ylabel('Count')

# Save the histogram
plt.savefig('Cerinta10/loneliness.png')