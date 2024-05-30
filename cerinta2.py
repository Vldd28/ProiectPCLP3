import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

# percentage of people who survived and who did not survive
survived = df['Survived'].value_counts(normalize=True) * 100
print(f'Percentage of people who survived and who did not survive: \n{survived}')

# percentage of passengers for each class type
pclass = df['Pclass'].value_counts(normalize=True) * 100
print(f'Percentage of passengers for each class type: \n{pclass}')

sex = df['Sex'].value_counts(normalize=True) * 100
print(f'Percentage of men and women: \n{sex}')

# creating a plot to present these results
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# plot for survival
axs[0].bar(survived.index, survived.values, color=['red', 'green'])
axs[0].set_title('Survival Percentage')
axs[0].set_xticks([0, 1])
axs[0].set_xticklabels(['No', 'Yes'])

# plot for class
axs[1].bar(pclass.index, pclass.values, color=['blue', 'orange', 'green'])
axs[1].set_title('Passenger Percentage by Class')
axs[1].set_xticks([1, 2, 3])
axs[1].set_xticklabels(['Class 1', 'Class 2', 'Class 3'])

# sex plot
axs[2].bar(sex.index, sex.values, color=['blue', 'pink'])
axs[2].set_title('Passenger Percentage by Sex')
axs[2].set_xticks([0, 1])
axs[2].set_xticklabels(['Men', 'Women'])

plt.tight_layout()
plt.savefig(f'Task2/graph.png')