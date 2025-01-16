
import pandas as pd

# Load the sales data
df = pd.read_csv("sales_data.csv")

# Clean the data
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Adding new columns for Month and Year
df['Month'] = pd.to_datetime(df['Date']).dt.month
df['Year'] = pd.to_datetime(df['Date']).dt.year

# Grouping data by Region and Month for trend analysis
monthly_sales = df.groupby(['Region', 'Month'])['Sales Amount'].sum().reset_index()
print(monthly_sales)
