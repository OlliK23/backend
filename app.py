from flask import Flask, request, jsonify
import os

app = Flask(__name__)
DATA_FILE = 'data.txt'

# Версия 1.0: принимать данные и сохранять в файл
@app.route('/api/send-name', methods=['POST'])
def send_name():
    data = request.get_json()
    name = data.get('name', '')
    if name:
        with open(DATA_FILE, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
        return jsonify({"status": "ok", "message": "Данные получены"}), 200
    return jsonify({"status": "error", "message": "Имя не указано"}), 400

# Версия 2.0: читать данные из файла
@app.route('/api/get-names', methods=['GET'])
def get_names():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        return content, 200
    return "Файл пуст", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)