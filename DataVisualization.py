import matplotlib.pyplot as plt
import seaborn as sns

# Creating a scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.scatter(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.show()

# Creating a histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
sns.histplot(data, bins=5, kde=True)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()
