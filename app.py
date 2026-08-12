from flask import Flask, request, jsonify, render_template
from flask_caching import Cache
import time
import random

app = Flask(__name__)

app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 30
cache = Cache(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/weather')
def weather():
    city = request.args.get('city', 'Unknown').lower()

    cached_data = cache.get(city)
    if cached_data:
        cached_data['cached'] = True
        return jsonify(cached_data)

    time.sleep(2)

    data = {
        "city": city.capitalize(),
        "temperature": random.randint(-10, 35),
        "cached": False
    }

    cache.set(city, data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)