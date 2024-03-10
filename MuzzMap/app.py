from flask import Flask, render_template, jsonify,request
from pymongo import MongoClient
import json
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
google_maps_api_key = 'AIzaSyD32bveBrwe-P40Q-cOTvc3NJPz2rF_j_I'
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
