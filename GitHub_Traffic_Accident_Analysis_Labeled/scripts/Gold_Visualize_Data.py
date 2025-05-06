import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["accidents_db"]

# Read from clean_data
df = pd.DataFrame(list(db["clean_data"].find()))

# Accidents by State
state_counts = df["State"].value_counts().head(10)
plt.figure(figsize=(10, 6))
state_counts.plot(kind="bar", title="Top 10 States with Most Accidents", color="skyblue")
plt.xlabel("State")
plt.ylabel("Accident Count")
plt.tight_layout()
plt.savefig("visualizations/accidents_by_state.png")
plt.close()

# Severity distribution
severity_counts = df["Severity"].value_counts()
plt.figure(figsize=(6, 6))
severity_counts.plot.pie(autopct="%1.1f%%", title="Severity Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/severity_distribution.png")
plt.close()

print("Visualizations saved in visualizations/")