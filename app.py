from flask import Flask, render_template, request, jsonify
import pandas as pd
import math

app = Flask(__name__)

# Load the toilet facility dataset
# Assumes the CSV has columns: 'name', 'latitude', 'longitude'
toilet_df = pd.read_csv('fac_p_12.csv')

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the Earth (specified in decimal degrees).
    Returns distance in kilometers.
    """
    R = 6371  # Earth radius in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_nearest_toilet', methods=['POST'])
def get_nearest_toilet():
    """
    Expects a JSON payload with 'latitude' and 'longitude' provided by the client.
    Returns the nearest toilet facility and the distance (in km) as JSON.
    """
    data = request.get_json()
    user_lat = data.get('latitude')
    user_lon = data.get('longitude')
    
    if user_lat is None or user_lon is None:
        return jsonify({'error': 'Missing location data'}), 400

    # Initialize minimum distance and nearest facility
    min_distance = float('inf')
    nearest_toilet = None

    # Iterate over each toilet facility in the dataset
    for _, row in toilet_df.iterrows():
        toilet_lat = row['latitude']
        toilet_lon = row['longitude']
        distance = haversine(user_lat, user_lon, toilet_lat, toilet_lon)
        if distance < min_distance:
            min_distance = distance
            nearest_toilet = row.to_dict()

    return jsonify({
        'nearest_toilet': nearest_toilet,
        'distance_km': min_distance
    })

@app.route('/start_navigation', methods=['POST'])
def start_navigation():
    data = request.get_json()
    user_lat = data.get('latitude')
    user_lon = data.get('longitude')
    toilet_lat = data.get('toilet_lat')
    toilet_lon = data.get('toilet_lon')
    
    if not all([user_lat, user_lon, toilet_lat, toilet_lon]):
        return jsonify({'error': 'Missing navigation data'}), 400

    maps_url = (
        f"https://www.google.com/maps/dir/?api=1"
        f"&origin={user_lat},{user_lon}"
        f"&destination={toilet_lat},{toilet_lon}"
        f"&travelmode=walking"
    )
    
    return jsonify({'maps_url': maps_url})


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
    app.run(debug=True)
