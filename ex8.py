import pandas as pd
import matplotlib.pyplot as plt

# Load the Wine Quality dataset
data = pd.read_csv("winequality-red.csv", delimiter=";")

# Print the first 5 rows
print("First 5 Rows:")
print(data.head())

# Print summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Create histograms for all features
data.hist(bins=50, figsize=(20, 15))
plt.suptitle("Histogram of Wine Quality Features")
plt.savefig("histogram.png")
plt.show()

# Create a scatter matrix to visualize relationships between features
pd.plotting.scatter_matrix(data, figsize=(20, 20))
plt.suptitle("Scatter Matrix of Wine Quality Features")
plt.savefig("scatter_matrix.png")
plt.show()
