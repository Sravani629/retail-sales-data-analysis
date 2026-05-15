import pandas as pd

# Load dataset
df = pd.read_excel("retail_sales_data.xlsx")

# Show data
print("First 5 rows:")
print(df.head())

# Check columns (important for debugging)
print("\nColumns in dataset:")
print(df.columns)

# Clean column names (recommended)
df.columns = df.columns.str.strip()

# Basic analysis
print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nCategory-wise Sales:")
print(df.groupby("Category")["Sales"].sum())

print("\nTop Selling Product:")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(1))
