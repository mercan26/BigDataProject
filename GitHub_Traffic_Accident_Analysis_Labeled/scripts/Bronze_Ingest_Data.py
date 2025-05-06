import pandas as pd
from pymongo import MongoClient

# Load CSV
df = pd.read_csv("data/US_Accidents.csv")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["accidents_db"]

# Drop existing collection if exists
if "raw_data" in db.list_collection_names():
    db["raw_data"].drop()

# Insert into MongoDB
db["raw_data"].insert_many(df.to_dict(orient="records"))

print(f"Ingested {len(df)} rows into MongoDB.")