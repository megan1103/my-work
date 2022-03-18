import numpy as np
import matplotlib.pyplot as plt
xpoints = np.array(range(1,101))
# y points will be x^2
ypoints = xpoints* xpoints
plt.plot(xpoints,ypoints, label ="xsquared")
plt.plot(xpoints,xpoints, label = "straight line", color = 'blue')
plt.legend() ## labels and color won't show in plot without this line


randompoints = np.random.randint(1,1000,100)
plt.scatter(xpoints,randompoints, label ="random")

plt.show() ### to show the graph
#plt.savefig('Lecture Week 08 Plot') ## will save the plot as a png file