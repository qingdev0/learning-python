import matplotlib.pyplot as plt
import numpy as np

f = lambda p: -np.log(p / 10000.0)
x = np.arange(1, 10000)

plt.scatter(x, f(x))
plt.show()