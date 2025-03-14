from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

model_path = 'random_forest_model.pkl'
rf_model = joblib.load(model_path)

@app.route('/read-form', methods=['POST'])
def read_form():
    data = request.form



    def safe_get(data, key, default):
        value = data.get(key, default)
        if value == "":  
            return default
        return type(default)(value)  


    to_process = {
        "squareMeters": safe_get(data, 'squareMeters', 50.0),
        "rooms": safe_get(data, 'rooms', 3),
        "floor": safe_get(data, 'floor', 1),
        "floorCount": safe_get(data, 'floorCount', 1),
        "latitude": safe_get(data, 'latitude', 21.0118),
        "longitude": safe_get(data, 'longitude', 52.2298),
        "centreDistance": safe_get(data, 'centreDistance', 0.1),
        "poiCount": safe_get(data, 'poiCount', 20),
        "hasParkingSpace": safe_get(data, 'hasParkingSpace', 1),
        "hasBalcony": safe_get(data, 'hasBalcony', 1),
        "hasElevator": safe_get(data, 'hasElevator', 1),
        "hasSecurity": safe_get(data, 'hasSecurity', 1),
        "hasStorageRoom": safe_get(data, 'hasStorageRoom', 1),
        "type_numerical": safe_get(data, 'type', 0),
        "city_numerical": safe_get(data, 'city', 13)
    }

    print(to_process)
    
    df = pd.DataFrame.from_dict([to_process])
    prediction = rf_model.predict(df)

    return jsonify({'prediction': '%.2f' % prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)