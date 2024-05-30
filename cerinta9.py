import re
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

df['Title'] = df['Name'].apply(lambda x: re.search(r'(\b[A-Za-z]+\.)', x).group(1))

# Map titles to a standard set of titles and genders
title_gender_map = {
    'Mr.': 'male', 'Mrs.': 'female', 'Miss.': 'female', 'Master.': 'male',
    'Dr.': 'unknown', 'Rev.': 'male', 'Col.': 'male', 'Major.': 'male',
    'Mlle.': 'female', 'Mme.': 'female', 'Don.': 'male', 'Dona.': 'female',
    'Lady.': 'female', 'Sir.': 'male', 'Capt.': 'male', 'Countess.': 'female',
    'Jonkheer.': 'male'
}

# Create a new column 'ExpectedSex' based on the title
df['ExpectedSex'] = df['Title'].map(title_gender_map)

# Compare the 'ExpectedSex' with 'Sex' to check for correspondence
df['Matches'] = df['Sex'] == df['ExpectedSex']

# Count the number of people for each title
title_counts = df['Title'].value_counts()

# Count the number of matches for each title
title_matches = df[df['Matches']]['Title'].value_counts()

# Create a DataFrame for plotting
plot_data = pd.DataFrame({
    'Total': title_counts,
    'Matches': title_matches
}).fillna(0)

# Plot the data

plot_data.plot(kind='bar', figsize=(12, 6))
plt.title('Number of People Corresponding to Each Title')
plt.xlabel('Title')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(['Total', 'Matches'])
plt.savefig('Cerinta9/Names.png')