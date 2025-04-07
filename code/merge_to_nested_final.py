from pymongo import MongoClient

# Connect  database
client = MongoClient("mongodb://localhost:27017/")
db = client["Final_project"]


general_info = db["general_info"].find()
property_details = {doc["id"]: doc for doc in db["property_details"].find()}
pricing = {doc["id"]: doc for doc in db["pricing"].find()}
price_details = {doc["id"]: doc for doc in db["price_details"].find()}
media = {doc["id"]: doc for doc in db["media"].find()}
sources = {doc["id"]: doc for doc in db["sources"].find()}

# ✅ amenities_types collection → facility id and name mapping table
amenities = {
    doc["amenity_id"]: doc.get("type", f"amenity_{doc['amenity_id']}")
    for doc in db["amenities_types"].find()
}

# ✅ property_amenities 集合：构建 {property_id: [amenity_name1, amenity_name2]} 映射
property_amenities = {}
for doc in db["property_amenities"].find():
    pid = doc.get("property_id") or doc.get("id")
    aid = doc["amenity_id"]
    if pid not in property_amenities:
        property_amenities[pid] = []
    property_amenities[pid].append(amenities.get(aid, f"amenity_{aid}"))

# delect old database
db["final_apartments"].delete_many({})

# Merge and insert documents
for doc in general_info:
    _id = doc["id"]

    final_doc = {
        "id": _id,
        "title": doc.get("title"),
        "cityname": doc.get("cityname"),
        "state": doc.get("state"),
        "latitude": doc.get("latitude"),
        "longitude": doc.get("longitude"),
        "square_feet": doc.get("square_feet"),

        "details": {
            "bedrooms": property_details.get(_id, {}).get("bedrooms"),
            "bathrooms": property_details.get(_id, {}).get("bathrooms"),
            "pets_allowed": property_details.get(_id, {}).get("pets_allowed")
        },

        "price": {
            "amount": pricing.get(_id, {}).get("price"),
            "currency": pricing.get(_id, {}).get("currency"),
            "display": price_details.get(_id, {}).get("price_display"),
            "type": price_details.get(_id, {}).get("price_type")
        },

        "media": {
            "has_photo": media.get(_id, {}).get("has_photo")
        },

        "amenities": property_amenities.get(_id, []),
        "source": sources.get(_id, {}).get("source")
    }

    db["final_apartments"].insert_one(final_doc)

print("✅ 所有数据已成功合并到 Final_project.final_apartments 集合！")
