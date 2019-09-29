import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta as delta
'''
ndays=10
start=datetime(2018,3,31)
dates=[start-delta(days=x)for x in range(0,ndays)]

values=[25,56,59,65,70,75,80,95,105,125]
ts=pd.Series(values,index=dates)
print(ts)

ts=ts.plot(kind= "bar")
plt.show()
'''

index=pd.date_range('12/24/1970','01/03/1971')
print(index)
