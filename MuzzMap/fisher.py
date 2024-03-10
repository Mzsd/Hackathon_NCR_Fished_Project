from pymongo import MongoClient
import random
import time
import json


# Connect to MongoDB
client = MongoClient('mongodb://root:example@localhost:27017/')
db = client['ncr_atms']

# collist = db.list_collection_names()
# if "AtmStatus" in collist:
#     print("The collection exists.")
# else:
collection = db['AtmStatus']

with open('HSBC_atms.json') as f:
    hsbc_atms = json.load(f)['data'][0]['Brand']
    
# For each brand
json_data = [
        {
            "site_name": atm['Location']['Site']['Name'],
            "atm_id" : atm['Identification'],
            "branch_id" : atm['Branch']['Identification'],
            "GeographicCoordinates": {
                "latitude": float(atm['Location']['PostalAddress']['GeoLocation']['GeographicCoordinates']['Latitude']),
                "longitude": float(atm['Location']['PostalAddress']['GeoLocation']['GeographicCoordinates']['Longitude'])
            },
            "timestamp": int(time.time())
        }
    
        for b in hsbc_atms 
        for atm in b['ATM']
    ]

max_fished = random.randint(1, (len(json_data) - 1) // 50 )
random_number = random.randint(1, len(json_data) - 1)

# Get random site
random_site = json_data[random_number]

# Sort the json_data based on distance from random_site
json_data.sort(
    key=lambda site: 
        abs(site['GeographicCoordinates']['longitude'] - random_site['GeographicCoordinates']['longitude']) + 
        abs(site['GeographicCoordinates']['latitude'] - random_site['GeographicCoordinates']['latitude'])
    )

# Select the closest sites
selected_sites = json_data[:max_fished]

# Print the selected sites
for k, site in enumerate(selected_sites):
    if k == 0:
        print("Main Site: ", random_site)
    else:
        print(site)

# Insert the data into the collection
collection.insert_many(selected_sites)

# Close the connection
client.close()
