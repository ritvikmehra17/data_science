import matplotlib.pyplot as plt
'''graph 1 spines'''
days=list(range(0,22,3))
print(days)
temp_min=[23,25,21,30,36,26,30,22]
temp_max=[28,27,23,32,37,29,35,38]
plt.plot(days,temp_min,
         days,temp_min,'ob',
         days,temp_max,
        days,temp_max,'or',)
plt.xlabel('day')
plt.ylabel('temperature')
ax=plt.gca()
ax.spines['right'].set_visible(False)
plt.show()

'''graph 2 spines'''


plt.plot(days,temp_min,
         days,temp_min,'ob',
         days,temp_max,
        days,temp_max,'or',)
plt.xlabel('day')
plt.ylabel('temperature')
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()



'''graph 3  spines'''

plt.plot(days,temp_min,
         days,temp_min,'ob',
         days,temp_max,
        days,temp_max,'or',)
plt.xlabel('day')
plt.ylabel('temperature')
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_bounds(22.5,37.5)
plt.show()

'''graph 4 ticks'''

plt.plot(days,temp_min,
         days,temp_min,'ob',
         days,temp_max,
        days,temp_max,'or',)
plt.xlabel('day')
plt.ylabel('temperature')
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.xticks(list(range(0,22)))

plt.show()

'''graph 5 ticks'''

plt.plot(days,temp_min,
         days,temp_min,'ob',
         days,temp_max,
        days,temp_max,'or',)
plt.xlabel('day')
plt.ylabel('temperature')
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.xticks(list(range(0,28,7)),['w1','w2','w3','w4'])

plt.show()
