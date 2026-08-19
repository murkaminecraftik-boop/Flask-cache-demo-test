from flask import Flask, request, jsonify, render_template
from flask_caching import Cache
import time
import random
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 30
cache = Cache(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/weather')
def weather():
    start_time = time.time()

    city = request.args.get('city', 'Unknown').lower()
    cached_data = cache.get(city)

    if cached_data:
        result = {**cached_data, "cached": True}

        duration = time.time() - start_time
        app.logger.info(f"[КЭШ ДЕМО] Город: {city} | Взято из кэша: ДА | Время обработки: {duration:.4f} сек")

        return jsonify(result)

    time.sleep(2)

    data = {
        "city": city.capitalize(),
        "temperature": random.randint(-10, 35)
    }

    cache.set(city, data)

    result = {**data, "cached": False}

    duration = time.time() - start_time
    app.logger.info(f"[КЭШ ДЕМО] Город: {city} | Взято из кэша: НЕТ | Время обработки: {duration:.4f} сек")

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)