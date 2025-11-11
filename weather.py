from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock weather data for different cities
weather_data = {
    'London': {'temperature': '15°C', 'condition': 'Cloudy', 'humidity': '75%'},
    'Paris': {'temperature': '18°C', 'condition': 'Sunny', 'humidity': '60%'},
    'New York': {'temperature': '12°C', 'condition': 'Rainy', 'humidity': '80%'},
    'Tokyo': {'temperature': '20°C', 'condition': 'Clear', 'humidity': '65%'},
    'Zanzibar': {'temperature': '29°C', 'condition': 'Humid', 'humidity': '85%'}
}

# Mock forecast data (simplified 3-day forecast)
forecast_template = [
    {'day': 'Day 1', 'temperature': '22°C', 'condition': 'Sunny'},
    {'day': 'Day 2', 'temperature': '24°C', 'condition': 'Partly Cloudy'},
    {'day': 'Day 3', 'temperature': '21°C', 'condition': 'Light Rain'}
]


@app.route('/api/weather/current')
def current_weather():
    city = request.args.get('city', 'Unknown')
    data = weather_data.get(city)

    if data:
        return jsonify({
            'city': city,
            'temperature': data['temperature'],
            'condition': data['condition'],
            'humidity': data['humidity']
        })
    else:
        return jsonify({'error': f'Weather data for {city} not found'}), 404


@app.route('/api/weather/forecast')
def forecast_weather():
    city = request.args.get('city', 'Unknown')
    days = int(request.args.get('days', 3))

    forecast = forecast_template[:days]
    return jsonify({
        'city': city,
        'forecast_days': days,
        'forecast': forecast
    })


if __name__ == '__main__':
    app.run(debug=True, port=5001)
