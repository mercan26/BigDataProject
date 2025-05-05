# US Traffic Accidents Big Data Project

This project uses MongoDB and Python to analyze 100,000 U.S. traffic accident records.

## Structure

- **scripts/**
  - `ingest.py`: Loads data into MongoDB
  - `clean_data.py`: Cleans records with missing values
  - `aggregate_and_visualize.py`: Creates charts
- **outputs/**: Visualizations (PNG)

## Instructions

1. Start MongoDB locally.
2. Place `US_Accidents_100k.csv` in the root directory.
3. Run the scripts in order:
   ```
   python scripts/ingest.py
   python scripts/clean_data.py
   python scripts/aggregate_and_visualize.py
   ```

## Output Charts

- Top 10 States by Number of Accidents
- Top 8 Weather Conditions
- Severity Level Pie Chart
