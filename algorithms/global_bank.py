import pandas as pd

# convert to csv to load faster

# df = pd.read_excel("C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\WDIEXCEL.xlsx")
# df.to_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\WDIEXCEL.csv', sep=';')
# df = pd.read_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\WDIEXCEL.csv', sep=';')
# df = df.loc[df['Country Code'].isin({"GRC", "DEU", "FRA", "ITA"})]
# df.to_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\my_countries.csv', sep=';')
# df = pd.read_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\my_countries.csv', sep=';')
# df.drop(df.columns[[0, 1]], axis=1, inplace=True)
# df.to_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\countries.csv', sep=';')

df = pd.read_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\countries.csv', sep=';')
df.drop(df.columns[[0]], axis=1, inplace=True)
print(df)
