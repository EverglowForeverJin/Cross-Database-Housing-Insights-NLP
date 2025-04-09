import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# === Set the CSV file path ===
data_dir = "data/"
csv_path = data_dir + "final_dataset.csv"
df = pd.read_csv(csv_path)
df["time"] = pd.to_datetime(df["time"])

# === Split the amenities field ===
unique_amenities = set()
property_amenities_map = {}

for _, row in df.iterrows():
    pid = row["id"]
    amenity_list = [a.strip() for a in row["amenities"].split(",") if a.strip() and a.strip().lower() != "no amenties"]
    for amenity in amenity_list:
        unique_amenities.add(amenity)
        property_amenities_map.setdefault(pid, []).append(amenity)

amenity_id_map = {name: idx + 1 for idx, name in enumerate(sorted(unique_amenities))}

# === connect MongoDB ===
client = MongoClient("mongodb://localhost:27017/")

# === Database 1: rental ===
rental_db = client["rental"]
rental_db.drop_collection("general_info")
rental_db.drop_collection("property_details")
rental_db.drop_collection("amenities")
rental_db.drop_collection("property_amenities")

rental_db["general_info"].insert_many([
    {
        "id": row["id"],
        "title": row["title"],
        "cityname": row["cityname"],
        "state": row["state"],
        "latitude": row["latitude"],
        "longitude": row["longitude"]
    }
    for _, row in df.iterrows()
])

rental_db["property_details"].insert_many([
    {
        "id": row["id"],
        "square_feet": row["square_feet"],
        "bedrooms": row["bedrooms"],
        "bathrooms": row["bathrooms"],
        "pets_allowed": row["pets_allowed"]
    }
    for _, row in df.iterrows()
])

rental_db["amenities"].insert_many([
    {
        "amenity_id": amenity_id_map[name],
        "amenity_name": name
    }
    for name in amenity_id_map
])

rental_db["property_amenities"].insert_many([
    {
        "id": pid,
        "amenity_id": amenity_id_map[an]
    }
    for pid, amenities in property_amenities_map.items()
    for an in amenities
])

# === Database 2: price ===
price_db = client["price"]
price_db.drop_collection("pricing")
price_db.drop_collection("price_details")

price_db["pricing"].insert_many([
    {
        "id": row["id"],
        "price": row["price"],
        "currency": row["currency"]
    }
    for _, row in df.iterrows()
])

price_db["price_details"].insert_many([
    {
        "id": row["id"],
        "price_display": row["price_display"],
        "price_type": row["price_type"]
    }
    for _, row in df.iterrows()
])

# === Database 3: aptadditional ===
apt_db = client["aptadditional"]
apt_db.drop_collection("media")
apt_db.drop_collection("sources")

apt_db["media"].insert_many([
    {
        "id": row["id"],
        "has_photo": row["has_photo"]
    }
    for _, row in df.iterrows()
])

apt_db["sources"].insert_many([
    {
        "id": row["id"],
        "source": row["source"],
        "time": row["time"]
    }
    for _, row in df.iterrows()
])

client.close()
print("The data has been successfully split and written into the three databases of rental, price, and aptadditional in MongoDB!")
