# 📊 E-Commerce Sales Analytics Pipeline

An end-to-end analytics engineering project built using Python, PostgreSQL, SQL, and Streamlit to process, analyze, and visualize large-scale e-commerce transaction data.

This project automates data cleaning, performs KPI-driven business analysis, and delivers interactive dashboards for revenue, customer, and product insights.

---

# 🚀 Live Dashboard

(Add Streamlit deployment link here after deployment)

Example:

https://your-dashboard.streamlit.app

---

# 🧠 Project Overview

The objective of this project was to simulate a real-world analytics workflow used by modern e-commerce companies.

The pipeline includes:

- Automated ETL and preprocessing using Python
- PostgreSQL database integration
- SQL-based KPI analysis
- Interactive Streamlit dashboard
- Business insight generation
- Exploratory data analysis

The project processes large transactional datasets and transforms raw data into actionable business intelligence.

---

# 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data processing & analytics |
| Pandas | Data cleaning & transformation |
| PostgreSQL | Database storage |
| SQLAlchemy | Database connectivity |
| SQL | KPI analysis |
| Streamlit | Interactive dashboard |
| Plotly | Data visualization |
| Jupyter Notebook | EDA |
| Git & GitHub | Version control |

---

# 📂 Project Structure

```text
ecommerce-sales-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dashboards/
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
│   ├── app.py
│   └── requirements.txt
│
├── README.md
│
└── requirements.txt
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
- Feature engineering
- Dataset merging

---

## ✅ PostgreSQL Integration

- Automated database upload using SQLAlchemy
- Structured relational storage
- SQL-based querying

---

## ✅ KPI Analytics

Key metrics analyzed:

- Total Revenue
- Average Order Value
- Customer Distribution
- Revenue Trends
- SKU Contribution
- Product Performance
- Regional Revenue Analysis

---

## ✅ Interactive Dashboard

The Streamlit dashboard includes:

- Revenue overview
- Monthly sales trends
- State-wise revenue analysis
- Top-performing products
- Payment type distribution
- Dynamic filters & slicers

---

# 📊 Dashboard Preview

## Revenue Dashboard

(Add screenshot here)

```markdown
![Revenue Dashboard](assets/dashboard1.png)
```

---

## Customer Insights

(Add screenshot here)

```markdown
![Customer Dashboard](assets/dashboard2.png)
```

---

## Product Performance

(Add screenshot here)

```markdown
![Product Dashboard](assets/dashboard3.png)
```

---

# 🔍 Exploratory Data Analysis

EDA was conducted using Jupyter Notebook to identify:

- Seasonal demand patterns
- Revenue concentration
- Regional purchasing trends
- Product-level contribution
- Customer purchasing behavior

---

# 💡 Key Business Insights

- Q4 sales demonstrated strong seasonal growth compared to Q2 baseline periods.
- A relatively small percentage of SKUs contributed disproportionately to overall revenue.
- Urban regions generated the highest concentration of orders and revenue.
- Repeat customers showed significantly higher average transaction values.

---

# 📌 Future Improvements

- Real-time dashboard refresh
- Customer lifetime value prediction
- Sales forecasting
- Recommendation system
- Docker deployment
- Cloud database integration

---

# ▶️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ecommerce-sales-analytics.git
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configure PostgreSQL

Update database credentials inside:

```text
streamlit_app/app.py
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

# ⭐ If You Found This Useful

Consider starring the repository.