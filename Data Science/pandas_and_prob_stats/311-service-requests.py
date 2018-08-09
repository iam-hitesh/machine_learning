%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')


# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)

complaints = pd.read_csv('311-service-requests.csv')
# complaints
# complaints['Complaint Type']
# complaints['Complaint Type'][:5]
# complaints[:5][['Complaint Type','Borough']]
# complaints[['Complaint Type','Borough']]
complaint_count = complaints['Complaint Type'].value_counts()
# complaint_count[:10]
complaint_count[:10].plot(kind="Bar")
plt.show(block=True)
