from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# ============ v1.0: приём данных ============
@app.route('/api/data', methods=['POST'])
def receive_data():
    """Принимает JSON {'text': '...'} и дописывает текст в data.txt"""
    data = request.get_json()
    text = data.get('text', '')

    with open('data.txt', 'a', encoding='utf-8') as f:
        f.write(text + '\n')

    return jsonify({'status': 'ok', 'received': text})

# ============ v2.0: чтение данных ============
@app.route('/api/read', methods=['GET'])
def read_data():
    """Возвращает содержимое data.txt"""
    if not os.path.exists('data.txt'):
        return jsonify({'content': '', 'status': 'empty'})

    with open('data.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    return jsonify({'content': content, 'status': 'ok'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)