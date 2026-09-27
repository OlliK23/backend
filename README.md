# Backend — лабораторная работа по Git

Flask-сервер, принимающий данные от frontend и сохраняющий их в файл `data.txt`.

## Версии

- **v1.0** — приём POST-запросов на `/api/data`, запись в `data.txt`
- **v2.0** — добавлен GET-эндпоинт `/api/read`, возвращающий содержимое `data.txt`

## Запуск

```bash
pip install flask flask-cors
python app.py