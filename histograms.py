import matplotlib.pyplot as plt
'''graph 1 s'''
days=list(range(0,22,3))
print(days)
temp_min=[23,25,21,30,36,26,30,22]
temp_max=[28,27,23,32,37,29,35,38]

import numpy as np
gaus_numbers =np.random.normal(size=1000)
plt.hist(gaus_numbers)


'''graph 2'''
gaus_numbers =np.random.normal(size=1000)
plt.hist(gaus_numbers,bins=100)

'''graph 3'''
gaus_numbers =np.random.normal(size=1000)
plt.hist(gaus_numbers,bins=20,color="r")

'''graph 4'''
gaus_numbers =np.random.normal(size=1000)
plt.hist(gaus_numbers,bins=20,color="r",edgecolor='b')

'''graph 5'''
gaus_numbers =np.random.normal(size=1000)
plt.hist(gaus_numbers,bins=20,color="r",
         edgecolor='b',stacked=True,cumulative=True)
