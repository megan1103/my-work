# Messing with Pie Charts
# Author: Megan O'Donovan

import numpy as np
import matplotlib.pyplot as plt

fruit = np.array(['Apple', 'Orange', 'Banana'])
numbers = np.array([23,77,50])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()