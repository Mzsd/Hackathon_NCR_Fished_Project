from flask import Flask, render_template

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
google_maps_api_key = 'AIzaSyD32bveBrwe-P40Q-cOTvc3NJPz2rF_j_I'

@app.route('/')
def index():
    return render_template('index.html', google_maps_api_key=google_maps_api_key)

if __name__ == '__main__':
    app.run(debug=True)
