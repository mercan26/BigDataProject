import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["accidents_db"]

# Load cleaned data
df = pd.DataFrame(list(db["clean_data"].find()))

# Visualization 1: Accidents by State
state_counts = df["State"].value_counts()
state_counts.plot(kind="bar", figsize=(12,6), title="Accidents by State")
plt.tight_layout()
plt.savefig("../screenshots/accidents_by_state.png")

# Visualization 2: Severity Distribution
severity_counts = df["Severity"].value_counts()
severity_counts.plot.pie(autopct="%1.1f%%", title="Severity Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("../screenshots/severity_distribution.png")