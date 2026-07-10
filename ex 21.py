# Exploratory Data Analysis on Email Dataset

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the email dataset
df = pd.read_csv("emails.csv")

# Display first five records
print("First Five Emails:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate emails
df = df.drop_duplicates()

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Extract useful date information
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month_name()
df["Day"] = df["Date"].dt.day_name()
df["Hour"] = df["Date"].dt.hour

# ------------------------------------
# 1. Top Email Senders
# ------------------------------------

top_senders = df["From"].value_counts().head(10)

print("\nTop Email Senders:")
print(top_senders)

top_senders.plot(
    kind="bar",
    title="Top Email Senders"
)

plt.xlabel("Email Sender")
plt.ylabel("Number of Emails")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ------------------------------------
# 2. Emails Received by Month
# ------------------------------------

monthly_emails = df["Month"].value_counts()

monthly_emails.plot(
    kind="bar",
    title="Emails Received by Month"
)

plt.xlabel("Month")
plt.ylabel("Number of Emails")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ------------------------------------
# 3. Emails Received by Day
# ------------------------------------

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

daily_emails = df["Day"].value_counts().reindex(
    day_order,
    fill_value=0
)

daily_emails.plot(
    kind="line",
    marker="o",
    title="Email Activity by Day"
)

plt.xlabel("Day")
plt.ylabel("Number of Emails")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()


# ------------------------------------
# 4. Email Distribution by Label
# ------------------------------------

label_count = df["Label"].value_counts()

label_count.plot(
    kind="pie",
    autopct="%1.1f%%",
    title="Email Distribution by Category"
)

plt.ylabel("")
plt.tight_layout()
plt.show()


# ------------------------------------
# 5. Subject Length Analysis
# ------------------------------------

df["Subject_Length"] = (
    df["Subject"]
    .fillna("")
    .str.len()
)

df["Subject_Length"].plot(
    kind="hist",
    bins=10,
    edgecolor="black",
    title="Distribution of Email Subject Length"
)

plt.xlabel("Number of Characters")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# Display statistical information
print("\nEmail Dataset Statistics:")
print(df.describe())

# Save the cleaned email dataset
df.to_csv(
    "cleaned_email_dataset.csv",
    index=False
)

print("\nEDA completed successfully.")
print("Cleaned dataset exported successfully.")