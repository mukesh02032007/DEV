import datetime
import random
import pandas as pd
import matplotlib.pyplot as plt
import radar
from faker import Faker

# Create Faker object
fake = Faker()

# Function to generate sample data
def generateData(n):
    listdata = []

    start = datetime.datetime(2019, 8, 1)
    end = datetime.datetime(2019, 8, 30)

    for _ in range(n):
        date = radar.random_datetime(
            start="2019-08-01",
            stop="2019-08-30"
        ).strftime("%Y-%m-%d")

        price = round(random.uniform(900, 1000), 4)

        listdata.append([date, price])

    return listdata


# Generate 100 sample records
data = generateData(100)

# Create DataFrame
df = pd.DataFrame(data, columns=["Date", "Price"])

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")

# Group by Date and calculate mean Price
df = df.groupby("Date").mean()

# Plot settings
plt.rcParams["figure.figsize"] = (14, 10)

# Plot graph
plt.plot(df.index, df["Price"], marker="o")

# Labels and title
plt.title("Average Daily Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)

# Save graph
plt.savefig("price_graph.png")

# Display graph
plt.show()
