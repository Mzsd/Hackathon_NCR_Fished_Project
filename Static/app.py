from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime

import requests

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://root:example@localhost:27017/')
db = client['ncr_atms']
collection = db['AtmStatus']
app = Flask(__name__)

# Route to serve the HTML file


@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch data from the JSON server
@app.route('/data')
def get_data():
    json_server_url = 'http://localhost:3001/data'
    response = requests.get(json_server_url)
    return jsonify(response.json())


@app.route('/toggle_status', methods=['POST'])
def toggle_status():
    data = request.get_json()

    # Update MongoDB
    document = {
        "Identification": data.get("Identification"),
        "Status": data.get("Status"),
        "Timestamp": datetime.utcnow()
    }
    collection.insert_one(document)
    print(f"Status toggled successfully for Identification {data.get('Identification')}")


    return jsonify({"message": "Status toggled successfully."})

if __name__ == '__main__':
    app.run(debug=True)
