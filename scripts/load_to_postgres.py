import pandas as pd
from sqlalchemy import create_engine

# Load processed dataset
df = pd.read_csv("data/processed/final_dataset.csv")

# PostgreSQL connection
username = "postgres"
from urllib.parse import quote_plus

password = quote_plus("ajit@123at")
host = "localhost"
port = "5432"
database = "ecommerce"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# Upload dataframe to PostgreSQL
df.to_sql(
    "final_dataset",
    engine,
    if_exists="replace",
    index=False
)

print("Data imported successfully")