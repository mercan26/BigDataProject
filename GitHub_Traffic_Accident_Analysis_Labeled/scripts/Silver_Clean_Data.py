import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["accidents_db"]

# Read from raw_data
df = pd.DataFrame(list(db["raw_data"].find()))

# Clean the data
df = df.dropna(subset=["Severity", "State", "Weather_Condition"])

# Drop existing clean collection
if "clean_data" in db.list_collection_names():
    db["clean_data"].drop()

# Insert cleaned data
db["clean_data"].insert_many(df.to_dict(orient="records"))

print(f"Cleaned data: {len(df)} rows remaining.")