from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    text = data.get('text', '')

    with open('data.txt', 'a', encoding='utf-8') as f:
        f.write(text + '\n')

    return jsonify({'status': 'ok', 'recegit add .gitignore app.pyived': text})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)