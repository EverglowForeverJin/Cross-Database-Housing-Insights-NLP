import sqlalchemy
import pymysql
import sys
import pandas as pd

# Load into rental database
engine_rental = sqlalchemy.create_engine('mysql+pymysql://root:Dsci-551@localhost/rental')

print("Begin generalInfo.csv")
pd.read_csv('generalInfo.csv').to_sql('generalInfo', con=engine_rental, if_exists='append', index=False)
print("Done generalInfo.csv")

print("Begin propertyDetails.csv")
pd.read_csv('propertyDetails.csv').to_sql('propertyDetails', con=engine_rental, if_exists='append', index=False)
print("Done propertyDetails.csv")

print("Begin amenities.csv")
pd.read_csv('amenities.csv').to_sql('amenities', con=engine_rental, if_exists='append', index=False)
print("Done amenities.csv")

print("Begin amenities_types.csv")
pd.read_csv('amenities_types.csv').to_sql('amenities_types', con=engine_rental, if_exists='append', index=False, chunksize=1000)
print("Done amenities_types.csv")

# Load into price database
engine_price = sqlalchemy.create_engine('mysql+pymysql://root:Dsci-551@localhost/price')

print("Begin pricing.csv")
pd.read_csv('pricing.csv').to_sql('pricing', con=engine_price, if_exists='append', index=False)
print("Done pricing.csv")

print("Begin payment.csv")
pd.read_csv('payment.csv').to_sql('payment', con=engine_price, if_exists='append', index=False)
print("Done payment.csv")

# Load into aptadditional database
engine_apt = sqlalchemy.create_engine('mysql+pymysql://root:Dsci-551@localhost/aptadditional')

print("Begin media.csv")
pd.read_csv('media.csv').to_sql('media', con=engine_apt, if_exists='append', index=False)
print("Done media.csv")

print("Begin sources.csv")
pd.read_csv('sources.csv').to_sql('sources', con=engine_apt, if_exists='append', index=False)
print("Done sources.csv")

print("Finished")