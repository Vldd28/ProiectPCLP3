import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

survived = df['Survived'].value_counts(normalize=True) * 100
print(f'Procentul persoanelor care au supravietuit si care nu au supravietuit: \n{survived}')

# Procentul pasagerilor pentru fiecare tip de clasa
pclass = df['Pclass'].value_counts(normalize=True) * 100
print(f'Procentul pasagerilor pentru fiecare tip de clasa: \n{pclass}')

# Procentul barbatilor si procentul femeilor
sex = df['Sex'].value_counts(normalize=True) * 100
print(f'Procentul barbatilor si femeilor: \n{sex}')

# Crearea unui grafic pentru prezentarea acestor rezultate
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Grafic pentru supravietuire
axs[0].bar(survived.index, survived.values, color=['red', 'green'])
axs[0].set_title('Procentul de supravietuire')
axs[0].set_xticks([0, 1])
axs[0].set_xticklabels(['Nu', 'Da'])

# Grafic pentru clasa
axs[1].bar(pclass.index, pclass.values, color=['blue', 'orange', 'green'])
axs[1].set_title('Procentul pasagerilor pe clase')
axs[1].set_xticks([1, 2, 3])
axs[1].set_xticklabels(['Clasa 1', 'Clasa 2', 'Clasa 3'])

# Grafic pentru sex
axs[2].bar(sex.index, sex.values, color=['blue', 'pink'])
axs[2].set_title('Procentul pasagerilor pe sex')
axs[2].set_xticks([0, 1])
axs[2].set_xticklabels(['Barbati', 'Femei'])

# Creeaza graficul
plt.tight_layout()
plt.savefig(f'Cerinta2/graph.png')


