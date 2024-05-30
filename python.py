
### CERINTA 4

missing_proportion = missing_values / len(df)

missing_cols = df.column[df.isnull().sum()].tolist()

for col in missing_cols:
        missing_cols = df[col].isnull().sum()
        missing_proportion = df[col].isnull().mean()
        print(f'For column {col}, missing count: {missing_count}, missing proportion: {missing_proportion}')

missing_per_class = df.groupby('Survived').apply(lambda x: x.isnull().mean())
print(missing_per_class)

### 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