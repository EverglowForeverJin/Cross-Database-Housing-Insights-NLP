import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Final_project"]


files_collections = {
    "generalInfo.csv": "general_info",
    "propertyDetails.csv": "property_details",
    "pricing.csv": "pricing",
    "payment.csv": "price_details",
    "amenities_types.csv": "amenities",
    "amenities.csv": "property_amenities",
    "media.csv": "media",
    "sources.csv": "sources"
}

data_dir = "data/"

for file_name, collection_name in files_collections.items():
    path = data_dir + file_name
    print(f"📥 导入 {file_name} 到 Final_project.{collection_name}")
    
    df = pd.read_csv(path)
    records = df.to_dict("records")
    
    collection = db[collection_name]
    collection.delete_many({}) 
    if records:
        collection.insert_many(records)

print("✅ 所有数据已成功导入 Final_project 数据库")
