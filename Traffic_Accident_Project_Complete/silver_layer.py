from pymongo import MongoClient
import pandas as pd

# Connect and load data
client = MongoClient("mongodb://localhost:27017/")
db = client["accidents_db"]
collection = db["raw_data"]

df = pd.DataFrame(list(collection.find()))

# Clean: drop rows with nulls in key columns
clean_df = df.dropna(subset=["Severity", "State", "Weather_Condition"])

# Save to new collection
clean_records = clean_df.to_dict(orient="records")
db["clean_data"].drop()  # Clear if exists
db["clean_data"].insert_many(clean_records)

print(f"Cleaned data contains {len(clean_records)} records")
