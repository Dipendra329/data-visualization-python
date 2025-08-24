import matplotlib.pyplot as plt
import numpy as np

labels = np.array(['A', 'B', 'C', 'D', 'E'])
data1 = np.array([4, 5, 3, 4, 2])
data2 = np.array([3, 4, 4, 2, 5])

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
data1 = np.concatenate((data1, [data1[0]]))
data2 = np.concatenate((data2, [data2[0]]))
angles = np.concatenate((angles, [angles[0]]))

fig, ax = plt.subplots(subplot_kw={'polar': True})
ax.plot(angles, data1, marker='o', color='blue', label='Student 1')
ax.fill(angles, data1, color='blue', alpha=0.25)
ax.plot(angles, data2, marker='s', color='orange', label='Student 2')
ax.fill(angles, data2, color='orange', alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
plt.title('Radar Chart - Comparison', size=14, weight='bold')
plt.show()