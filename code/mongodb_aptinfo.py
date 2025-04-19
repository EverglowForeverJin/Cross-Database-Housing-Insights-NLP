import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# Set the CSV file path
data_dir = "data/"
csv_path = data_dir + "final_dataset.csv"
df = pd.read_csv(csv_path)
df["time"] = pd.to_datetime(df["time"])

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Drop old project-related databases: rental, price, aptadditional
old_project_dbs = {"rental", "price", "aptadditional"}

for db_name in client.list_database_names():
    if db_name in old_project_dbs:
        client.drop_database(db_name)
        print(f"Dropped old project database: {db_name}")


#  Use only 'rental' database
rental_db = client["rental"]

# Drop old collections to avoid duplicates
rental_db.drop_collection("general_info")
rental_db.drop_collection("location")
rental_db.drop_collection("property_details")
rental_db.drop_collection("media")

# Insert into general_info
rental_db["general_info"].insert_many([
    {
        "id": row["id"],
        "title": row["title"],
        "body": row.get("body", "")  # Use "" if 'body' not present
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

client.close()
print("Done!!")
