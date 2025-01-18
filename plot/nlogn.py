import matplotlib.pyplot as plt
import numpy as np

# Create a list of input sizes
n_values = np.linspace(1, 10, 10)

# Calculate the time complexity for each input size
time_complexity_1 = [1 for n in n_values]
time_complexity_n = list(n_values)
time_complexity_logn = [np.log(n) for n in n_values]
time_complexity_nlogn = [n * np.log(n) for n in n_values]
time_complexity_n2 = [n**2 for n in n_values]

# Plot the time complexity graph
plt.plot(n_values, time_complexity_1, label="O(1)")
plt.plot(n_values, time_complexity_n, label="O(n)")
plt.plot(n_values, time_complexity_logn, label="O(log n)")
plt.plot(n_values, time_complexity_nlogn, label="O(n log n)")
plt.plot(n_values, time_complexity_n2, label="O(n**2)")

plt.xlabel("Input size")
plt.ylabel("Time complexity")
plt.legend()
plt.show()
