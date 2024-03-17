from flask import Flask, render_template, jsonify,request
from pymongo import MongoClient
import json
import requests
import math

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
google_maps_api_key = '<google-api>'
# Connect to MongoDB
client = MongoClient('mongodb://root:example@localhost:27017/')
db = client['ncr_atms']
collection = db['AtmStatus']

@app.route('/')
def atms():
    with open('HSBC_atms.json') as f:
        hsbc_atms = json.load(f)['data'][0]['Brand']
    
    markers = []
    for b in hsbc_atms:
        for atm in b['ATM']:
            lat = float(atm['Location']['PostalAddress']['GeoLocation']['GeographicCoordinates']['Latitude'])
            lng = float(atm['Location']['PostalAddress']['GeoLocation']['GeographicCoordinates']['Longitude'])
            markers.append({'lat': lat, 'lng': lng})
    
    return render_template('index.html', markers=markers)


def calculate_distance(coord1, coord2):
    lat1, lon1 = map(float, coord1)
    lat2, lon2 = map(float, coord2)
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)


def nearest_neighbor(engineer_location, locations):
    unvisited = set(locations.keys())
    path = [engineer_location]

    while unvisited:
        nearest = min(unvisited, key=lambda x: calculate_distance(
            locations[path[-1]], locations[x]))
        path.append(nearest)
        unvisited.remove(nearest)

    return path


@app.route('/generate_route', methods=['POST'])
def generate_route():
    # Extract data from the JSON request
    data = request.json
    engineer_location = data['engineer_location']
    atm_locations = data['atm_locations']

    # Calculate the nearest neighbor path
    path = nearest_neighbor(engineer_location, atm_locations)
    path.pop(1)

    print("Path:", path)

    # You can return a response if needed
    return jsonify({'status': 'success'})

@app.route('/check_compromised')
def check_compromised():
    with open('HSBC_atms.json') as f:
        hsbc_atms = json.load(f)['data'][0]['Brand']

    compromised_atms = []

    for b in hsbc_atms:
        for atm in b['ATM']:
            identification = atm['Identification']
            
            # print(identification)

            # Query MongoDB to check if the ATM is in the collection
            db_atm = collection.find_one({'Identification': identification})

            if db_atm:
                print(db_atm)
                # Check the most recent entry and its status
                recent_entry = collection.find({'Identification': identification}).sort(
                    'Timestamp', -1).limit(1)[0]

                if recent_entry['Status'] == False:
                    compromised_atms.append({
                        'Identification': identification,
                        'Location': atm['Location']['Site']['Name'],
                        'Latitude': float(atm['Location']['PostalAddress']['GeoLocation']['GeographicCoordinates']['Latitude']),
                        'Longitude': float(atm['Location']['PostalAddress']['GeoLocation']['GeographicCoordinates']['Longitude']),
                        
                    })
    print(compromised_atms)

    return jsonify({'compromised_atms': compromised_atms})

# Route to fetch data from the JSON server


@app.route('/data')
def get_data():
    json_server_url = 'http://localhost:3001/data'
    response = requests.get(json_server_url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True,port=5001)
