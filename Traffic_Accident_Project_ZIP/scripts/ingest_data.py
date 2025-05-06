import pandas as pd
from pymongo import MongoClient

# Load data
file_path = "../us_traffic_accidents.csv"
df = pd.read_csv(file_path)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["accidents_db"]

# Insert raw data into MongoDB
db["raw_data"].insert_many(df.to_dict(orient="records"))
print(f"Inserted {len(df)} records into MongoDB.")