# Mall Customer Segmentation - Data Cleaning

import pandas as pd

# Load dataset
df = pd.read_csv("Mall_Customers.csv")
df.head()

# Drop empty column
df = df.drop(columns=["Unnamed: 5"])

# Check for duplicates
print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

# Standardize Gender column
df["Gender"] = df["Gender"].str.strip().str.lower()
print(df["Gender"].unique())

# Rename columns
df.rename(columns={
    "CustomerID": "customer_id",
    "Gender": "gender",
    "Age": "age",
    "Annual Income (k$)": "annual_income_k$",
    "Spending Score (1-100)": "spending_score"
}, inplace=True)

# Check data types
print(df.dtypes)

# Save cleaned dataset
df.to_csv("Mall_Customers_Cleaned.csv", index=False)
print("Cleaned dataset saved as Mall_Customers_Cleaned.csv")
