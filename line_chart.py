import matplotlib.pyplot as plt

# take input from user
x = list(map(int, input("Enter X values (space separated): ").split()))
y = list(map(int, input("Enter Y values (space separated): ").split()))

plt.plot(x, y)
plt.title('Custom line chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()