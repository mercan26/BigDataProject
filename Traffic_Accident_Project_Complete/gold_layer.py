from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["accidents_db"]
collection = db["clean_data"]

df = pd.DataFrame(list(collection.find()))

# Aggregation: Accidents by State
state_counts = df["State"].value_counts()
state_counts.plot(kind="bar", title="Accidents by State")
plt.tight_layout()
plt.savefig("sample_outputs/state_bar_chart.png")
plt.clf()

# Pie Chart: Severity distribution
severity_counts = df["Severity"].value_counts()
severity_counts.plot.pie(autopct="%1.1f%%", title="Severity Distribution")
plt.tight_layout()
plt.savefig("sample_outputs/severity_pie_chart.png")
