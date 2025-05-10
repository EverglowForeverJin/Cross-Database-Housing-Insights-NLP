import pymysql
import sqlalchemy
import pandas as pd

conn = pymysql.connect(host="localhost", user="root", password="YOUR_PASSWORD", autocommit=True)
cursor = conn.cursor()

cursor.execute("create database if not exists aptadditional;")

# additionalInfo database
cursor.execute("use aptadditional;")
cursor.execute("drop table if exists property_amenities;")
cursor.execute("drop table if exists amenities;")
cursor.execute("drop table if exists pricing;")
cursor.execute("drop table if exists price_details;")
cursor.execute("drop table if exists pets;")

cursor.execute("""
create table pricing (
    id varchar(100) primary key,
    price int,
    currency varchar(100)
);
""")

cursor.execute("""
create table amenities (
    amenity_id int auto_increment primary key,
    amenity_name varchar(100)
);
""")

cursor.execute("""
create table pets (
    id varchar(100) primary key,
    pets_allowed varchar(100),
    fee varchar(50),
    foreign key (id) references pricing(id) on delete cascade on update cascade
);
""")

cursor.execute("""
create table price_details (
    id varchar(100) primary key,
    price_display varchar(100),
    price_type varchar(100),
    foreign key (id) references pricing(id) on delete cascade on update cascade
);
""")

cursor.execute("""
create table property_amenities (
    id varchar(100),
    amenity_id int,
    primary key (id, amenity_id),
    foreign key (id) references pricing(id) on delete cascade on update cascade,
    foreign key (amenity_id) references amenities(amenity_id) on delete cascade on update cascade
);
""")

print("MySQL Database structure created successfully.")

# Load into aptadditional database
engine_apt = sqlalchemy.create_engine("mysql+pymysql://root:Dsci-551@localhost/aptadditional")

pd.read_csv("../data/pricing.csv").to_sql("pricing", con=engine_apt, if_exists="append", index=False, chunksize=1000)
print("Done pricing")

pd.read_csv("../data/payment.csv").to_sql("price_details", con=engine_apt, if_exists="append", index=False, chunksize=1000)
print("Done price_details")

pd.read_csv("../data/pets.csv").to_sql("pets", con=engine_apt, if_exists="append", index=False, chunksize=1000)
print("Done pets")

pd.read_csv("../data/amenities.csv").to_sql("amenities", con=engine_apt, if_exists="append", index=False, chunksize=1000)
print("Done amenities")

pd.read_csv("../data/amenities_types.csv").to_sql("property_amenities", con=engine_apt, if_exists="append", index=False, chunksize=1000)
print("Done property_amenities")

print("All imported.")
