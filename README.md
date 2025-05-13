# Cross Database Housing Insights Platform

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
│   ├── config.json  
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
| `config.json`            | Save the Gemini API key                |

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

4. Navigate to the code/ folder and open **mysql_python.py**.
Update those 2 connection lines to match your MySQL setup:

```python
conn = pymysql.connect(host="localhost", user="root", password="YOUR_PASSWORD", autocommit=True)
```

```python
engine_apt = sqlalchemy.create_engine("mysql+pymysql://root:YOUR_PASSWORD@localhost/aptadditional")
```

5. Open **mongodb_aptinfo.py** and edit the following line with your MongoDB host info:

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
    1) Open the notebook LLM_implementation.ipynb, please run the very 1st cell to make sure you have the google-genai installed.
    ```python
    !pip install google-genai
    ```

    2) Place your **Google Gemini API key** in the file named `config.json` inside the same folder with LLM_implementation.ipynb:

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
    4) You may also need to edit the connection example in the AI prompt.

    ```text
    Assume mySQL has initialized as:
    apt = sqlalchemy.create_engine("mysql+pymysql://root:YOUR_PASSWORD@localhost/aptadditional")

    Assume MongoClient has been initialized as:
    client = MongoClient("mongodb://localhost:YOUR_PORT/")
    ```

    5) Run all cells in the notebook to initialize the interface.
    6) Here are some questions you can test on our Interface
    
    ***MySQL***

    **Schema Exploration**:

    - `What tables do I have in my MySQL database?`
    - `What are the columns in the amenities table?`
    - `How many listings stored in pricing table?`
    
    **Sample Queries & Query Execution**
    - `Show the cheapest apartment amenities and pets policy.`
    - `Show the top 3 most expensive apartments listing price, skipping the first 5.`
    - `Show listings id in USD and their price that cost more than 10000.`
    - `How many listings fall under each pets_allowed policy?` 
    - `What is the average price of listings that allow dogs?`
    - `Which pet rules have more than 1000 listings?`

    **Data Modification**
    - `Add a new listing with id ‘testobs’ and price in price table at 1500 USD.`
    - `Did the listing with ID 'testobs' get added in price table?`
    - `Update the price to 2000 for listing 'testobs' in the pricing table.` 
    - `Can you tell me the current price for listing ‘testobs’ from the pricing table display both id and price.`
    - `Please remove the listing with ID 'testobs' from the pricing table.` 
    - `Is the ‘testobs’ listing still in the pricing table?`

    ***MongoDB***

    **Schema Exploration**
    - `What collections are in the rental database?`
    - `What information does the location collection store? Show 1 example`

    **Sample Queries & Query Execution**
    - `Show me 3 apartment listings in Florida with exactly 2 bedrooms? I only need their ID, city name, state, number of bedrooms and square footage. `
    - `How many apartment listings are there in each state?`
    - `Which 5 cities have the highest number of apartment listings?`
    - `Show me 3 apartment listings in Tampa, but skip the first 3 results. I’d like to see their ID, title, and state. `
    - `Can you show me 5 apartment titles with cities they’re located in? `
    - `Show me the ID and square footage of 3 listings that are between 900 and 1000 square feet? `
    - `Find 5 listings in Orlando and only return their id and state.`

    **Data Modification**
    - `Add a new apartment to the listings with id ‘apt888’, titled ‘Oceanview Studio’, the description is ‘Quiet studio near the beach in Santa Monica’. `
    - `Find the listing with id ‘apt888’ and show its general info`
    - `Delete the listing with ID 'apt888' about its general info` 
    - `Insert two record into the sources collection: one with id ‘apt888’ and source ‘google’ and another with id ‘apt889’ and source ‘bing’.` 
    - `Update the source to ‘Yahoo’ for ID ‘apt888’.` 
    - `Show me the id and source for listing ‘apt888’ and ‘apt889’.`


 





