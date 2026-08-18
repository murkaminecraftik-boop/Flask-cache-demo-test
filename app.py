from flask import Flask, request, jsonify, render_template
import time
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

ideas_db = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/ideas', methods=['GET', 'POST'])
def manage_ideas():
    start_time = time.time()

    if request.method == 'POST':
        data = request.get_json()
        if 'idea' in data and data['idea'].strip():
            ideas_db.append(data['idea'].strip())


        duration = time.time() - start_time
        app.logger.info(f"[БЕЗ КЭША] Добавлена новая идея | Время обработки (POST): {duration:.4f} сек")

        return jsonify({"status": "success"})

    duration = time.time() - start_time
    app.logger.info(f"[БЕЗ КЭША] Отдан список идей | Время обработки (GET): {duration:.4f} сек")

    return jsonify(ideas_db)


if __name__ == '__main__':
    app.run(debug=True)