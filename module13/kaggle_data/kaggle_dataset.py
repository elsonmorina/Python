import pandas as pd
from tensorflow.python.framework.test_util import disable_ubsan

df = pd.read_csv('file1.csv')
print(df.info())

first_rows = df.head()
print(first_rows)

country_data = df['Country']
print(country_data)

subset = df[['Country','Average IQ']]
print(subset)

filtered_df = subset[subset['Average IQ']>100]
print(filtered_df)

duplicated_cont = df.duplicated().sum()
print('\nCount of duplicated rows:')
print(duplicated_cont)

average_iq_per_continent = df.groupby('Continent')['Average IQ'].mean()
print(average_iq_per_continent)
