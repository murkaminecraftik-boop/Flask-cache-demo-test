from flask import Flask, request, jsonify, render_template
import time
import random
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/weather')
def weather():
    start_time = time.time()

    city = request.args.get('city', 'Unknown').lower()

    time.sleep(2)

    data = {
        "city": city.capitalize(),
        "temperature": random.randint(-10, 35),
        "cached": False
    }

    duration = time.time() - start_time
    app.logger.info(f"[БЕЗ КЭША] Город: {city} | Взято из кэша: НЕТ | Время обработки: {duration:.4f} сек")

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)