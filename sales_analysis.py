import pandas as pd
import matplotlib.pyplot as plt

# Load the sales dataset
df = pd.read_csv("sales_data.csv")

# Display the dataset
print("Sales Data:")
print(df)

# Basic analysis
total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()

print("\nTotal Sales: ₹", total_sales)
print("Average Sales: ₹", round(average_sales, 2))

# Sales by product
product_sales = df.groupby("Product")["Sales"].sum()

print("\nSales by Product:")
print(product_sales)

# Create visualization
product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=0)
plt.tight_layout()

# Save chart
plt.savefig("sales_by_product.png")

plt.show()
