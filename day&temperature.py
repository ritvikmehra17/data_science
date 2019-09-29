import matplotlib.pyplot as plt
'''1st graph'''

plt.plot([-1,0,6,8,5])
plt.show()

'''2 graph'''
plt.plot([-1,0,6,8,5],'or')
plt.show()

'''3 graph'''
days=list(range(0,22,3))
print(days)
temp=[23,25,21,30,36,26,30,22]
plt.plot(days,temp)
plt.show()

'''4 graph'''
plt.plot(days,temp,'ob')
plt.show()

'''5 graph'''
temp_min=[23,25,21,30,36,26,30,22]
temp_max=[28,27,23,32,37,29,35,38]
plt.plot(days,temp_min,
         days,temp_min,'ob',
         days,temp_max,
        days,temp_max,'or',)
plt.xlabel('day')
plt.ylabel('temperature')
plt.show()
