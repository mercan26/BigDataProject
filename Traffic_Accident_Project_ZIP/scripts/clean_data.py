import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["accidents_db"]

# Load raw data from MongoDB
raw_df = pd.DataFrame(list(db["raw_data"].find()))

# Drop rows with null Severity, State, or Weather_Condition
clean_df = raw_df.dropna(subset=["Severity", "State", "Weather_Condition"])

# Save clean data back to MongoDB
db["clean_data"].insert_many(clean_df.to_dict(orient="records"))
print(f"Cleaned data: {len(clean_df)} rows remaining.")