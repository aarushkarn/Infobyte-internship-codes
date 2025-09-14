# welcome to my cozy weather app script!
# You'll need Flask and requests installed

from flask import Flask, request, render_template, jsonify
import requests #asking internet

app = Flask(__name__)

# Get your own API key 
OPENWEATHER_API = ''

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/weather')
def send_weather():
    city = request.args.get('city', 'Jaipur')  # If no city, default to Jaipur
    if not city:
        return jsonify({'error': 'City name is missing!'}), 400

    
    source = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API}&units=metric"
    reply = requests.get(source)
    if reply.status_code != 200:
        return jsonify({'error': 'Something went wrong fetching weather.'}), 500

    data = reply.json()
    # Scoop out only what matters
    weather_stuff = {
        'place': data.get('name', city),
        'temperature': data.get('main', {}).get('temp', 'No temp!?'),
        'summary': data.get('weather', [{}])[0].get('description', 'No weather info.'),
        'humidity': data.get('main', {}).get('humidity', '?'),
    }
    return jsonify(weather_stuff)

if __name__ == '__main__':
    app.run(debug=True)
