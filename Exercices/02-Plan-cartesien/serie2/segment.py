import matplotlib.pyplot as plt

liste = [0, 1, 0.5, 0.25, 0.75]

for element in liste:
    x = element*1 + (1-element)*3
    y = element*1 + (1-element)*(-1)
    
    plt.scatter(x,y)

plt.grid()
plt.show()
