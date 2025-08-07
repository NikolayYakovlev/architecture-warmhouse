from flask import Flask, request, jsonify

import random, datetime

app = Flask(__name__)

@app.route('/temperature', methods=['GET'], strict_slashes=False)
@app.route('/temperature/<sensorID>', methods=['GET'], strict_slashes=False)
def get_temperature(sensorID=None):
    location = request.args.get('location', '')

    # If no location is provided, use a default based on sensor ID
    if not location:
        if sensorID == "1":
            location = "Living Room"
        elif sensorID == "2":
            location = "Bedroom"
        elif sensorID == "3":
            location = "Kitchen"
        else:
            location = "Unknown"

    # If no sensor ID is provided, generate one based on location
    if not sensorID:
        if location == "Living Room":
            sensorID = "1"
        elif location == "Bedroom":
            sensorID = "2"
        elif location == "Kitchen":
            sensorID = "3"
        else:
            sensorID = "0"

    temperature = round(random.uniform(15.0, 30.0), 2)
    return jsonify({
        'value': temperature,
        'unit': '°C',
        'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'location': location,
        'status': 'active',
        'sensor_id': sensorID,
        'sensor_type': 'temperature',
        'description': ''
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081) 
