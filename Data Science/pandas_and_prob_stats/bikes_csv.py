import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

broken_df = pd.read_csv('bikes.csv')
# print(broken_df[:3])

fixed_df = pd.read_csv('bikes.csv',sep=';',encoding='latin1',parse_dates=['Date'],dayfirst=True,index_col='Date')
# print(fixed_df[4:7])
# fixed_df['Maisonneuve 2'].plot()
# fixed_df.plot(figsize=[25,10])

df = pd.read_csv('bikes.csv',sep=';',encoding='latin1',parse_dates=['Date'],dayfirst=True,index_col='Date')
df["Berri 1"].plot(figsize=[45,15])
