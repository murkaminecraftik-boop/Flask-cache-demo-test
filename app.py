from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

ideas_db = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/ideas', methods=['GET', 'POST'])
def manage_ideas():
    if request.method == 'POST':
        data = request.get_json()
        if 'idea' in data and data['idea'].strip():
            ideas_db.append(data['idea'].strip())
        return jsonify({"status": "success"})

    return jsonify(ideas_db)


if __name__ == '__main__':
    app.run(debug=True)