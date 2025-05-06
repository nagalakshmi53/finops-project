import boto3
import sqlite3
from datetime import datetime, timedelta

# AWS Setup
client = boto3.client('ce')  # Cost Explorer

# Date range
end = datetime.utcnow().date()
start = end - timedelta(days=1)

# Fetch cost data
response = client.get_cost_and_usage(
    TimePeriod={
        'Start': start.isoformat(),
        'End': end.isoformat()
    },
    Granularity='DAILY',
    Metrics=['UnblendedCost'],
    GroupBy=[
        {'Type': 'DIMENSION', 'Key': 'SERVICE'}
    ]
)

# SQLite setup
conn = sqlite3.connect("cloud_usage.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usage (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        service TEXT,
        cost REAL
    )
''')

# Insert data
for group in response['ResultsByTime'][0]['Groups']:
    service = group['Keys'][0]
    cost = float(group['Metrics']['UnblendedCost']['Amount'])
    cursor.execute("INSERT INTO usage (date, service, cost) VALUES (?, ?, ?)",
                   (start.isoformat(), service, cost))

conn.commit()
conn.close()

print("Data fetched and stored successfully.")
