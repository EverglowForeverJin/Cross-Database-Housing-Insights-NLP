import pymysql
import sqlalchemy
import pandas as pd

conn = pymysql.connect(host="localhost", user="root", password="Dsci-551", autocommit=True)
cursor = conn.cursor()

cursor.execute("create database if not exists rental;")
cursor.execute("create database if not exists price;")
cursor.execute("create database if not exists aptadditional;")

# rental database
cursor.execute("use rental;")
cursor.execute("drop table if exists property_amenities;")
cursor.execute("drop table if exists amenities;")
cursor.execute("drop table if exists general_info;")
cursor.execute("drop table if exists property_details;")

cursor.execute("""
create table general_info (
    id varchar(100) primary key,
    title text,
    cityname varchar(100),
    state varchar(100),
    latitude decimal(9, 6),
    longitude decimal(9, 6)
);
""")

cursor.execute("""
create table property_details (
    id varchar(100),
    square_feet bigint,
    bedrooms decimal(2, 1),
    bathrooms decimal(2, 1),
    pets_allowed varchar(100),
    primary key (id),
    foreign key (id) references general_info(id) on delete cascade on update cascade
);
""")

cursor.execute("""
create table amenities (
    amenity_id int auto_increment primary key,
    amenity_name varchar(100)
);
""")

cursor.execute("""
create table property_amenities (
    id varchar(100),
    amenity_id int,
    primary key (id, amenity_id),
    foreign key (id) references general_info(id) on delete cascade on update cascade,
    foreign key (amenity_id) references amenities(amenity_id) on delete cascade on update cascade
);
""")

# price database
cursor.execute("use price;")
cursor.execute("drop table if exists price_details;")
cursor.execute("drop table if exists pricing;")

cursor.execute("""
create table pricing (
    id varchar(100) primary key,
    price int,
    currency varchar(100)
);
""")

cursor.execute("""
create table price_details (
    id varchar(100),
    price_display varchar(100),
    price_type varchar(100),
    primary key (id),
    foreign key (id) references pricing(id) on delete cascade on update cascade
);
""")

# aptadditional database
cursor.execute("use aptadditional;")
cursor.execute("drop table if exists sources;")
cursor.execute("drop table if exists media;")

cursor.execute("""
create table media (
    id varchar(100) primary key,
    has_photo varchar(100)
);
""")

cursor.execute("""
create table sources (
    id varchar(100),
    source varchar(100),
    time datetime,
    primary key (id),
    foreign key (id) references media(id) on delete cascade on update cascade
);
""")

print("MySQL Database structure created successfully.")

# Load into rental database
engine_rental = sqlalchemy.create_engine("mysql+pymysql://root:Dsci-551@localhost/rental")

pd.read_csv("generalInfo.csv").to_sql("general_info", con=engine_rental, if_exists="append", index=False, chunksize=1000)
print("Done generalInfo.csv")

pd.read_csv("propertyDetails.csv").to_sql("property_details", con=engine_rental, if_exists="append", index=False, chunksize=1000)
print("Done propertyDetails.csv")

pd.read_csv("amenities.csv").to_sql("amenities", con=engine_rental, if_exists="append", index=False, chunksize=1000)
print("Done amenities.csv")

pd.read_csv("amenities_types.csv").to_sql("property_amenities", con=engine_rental, if_exists="append", index=False, chunksize=1000)
print("Done amenities_types.csv")

# Load into price database
engine_price = sqlalchemy.create_engine("mysql+pymysql://root:Dsci-551@localhost/price")

pd.read_csv("pricing.csv").to_sql("pricing", con=engine_price, if_exists="append", index=False, chunksize=1000)
print("Done pricing.csv")

pd.read_csv("payment.csv").to_sql("price_details", con=engine_price, if_exists="append", index=False, chunksize=1000)
print("Done payment.csv")

# Load into aptadditional database
engine_apt = sqlalchemy.create_engine("mysql+pymysql://root:Dsci-551@localhost/aptadditional")

pd.read_csv("media.csv").to_sql("media", con=engine_apt, if_exists="append", index=False, chunksize=1000)
print("Done media.csv")

pd.read_csv("sources.csv").to_sql("sources", con=engine_apt, if_exists="append", index=False, chunksize=1000)
print("Done sources.csv")

print("All imported.")
