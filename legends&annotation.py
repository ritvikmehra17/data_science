import matplotlib.pyplot as plt
'''graph 1 annotation'''
days=list(range(0,22,3))
print(days)
temp_min=[23,25,21,30,36,26,30,22]
temp_max=[28,27,23,32,37,29,35,38]
plt.plot(days,temp_min)
plt.plot(days,temp_min,'ob',label='min')
plt.plot(days,temp_max)
plt.plot(days,temp_max,'or',label='max')
plt.legend(loc='best')
plt.annotate('temperature difference \n accross month',xy=(1,33.0))
plt.xlabel('day')
plt.ylabel('temperature')
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.xticks(list(range(0,28,7)),['w1','w2','w3','w4'])

plt.show()


'''graph 2 legends'''

plt.plot(days,temp_min)
plt.plot(days,temp_min,'ob',label='min')
plt.plot(days,temp_max)
plt.plot(days,temp_max,'or',label='max')
plt.legend(loc='best')
plt.xlabel('day')
plt.ylabel('temperature')
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.xticks(list(range(0,28,7)),['w1','w2','w3','w4'])

plt.show()
