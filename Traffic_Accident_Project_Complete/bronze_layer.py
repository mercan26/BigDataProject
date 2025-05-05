import pandas as pd
from pymongo import MongoClient

# Load CSV (Replace filename as needed)
df = pd.read_csv("us_traffic_accidents.csv")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["accidents_db"]
collection = db["raw_data"]

# Convert to dict and insert into MongoDB
records = df.to_dict(orient="records")
collection.insert_many(records)

# Print confirmation
print(f"Inserted {len(records)} records into MongoDB")
