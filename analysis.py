import pandas as pd

# Load dataset
df = pd.read_excel("Microsoft Excel (.xlsx).xlsx")

# Basic analysis
print("First 5 rows:")
print(df.head())

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nCategory-wise Sales:")
print(df.groupby("Category")["Sales"].sum())

print("\nTop Selling Product:")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(1))
