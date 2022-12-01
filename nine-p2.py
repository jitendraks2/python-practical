import matplotlib.pyplot as plt
import numpy as np

p = np.arange(1, 11)
q = p * p
# plotting
plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(p, q, color ="red")
plt.show()