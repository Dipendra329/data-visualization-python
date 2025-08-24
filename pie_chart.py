import matplotlib.pyplot as plt

# take input from user
labels = input("Enter category names (space separated): ").split()
sizes = list(map(int, input("Enter Y values (space separated): ").split()))

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Bar chart')
plt.show()