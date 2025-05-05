import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["trafficDB"]
collection = db["accidents"]

# Load CSV
df = pd.read_csv("US_Accidents_100k.csv")

# Convert to dictionary and insert into MongoDB
collection.drop()  # Clean slate
collection.insert_many(df.to_dict(orient="records"))

# Count rows and columns
print("Rows in collection:", collection.count_documents({}))
print("Columns:", df.shape[1])
