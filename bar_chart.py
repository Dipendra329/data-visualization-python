import matplotlib.pyplot as plt

# take input from user
categories = input("Enter category names (space separated): ").split()
values = list(map(int, input("Enter Y values (space separated): ").split()))

plt.bar(categories, values)
plt.title('Bar chart')
plt.xlabel('categories')
plt.ylabel('values')
plt.show()