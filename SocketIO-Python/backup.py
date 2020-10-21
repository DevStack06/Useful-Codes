import socketio
import requests
import threading
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask_restful import Resource, Api
import sys
sys.path.append("..")
sio = socketio.Client()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('response')
def handle_response(response):
    print("Handle Response called")
    emit('message', response)


@socketio.on('message')
def handle_message(message):
    try:
        emit('message', "Spinning up Magnum Infrastructure..")

    except Exception as e:
        print(e)
        emit('message', "Sorry I am not trained to do that yet...")


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
