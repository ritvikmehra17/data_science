import matplotlib.pyplot as plt
'''graph 1 spines'''
days=list(range(0,22,3))
print(days)
temp_min=[23,25,21,30,36,26,30,22]
temp_max=[28,27,23,32,37,29,35,38]

fig=plt.figure(figsize=(8,6))
sub1 =plt.subplot(2,2,1)
sub2 =plt.subplot(2,2,2)
sub3 =plt.subplot(2,2,3)
sub4 =plt.subplot(2,2,4)
sub1.plot(days,temp_max,'or')
sub1.set_title("temp point plot")
sub3.plot(days,temp_max,'r')
sub3.set_title("temp point plot")
sub2.plot(days,temp_min,'ob')
sub2.set_title("temp point plot")


sub4.plot(days,temp_min,'ob')
sub4.set_title("temp point plot")
sub4.plot(days,temp_min,'b')
sub4.set_title("temp point plot")
sub4.plot(days,temp_max,'or')
sub4.set_title("temp point plot")
sub4.plot(days,temp_max,'r')
sub4.set_title("temp point plot")
