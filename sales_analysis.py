import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet",
                "Laptop", "Phone", "Tablet", "Laptop"],
    "Sales": [75000, 45000, 30000, 82000, 50000, 35000,
              90000, 55000, 40000, 78000]
}

df = pd.DataFrame(data)

# Display the data
print("Sales Data:")
print(df)

# Basic analysis
print("\nTotal Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())

# Sales by product
product_sales = df.groupby("Product")["Sales"].sum()

print("\nSales by Product:")
print(product_sales)

# Create bar chart
product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("sales_by_product.png")
plt.show()
