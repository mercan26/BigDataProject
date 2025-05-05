# Distributed Big Data Application: U.S. Traffic Accident Analysis

## Overview
This project analyzes U.S. traffic accident data using MongoDB and Python (PyMongo + Pandas + Matplotlib). It follows the Bronze-Silver-Gold data pipeline strategy and includes data ingestion, cleaning, aggregation, and visualization.

## Tools Used
- MongoDB (Big Data DB)
- Python (Pandas, PyMongo, Matplotlib)
- Jupyter for initial analysis
- GitHub for version control

## Project Structure
- `bronze_layer.py`: Ingest and load data into MongoDB
- `silver_layer.py`: Clean and filter data
- `gold_layer.py`: Perform aggregation and visualization
- `sample_outputs/`: Folder to store example screenshots
- `README.md`: Project overview

## Example Screenshots

### 1. Raw Data Sample (Bronze Layer)
```python
print(df.head())
```

### 2. Cleaned Data Sample (Silver Layer)
```python
clean_df = df.dropna(subset=["Severity", "State", "Weather_Condition"])
print(clean_df.describe())
```

### 3. Aggregation: Accidents per State (Gold Layer)
```python
state_counts = clean_df["State"].value_counts()
state_counts.plot(kind="bar", title="Accidents by State")
```

### 4. Visualization: Pie Chart of Accident Severity
```python
severity_counts = clean_df["Severity"].value_counts()
severity_counts.plot.pie(autopct="%1.1f%%", title="Severity Distribution")
```

## How to Use
1. Replace `us_traffic_accidents.csv` with your actual dataset (≥ 100K rows).
2. Run `bronze_layer.py` to load data into MongoDB.
3. Run `silver_layer.py` to clean data.
4. Run `gold_layer.py` to generate visualizations.
5. Record the steps for a 5–6 minute walkthrough video.

## Your Task
- Add screenshots of code and output to `sample_outputs/`
- Replace CSV name in scripts with actual file name.
- Push this structure to your GitHub repo.
- Record and upload an unlisted YouTube video.

