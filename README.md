# 📊 E-Commerce Sales Analytics Pipeline

An end-to-end analytics engineering project built using Python, PostgreSQL, SQL, and Streamlit to process, analyze, and visualize large-scale e-commerce transaction data.

This project simulates a real-world business analytics workflow used by modern e-commerce companies by automating data cleaning, performing KPI analysis, and generating interactive dashboards for revenue, customer, and product insights.

---

# 🚀 Live Demo

(https://ecommerce-sales-analyticssss.streamlit.app/)

---

# 🧠 Project Overview

The objective of this project was to transform raw transactional e-commerce data into actionable business insights through a complete analytics pipeline.

The workflow includes:

- Data preprocessing using Python and Pandas
- Exploratory Data Analysis (EDA)
- PostgreSQL database integration
- SQL-based KPI analysis
- Interactive dashboard development using Streamlit
- Business insight generation and reporting

The project processes large transaction datasets and visualizes meaningful patterns in customer behavior, sales trends, and product performance.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and analytics |
| Pandas | Data cleaning and transformation |
| PostgreSQL | Relational database storage |
| SQLAlchemy | Database connectivity |
| SQL | KPI querying and analysis |
| Streamlit | Interactive dashboard |
| Plotly | Data visualization |
| Jupyter Notebook | Exploratory Data Analysis |
| Git & GitHub | Version control and deployment |

---

# 📂 Project Structure

```text
ecommerce-sales-analytics/
│
├── assets/
│   ├── dashboard_overview.png
│   ├── revenue_analysis.png
│   ├── product_analysis.png
│   └── customer_insights.png
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── eda.ipynb
│
├── reports/
│   └── business_insights.md
│
├── scripts/
│   ├── data_cleaning.py
│   └── load_to_postgres.py
│
├── sql/
│   └── kpi_queries.sql
│
├── streamlit_app/
│   └── app.py
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Pipeline Architecture

```text
Raw CSV Data
      ↓
Python Data Cleaning Pipeline
      ↓
Processed Dataset
      ↓
PostgreSQL Database
      ↓
SQL KPI Analysis
      ↓
Interactive Streamlit Dashboard
      ↓
Business Insights & Reporting
```

---

# 📈 Features

## ✅ Automated Data Cleaning Pipeline

- Missing value handling
- Duplicate removal
- Datetime conversion
- Dataset merging
- Feature engineering
- Standardized preprocessing workflow

---

## ✅ PostgreSQL Integration

- Structured relational database storage
- Automated upload pipeline using SQLAlchemy
- SQL querying for KPI generation

---

## ✅ KPI Analytics

Key metrics analyzed:

- Total Revenue
- Total Orders
- Average Order Value
- Revenue Trends
- Customer Distribution
- Product Performance
- State-wise Revenue Analysis
- Payment Distribution

---

## ✅ Interactive Streamlit Dashboard

The dashboard includes:

- Revenue overview
- KPI cards
- Monthly revenue trends
- State-wise sales analysis
- Top-performing products
- Payment method distribution
- Interactive filters and slicers

---

# 📊 Dashboard Preview

## Main Dashboard

<img width="1914" height="968" alt="dashboard_overview" src="https://github.com/user-attachments/assets/088ac2ab-ce03-40bc-969f-389f0db088b3" />


---

## Revenue Analysis

<img width="1510" height="617" alt="revenue_analysis" src="https://github.com/user-attachments/assets/318028df-d577-4b8e-b353-23c01f9a3bc9" />


---

## Product Performance

<img width="1520" height="608" alt="product_analysis" src="https://github.com/user-attachments/assets/0dd57412-4ff4-4665-96af-e90f70d9230f" />


---

## Customer Insights

<img width="1518" height="559" alt="customer_insights" src="https://github.com/user-attachments/assets/1c1cb56a-6510-4d9c-b345-90305f3a6807" />


---

# 🔍 Exploratory Data Analysis

EDA was performed using Jupyter Notebook to identify:

- Seasonal demand patterns
- Revenue concentration trends
- Customer purchasing behavior
- Regional sales distribution
- Product-level contribution analysis

---

# 💡 Key Business Insights

- Q4 sales demonstrated strong seasonal growth compared to earlier quarters.
- A relatively small percentage of products generated a disproportionately high share of revenue.
- Urban regions contributed the highest concentration of orders and revenue.
- Repeat customers showed higher average transaction values than one-time buyers.

---

# 📌 Future Improvements

- Real-time dashboard refresh
- Customer lifetime value prediction
- Sales forecasting using machine learning
- Recommendation system integration
- Docker containerization
- Cloud database deployment

---

# ▶️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ecommerce-sales-analytics.git
```

---

## 2️⃣ Navigate to Project Directory

```bash
cd ecommerce-sales-analytics
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Streamlit Dashboard

```bash
streamlit run streamlit_app/app.py
```

---

# 📚 Dataset

Dataset used:

Brazilian E-Commerce Public Dataset by Olist

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

# 👨‍💻 Author

Avnish

---

# ⭐ Support

If you found this project useful, consider giving the repository a star.
