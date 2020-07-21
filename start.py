from flask import Flask, request
from settings import API_CONFIRM_TOKEN
from Create_answer import  create_answer

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/', methods=['POST'])
def bot():
    data = request.get_json(force=True, silent=True)

    if not data or 'type' not in data:
        return "Don't reg!"

    if data['type'] == 'confirmation':
        return API_CONFIRM_TOKEN

    elif data['type'] == 'message_new':
        create_answer(data['object'])

        return 'ok'

    return 'ok'