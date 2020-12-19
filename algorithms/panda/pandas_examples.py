import pandas as pd
import numpy as np

# – DataFrame(data=None, index=None, columns=None, dtype=None,copy=False)

dfCountries=pd.read_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\αρχεια\\gapminder.csv',sep='\t')
# dfCountries.head()
# print(dfCountries)
# print(dfCountries.groupby('year')['lifeExp'].mean())
# print(dfCountries.groupby('year')['pop'].mean())
# print(dfCountries.groupby('year')['gdpPercap'].mean())
# print(dfCountries.groupby(['year','continent'])[['lifeExp','pop','gdpPercap']].mean())
# print(dfCountries.groupby('continent')['country'].nunique())
# print(dfCountries['pop']*dfCountries['gdpPercap'])
# print(dfCountries.groupby('year')['pop'].mean()>dfCountries['pop'].mean())
print(dfCountries.groupby('year')['pop'].describe())



# Dframe = pd.DataFrame(np.random.rand(5,3),index=range(0,10,2),columns=list('ABC'))
# Dframe.iloc[0:3,1:3]
# Dframe.iloc[3]
# Dframe.loc[[0,2],:]
# Dframe.loc[[0,2],['A','B']]
# Dframe.loc[6:]>0

# – Series(data=None, index=None, dtype=None, name=None …)

# s2=pd.Series([5,7,3,5.252,'Nikos'],index=['A','B',4,'P',0])
# print(s2)