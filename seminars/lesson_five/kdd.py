# import libraries
from pandas import read_csv
import pandas as pd
# define the location of the dataset
path = 'C:/Directory1/weather.csv'
# load the dataset
df = read_csv(path)
# summarize the number of unique values in each column
print("Total uniques values per column:\n", df.nunique())
# calculate duplicates
dups = df.duplicated()
# report if there are any duplicates
print("\n\nAre there any duplicates?:", dups.any())
# list all duplicate rows
print("\n\nThe duplicate row(s) are:\n", df[dups])
# delete duplicate rows
df.drop_duplicates(inplace=True)
#store the data frame without the index in a new path
df.to_csv('C:/Directory1/weather_new.csv', index = False)

#delete first column day
df = df.drop('day', 1)
df.to_csv('C:/Directory1/new_1.csv', index = False)