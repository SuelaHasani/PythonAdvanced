from unittest.mock import inplace

import pandas as pd
from numpy.ma.extras import average

df = pd.read_csv('data1.csv')

print(df.info())

# na shfaq 5 rreshtat e pare
print(df.head())


country_data=df['Country']

print(country_data)


subset = df[['Country','Average IQ']]

print(subset)


filtred_df = subset[subset['Average IQ']>100]
print(filtred_df)

null_mask = df.isnull()

null_count = null_mask.sum()
print(null_count)


df.dropna(inplace=True)

print(df.info())
print("---------------------------------------------")
duplicates_count = df.duplicated().sum()
print(duplicates_count)


average_iq_continent = df.groupby('Continent')['Average IQ'].mean()

print(average_iq_continent)

sorted_avg_by_continent = average_iq_continent.sort_values(ascending=False)

print(sorted_avg_by_continent)


total_nobel_by_country = df.groupby('Country')['Nobel Prices'].sum()

print(total_nobel_by_country)


sorted_total_nobel_by_country = total_nobel_by_country.sort_values(ascending=False)

print(sorted_total_nobel_by_country)


sorted = sorted_total_nobel_by_country[sorted_total_nobel_by_country != 0]

print(sorted)