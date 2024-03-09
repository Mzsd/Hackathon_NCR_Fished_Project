from flask import Flask, render_template
import json

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
google_maps_api_key = 'AIzaSyD32bveBrwe-P40Q-cOTvc3NJPz2rF_j_I'

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


if __name__ == '__main__':
    app.run(debug=True)
