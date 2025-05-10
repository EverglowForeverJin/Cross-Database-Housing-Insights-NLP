import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# Set the CSV file path
csv_path = "../data/final_dataset.csv"  
df = pd.read_csv(csv_path)
df["time"] = pd.to_datetime(df["time"])
print("Done")

# Connect to MongoDB 
client = MongoClient(host=['localhost:YOUR_PORT'])
print("Connected")

# Database 1: rental
rental_db = client["rental"]
rental_db.drop_collection("general_info")
rental_db.drop_collection("property_details")
rental_db.drop_collection("location")
rental_db.drop_collection("media")

# Insert into general_info
rental_db["general_info"].insert_many([
    {
        "id": row["id"],
        "title": row["title"],
        # Use "" if 'body' not present
        "body": row.get("body", "")
    }
    for _, row in df.iterrows()
])

# Insert into location
rental_db["location"].insert_many([
    {
        "id": row["id"],
        "cityname": row["cityname"],
        "state": row["state"],
        "latitude": row["latitude"],
        "longitude": row["longitude"]
    }
    for _, row in df.iterrows()
])

# Insert into property_details
rental_db["property_details"].insert_many([
    {
        "id": row["id"],
        "square_feet": row["square_feet"],
        "bedrooms": row["bedrooms"],
        "bathrooms": row["bathrooms"]
    }
    for _, row in df.iterrows()
])

# Insert into media
rental_db["media"].insert_many([
    {
        "id": row["id"],
        "has_photo": row["has_photo"]
    }
    for _, row in df.iterrows()
])

# Insert into sources
rental_db["sources"].insert_many([
    {
        "id": row["id"],
        "source": row["source"],
        "time": row["time"]
    }
    for _, row in df.iterrows()
])

client.close()
print("MongoDB import completed")
