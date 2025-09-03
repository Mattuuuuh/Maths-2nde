import matplotlib.pyplot as plt
import matplotlib.cm as cm

liste = [i/100 for i in range(101)]

for element in liste:
    x = element*1 + (1-element)*3
    y = element*1 + (1-element)*(-1)
    
    plt.scatter(x,y, c=cm.rainbow(element))

plt.grid()
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
plt.xlim(-1,4)
plt.ylim(-2,2)
plt.show()
