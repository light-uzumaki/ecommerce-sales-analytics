import pandas as pd
import os

# Load datasets
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
payments = pd.read_csv("data/raw/olist_order_payments_dataset.csv")
products = pd.read_csv("data/raw/olist_products_dataset.csv")

print("Datasets loaded successfully")

# Handle missing values
products["product_category_name"].fillna("Unknown", inplace=True)

# Remove duplicates
orders.drop_duplicates(inplace=True)

# Convert date columns
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

# Feature engineering
orders["month"] = orders["order_purchase_timestamp"].dt.month
orders["year"] = orders["order_purchase_timestamp"].dt.year

# Merge datasets
merged = orders.merge(
    customers,
    on="customer_id",
    how="left"
)

merged = merged.merge(
    items,
    on="order_id",
    how="left"
)

merged = merged.merge(
    payments,
    on="order_id",
    how="left"
)

merged = merged.merge(
    products,
    on="product_id",
    how="left"
)

# Create processed folder if not exists
os.makedirs("data/processed", exist_ok=True)

# Save processed dataset
merged.to_csv(
    "data/processed/final_dataset.csv",
    index=False
)

print("Final dataset saved successfully")
print("Shape:", merged.shape)