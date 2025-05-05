from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["trafficDB"]
bronze = db["accidents"]
silver = db["accidents_cleaned"]
silver.drop()

cursor = bronze.find({
    "City": {"$ne": None},
    "State": {"$ne": None},
    "Severity": {"$ne": None},
    "Temperature(F)": {"$ne": None},
    "Weather_Condition": {"$ne": None}
})

cleaned_data = []
for doc in cursor:
    doc.pop("_id", None)
    cleaned_data.append(doc)

if cleaned_data:
    silver.insert_many(cleaned_data)

print("Cleaned rows inserted:", silver.count_documents({}))
