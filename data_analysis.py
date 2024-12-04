# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Step 1: Load the dataset
data_path = 'ecommerce_sales.csv'  # Replace with your dataset path
df = pd.read_csv(data_path)

# Step 2: Data Cleaning
# Convert 'Order Date' column to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Drop rows where 'Order Date' is invalid (NaT) after conversion
df.dropna(subset=['Order Date'], inplace=True)

# Remove rows with invalid or negative values in 'Quantity' and 'Price'
df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]

# Step 3: Add Derived Columns
# Extract month from 'Order Date'
df['Month'] = df['Order Date'].dt.month

# Calculate revenue (Quantity * Price)
df['Revenue'] = df['Quantity'] * df['Price']

# Step 4: Answer Questions and Analyze Data
# 4a. Top 5 Most Sold Products (by Quantity)
top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)

# 4b. Monthly Revenue (Total Revenue per Month)
monthly_revenue = df.groupby('Month')['Revenue'].sum().sort_index()

# 4c. Most Profitable Products (by Revenue)
most_profitable = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(5)

# Step 5: Visualizations
# 5a. Monthly Revenue Visualization
plt.figure(figsize=(10, 6))
monthly_revenue.plot(kind='bar', color='skyblue')
plt.title('Monthly Revenue (INR)')
plt.xlabel('Month')
plt.ylabel('Total Revenue (₹)')
plt.xticks(ticks=range(len(monthly_revenue.index)), labels=[f'Month {month}' for month in monthly_revenue.index], rotation=45)

# Format the y-axis to display full numbers (with commas)
ax = plt.gca()  # Get current axis
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))  # Format y-axis with commas

plt.tight_layout()
plt.savefig("monthly_revenue_chart.png")  # Save the chart as a file
plt.show()

# 5b. Top 5 Products by Quantity Visualization
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='orange')
plt.title('Top 5 Most Sold Products')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_products_chart.png")  # Save the chart as a file
plt.show()

# 5c. Most Profitable Products Visualization
plt.figure(figsize=(10, 6))
most_profitable.plot(kind='bar', color='green')
plt.title('Top 5 Most Profitable Products (INR)')
plt.xlabel('Product')
plt.ylabel('Revenue (₹)')
plt.xticks(rotation=45)

# Format the y-axis to display full numbers (with commas)
ax = plt.gca()  # Get current axis
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))  # Format y-axis with commas

plt.tight_layout()
plt.savefig("most_profitable_products_chart.png")  # Save the chart as a file
plt.show()

# Step 6: Summary of Insights
print("\nSummary of Insights:")
print("- The top-selling products are:")
print(top_products)
print("\n- Monthly revenue breakdown (₹):")
for month, revenue in monthly_revenue.items():
    print(f"Month {month}: ₹ {revenue:,.2f}")
print("\n- The month with the highest revenue is:")
print(f"Month {monthly_revenue.idxmax()} with a total revenue of ₹ {monthly_revenue.max():,.2f}")
print("\n- The most profitable products are:")
print(most_profitable)
