# Messing with Histograms
# Author: Megan O'Donovan

import numpy as np
import matplotlib.pyplot as plt

#np.random.seed(1)
normData = np.random.normal(size =10)
plt.hist(normData)
plt.show()