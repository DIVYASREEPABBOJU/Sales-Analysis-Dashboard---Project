
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

# Data Cleaning
df.dropna(inplace=True)

# KPI Metrics
total_revenue = df["Revenue"].sum()
total_orders = len(df)
top_product = df.groupby("Product")["Revenue"].sum().idxmax()

print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)
print("Top Product:", top_product)

# Revenue Trend
df["Date"] = pd.to_datetime(df["Date"])
monthly = df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum()

monthly.plot(kind="bar")
plt.title("Monthly Revenue Trend")
plt.tight_layout()
plt.savefig("revenue_trend.png")
plt.show()
