import pandas as pd

data = pd.read_csv('/Users/consultadd/Desktop/File Handling/sales_data_sample.csv', encoding='ISO-8859-1')
print(data.head())

# Calculate total sales, average sales, etc.
total_sales = data['SALES'].sum()
average_sales = data['SALES'].mean()
max_sales = data['SALES'].max()
min_sales = data['SALES'].min()

# Print the statistics
print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales}")
print(f"Max Sales: {max_sales}")
print(f"Min Sales: {min_sales}")
