# DSCI551-Final-Project

In this project, we developed a natural language interface (NLI) for both RDBMS (MySQL) and NoSQL (MongoDB) databases using Google's Gemini 'gemini-2.0-flash' model, allowing users to ask questions about apartment rentals in natural sentences and based on our well-written prompt to identify the target database and generate corresponding queries/commands to access database data.

## Original Dataset
- **Dataset**: The original apartment dataset was downloaded from Kaggle. 99492 rows with 22 columns.
- **Columns**: 'id', 'category', 'title', 'body', 'amenities', 'bathrooms', 'bedrooms', 'currency', 'fee', 'has_photo', 'pets_allowed', 'price', 'price_display', 'price_type', 'square_feet', 'address', 'cityname', 'state', 'latitude', 'longitude', 'source', 'time'

## Cleaned Dataset
- Converted time column to proper datetime format using ‘to_datetime’
- Dropped ‘category’ and ‘address’ columns due to high missing values and redundancy.
- Filled all empty amenities as ‘No amenities’
- Filled all empty pets_allowed as ‘No pets allowed’
- Removed all na values and duplicate listing IDs.
- Filtered dataset to include only listings from 5 east coast states: ‘VA', 'NC', 'FL', 'MD', 'MA'
- **Final Dataset**: 30624 rows with 20 columns
- **Columns**: 'id', 'title', 'body', 'amenities', 'bathrooms', 'bedrooms', 'currency', 'fee', 'has_photo', 'pets_allowed', 'price', 'price_display', 'price_type', 'square_feet', 'cityname', 'state', 'latitude', 'longitude', 'source', 'time'

## Databases 
### MySQL: **aptadditional**
| Table Name         | Description                                      |
|---------------------|--------------------------------------------------|
| pricing (id, price, currency)    | Primary key: id|
| price_details (id, price_display, price_type) | Primary key: id. Foreign Key: id. One-to-one relationship|
| amenities (amenity_id, amenity_name)    | Primary key: amenity_id|
| property_amenities (id, amenity_id)    | Primary key: (id, amenity_id), both are also foreign keys|
| pets(id, pets_allowed, fee)    | Primary key: id. Foreign key: id. One-to-one relationship|

### MongoDB: **rental**
- general_info (id, title, body)
- location(id, cityname, state, latitude, longitude)
- property_details (id, square_feet, bedrooms, bathrooms)
- media (id, has_photo)
- sources (id, source, time)

## Google Drive Structrue
```
DSCI551_Final_Project/
├── data/
│   ├── amenities.csv
│   ├── amenities_types.csv
│   ├── apartments_for_rent_classified_100K.csv
│   ├── final_dataset.csv
│   ├── payment.csv
│   ├── pets.csv
│   └── pricing.csv
├── code/
│   ├── DSCI551_Final_Project.ipynb
│   ├── LLM_implementation.ipynb
│   ├── mongodb_aptinfo.py
│   └── mysql_python.py
├── requirements.txt
└── README.md
```

## File Descriptions

### 📁 data/
| Filename                                | Description                                           |
|----------------------------------------|-------------------------------------------------------|
| `amenities.csv`                         | Unique amenity types with assigned ID              |
| `amenities_types.csv`                  | Maps each apartment to its amenities                    |
| `apartments_for_rent_classified_100K.csv` | Original dataset downloaded from Kaggle        |
| `final_dataset.csv`                    | Cleaned dataset              |
| `payment.csv`                          | Payment methods and displayed price |
| `pets.csv`                             | Pet policies per apartment                            |
| `pricing.csv`                          | Rental pricing information                            |

### 📁 code/
| Filename                     | Description                                                                |
|-----------------------------|----------------------------------------------------------------------------|
| `DSCI551_Final_Project.ipynb` | Notebook for data preprocessing        |
| `LLM_implementation.ipynb`   | Natural Language Interface using LLM to query MySQL and MongoDB             |
| `mongodb_aptinfo.py`         | Script to load MongoDB database                                 |
| `mysql_python.py`            | Script to load MySQL database                |

### 📄 Other Files
| Filename            | Description                                      |
|---------------------|--------------------------------------------------|
| `requirements.txt`  | Lists Python packages required to run the project |
| `README.md`         | Project explanation and how to run our code    |

## How to run our code:
1. Download the entire `DSCI551_Final_Project` folder to your local machine from Google Drive.

2. Set Up Python Environment: You may use your system’s Python 

3. Install required packages using pip:

```bash
pip install -r requirements.txt
```

4. Navigate to the code/ folder and open mysql_python.py.
Update the connection line to match your MySQL setup:

```python
conn = pymysql.connect(host="localhost", user="root", password="YOUR_PASSWORD", autocommit=True)
```

5. Open mongodb_aptinfo.py and edit the following line with your MongoDB host info:

```python
client = MongoClient(host=['localhost:YOUR_PORT'])
```

6. Run the two scripts separately in your terminal to load MySQL and MongoDB databases.

```bash
python mysql_python.py  
python mongodb_aptinfo.py 
```
 **Note: Depending on your setup, you may need to use python3 instead.**

If loaded successfully, you will see confirmation messages in the terminal. You can also verify manually in your MySQL and MongoDB clients.

7. To use the LLM-based interface: 
    1) Open the notebook LLM_implementation.ipynb
    2) Place your **Google Gemini API key** in a file named `config.json` inside the same folder with LLM_implementation.ipynb:

    ```json
    {
    "API_KEY": "your_google_gemini_api_key"
    }
    ```

    3) Edit the database connection sections in the notebook to match your local configuration

    ```python
    # MySQL Connection
    apt = sqlalchemy.create_engine("mysql+pymysql://root:YOUR_PASSWORD@localhost/aptadditional")

    # MongoDB Connection
    client = MongoClient("mongodb://localhost:YOUR_PORT/")
    ```

    4) Run all cells in the notebook to initialize the interface.


