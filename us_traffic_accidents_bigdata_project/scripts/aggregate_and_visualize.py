from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

client = MongoClient("mongodb://localhost:27017/")
db = client["trafficDB"]
collection = db["accidents_cleaned"]

# Aggregation 1: Top 10 states
agg1 = collection.aggregate([
    {"$group": {"_id": "$State", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}, {"$limit": 10}
])
df1 = pd.DataFrame(agg1)
df1.plot(kind="bar", x="_id", y="count", legend=False, title="Top 10 States by Accidents")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.savefig("outputs/top_states.png")
plt.clf()

# Aggregation 2: Weather condition frequency
agg2 = collection.aggregate([
    {"$group": {"_id": "$Weather_Condition", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}, {"$limit": 8}
])
df2 = pd.DataFrame(agg2)
df2.plot(kind="bar", x="_id", y="count", legend=False, title="Top Weather Conditions in Accidents")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.savefig("outputs/top_weather.png")
plt.clf()

# Aggregation 3: Severity pie chart
agg3 = collection.aggregate([
    {"$group": {"_id": "$Severity", "count": {"$sum": 1}}},
    {"$sort": {"_id": 1}}
])
df3 = pd.DataFrame(agg3)
plt.pie(df3["count"], labels=df3["_id"], autopct='%1.1f%%', startangle=140)
plt.title("Severity Distribution")
plt.savefig("outputs/severity_pie.png")
plt.clf()
