from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/weather/current')
def current_weather():
    city = request.args.get('city', 'London')
    data = {
        'city': city,
        'temperature': '24°C',
        'condition': 'Sunny',
        'humidity': '60%'
    }
    return jsonify(data)

@app.route('/api/weather/forecast')
def forecast_weather():
    city = request.args.get('city', 'London')
    days = int(request.args.get('days', 3))
    forecast = []
    for i in range(1, days + 1):
        forecast.append({
            'day': f'Day {i}',
            'temperature': f'{22 + i}°C',
            'condition': 'Partly Cloudy'
        })
    return jsonify({
        'city': city,
        'forecast_days': days,
        'forecast': forecast
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
