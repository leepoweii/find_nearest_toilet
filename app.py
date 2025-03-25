from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
import math
import numpy as np

app = Flask(__name__)

# Load the toilet facility dataset
# Assumes the CSV has columns: 'name', 'latitude', 'longitude'
# Load all CSV files from ./data/ and concatenate into a single DataFrame

toilet_df = pd.read_csv('data/all_toilets.csv')


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


def haversine_vectorized(lat1, lon1, lat2, lon2):
    """
    Vectorized haversine calculation using numpy.
    lat1, lon1: Scalar values for the user coordinates.
    lat2, lon2: Pandas Series or numpy arrays for facility coordinates.
    Returns: numpy array of distances in km.
    """
    R = 6371  # km
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_nearest_toilet', methods=['POST'])
def get_nearest_toilet():
    """
    Expects a JSON payload with 'latitude' and 'longitude', then returns
    the nearest toilet facility and its distance (in km).
    """
    data = request.get_json()
    user_lat = data.get('latitude')
    user_lon = data.get('longitude')
    
    if user_lat is None or user_lon is None:
        return jsonify({'error': 'Missing location data'}), 400

    user_lat = float(user_lat)
    user_lon = float(user_lon)
    
    # Compute distances for all facilities
    distances = haversine_vectorized(
        user_lat, user_lon,
        toilet_df['latitude'], toilet_df['longitude']
    )
    
    # Find the index of the minimum distance
    min_index = distances.idxmin()
    nearest_toilet = toilet_df.loc[min_index].to_dict()
    min_distance = distances[min_index]
    
    return jsonify({
        'nearest_toilet': nearest_toilet,
        'distance_km': min_distance
    })

#@app.route('/start_navigation', methods=['POST'])
#def start_navigation():
#    data = request.get_json()
#    user_lat = data.get('latitude')
#    user_lon = data.get('longitude')
#    toilet_lat = data.get('toilet_lat')
#    toilet_lon = data.get('toilet_lon')
#    
#    if not all([user_lat, user_lon, toilet_lat, toilet_lon]):
#        return jsonify({'error': 'Missing navigation data'}), 400
#
#    maps_url = (
#        f"https://www.google.com/maps/dir/?api=1"
#        f"&origin={user_lat},{user_lon}"
#        f"&destination={toilet_lat},{toilet_lon}"
#        f"&travelmode=walking"
#    )
#    
#    return jsonify({'maps_url': maps_url})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
    #app.run(debug=True)
