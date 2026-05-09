import streamlit as st
import pandas as pd
import plotly.express as px


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    layout="wide"
)

# -----------------------------
# DATABASE CONNECTION
# -----------------------------

from urllib.parse import quote_plus


# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/processed/final_dataset.csv")

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("Filters")

selected_state = st.sidebar.multiselect(
    "Select State",
    options=df["customer_state"].dropna().unique(),
    default=df["customer_state"].dropna().unique()
)

# Filter data
filtered_df = df[
    df["customer_state"].isin(selected_state)
]

# -----------------------------
# TITLE
# -----------------------------

st.title("📊 E-Commerce Sales Analytics Dashboard")

# -----------------------------
# KPI METRICS
# -----------------------------

total_revenue = filtered_df["payment_value"].sum()

total_orders = filtered_df["order_id"].nunique()

total_customers = filtered_df["customer_unique_id"].nunique()

avg_order_value = filtered_df["payment_value"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")

col2.metric("Total Orders", total_orders)

col3.metric("Total Customers", total_customers)

col4.metric("Avg Order Value", f"${avg_order_value:.2f}")

# -----------------------------
# MONTHLY REVENUE
# -----------------------------

monthly_sales = filtered_df.groupby("month")[
    "payment_value"
].sum().reset_index()

fig1 = px.line(
    monthly_sales,
    x="month",
    y="payment_value",
    title="Monthly Revenue Trend"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# TOP STATES
# -----------------------------

state_sales = filtered_df.groupby("customer_state")[
    "payment_value"
].sum().reset_index()

fig2 = px.bar(
    state_sales,
    x="customer_state",
    y="payment_value",
    title="Revenue by State"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# TOP PRODUCTS
# -----------------------------

top_products = filtered_df.groupby("product_id")[
    "payment_value"
].sum().reset_index()

top_products = top_products.sort_values(
    by="payment_value",
    ascending=False
).head(10)

fig3 = px.bar(
    top_products,
    x="product_id",
    y="payment_value",
    title="Top Products"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# PAYMENT TYPE DISTRIBUTION
# -----------------------------

payment_dist = filtered_df.groupby("payment_type")[
    "payment_value"
].sum().reset_index()

fig4 = px.pie(
    payment_dist,
    names="payment_type",
    values="payment_value",
    title="Payment Type Distribution"
)

st.plotly_chart(fig4, use_container_width=True)