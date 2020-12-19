import datetime as dt
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

################################################ 2 ####################################################################

dfShares=pd.read_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\αρχεια\\IBM.csv', sep=',')
dfShares['percentage_daily_fluctuation'] = round(100 * (dfShares['Open'] - dfShares['Close']) / dfShares['Open'], 2)
dfShares.to_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\αρχεια\\IBM_output.csv', sep=';')

########################################################################################################################

################################################ 3 ####################################################################

istogram = dfShares.groupby('percentage_daily_fluctuation')['Date'].count()
istogram.plot(kind='line',x='name',y='num_children')
plt.show()

########################################################################################################################

################################################ 4 ####################################################################

my_dict = dict(istogram)
istogram = pd.DataFrame(my_dict.items(), columns=["percentage_daily_fluctuation", "days"])
data = norm.rvs(istogram)
mu, std = norm.fit(data)
plt.hist(data, bins=25, density=True, alpha=0.3, color=['g', 'r'])
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Percentage Daily Fluctuation results: mu = %.2f, std = %.2f" % (mu, std)
plt.title(title)
plt.show()

########################################################################################################################

################################################ 5 ####################################################################

def financial_process(company_name, link):
    start = dt.datetime(1970,1,2)
    end = dt.datetime(2020,12,13)
    df = web.DataReader(company_name, link, start=start, end=end)
    df['percentage_daily_fluctuation'] = round(100 * (df['Open'] - df['Close']) / df['Open'], 2)
    df['Date'] = df.index

    istogram = df.groupby('percentage_daily_fluctuation')['Date'].count()
    istogram.plot(kind='line', x='name', y='num_children')
    plt.show()

    my_dict = dict(istogram)
    istogram = pd.DataFrame(my_dict.items(), columns=["percentage_daily_fluctuation", "days"])
    data = norm.rvs(istogram)
    mu, std = norm.fit(data)
    plt.hist(data, bins=25, density=True, alpha=0.3, color=['g', 'r'])
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Percentage Daily Fluctuation results: mu = %.2f, std = %.2f" % (mu, std)
    plt.title(title)
    plt.show()


name = input('Give name: ')
link = input('Give link: ')
# "TSLA", "yahoo"
financial_process(name, link)

########################################################################################################################