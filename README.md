# DSCI551-Final-Project

In this project, we developed a natural language interface (NLI) for both RDBMS (MySQL) and NoSQL (MongoDB) databases using Google's Gemini 'gemini-2.0-flash' model, allowing users to ask questions about apartment rentals in natural sentences and based on our well-written prompt to identify the target database and generate corresponding queries/commands to access database data.

### Original Dataset
- Dataset: The original apartment dataset was downloaded from Kaggle.
- 99492 rows with 22 columns
- Columns: 'id', 'category', 'title', 'body', 'amenities', 'bathrooms', 'bedrooms', 'currency', 'fee', 'has_photo', 'pets_allowed', 'price', 'price_display', 'price_type', 'square_feet', 'address', 'cityname', 'state', 'latitude', 'longitude', 'source', 'time'

### Cleaned Dataset
- Converted time column to proper datetime format using ‘to_datetime’
- Dropped ‘category’ and ‘address’ columns due to high missing values and redundancy.
- Filled all empty amenities as ‘No amenities’
- Filled all empty pets_allowed as ‘No pets allowed’
- Removed all na values and duplicate listing IDs.
- Filtered dataset to include only listings from 5 east coast states: ‘VA', 'NC', 'FL', 'MD', 'MA'
- 30624 rows with 20 columns
- Columns: 'id', 'title', 'body', 'amenities', 'bathrooms', 'bedrooms', 'currency', 'fee', 'has_photo', 'pets_allowed', 'price', 'price_display', 'price_type', 'square_feet', 'cityname', 'state', 'latitude', 'longitude', 'source', 'time'

### MySQL 
Database: aptadditional
- pricing (id, price, currency)
-   Primary key: id
- price_details (id, price_display, price_type)
-  Primary key: id. Foreign Key: id
-  One-to-one relationship
- amenities (amenity_id, amenity_name)
-  Primary key: amenity_id
- property_amenities (id, amenity_id)
-  Primary key: (id, amenity_id), both are also foreign keys
- pets(id, pets_allowed, fee)
-  Primary key: id. Foreign key: id
-  One-to-one relationship


### MongoDB 
Database 1: rental
- general_info (id, title, body)
- location(id, cityname, state, latitude, longitude)
- property_details (id, square_feet, bedrooms, bathrooms)
- media (id, has_photo)
- sources (id, source, time)

## 


