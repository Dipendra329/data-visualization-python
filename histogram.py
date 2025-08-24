import matplotlib.pyplot as plt
import numpy as np

data = list(map(int, input("Enter numbers (space separated): ").split()))


plt.hist(data, bins=5, edgecolor='black')
plt.title('Histogram')
plt.xlabel('values')
plt.ylabel('Frequency')
plt.show()