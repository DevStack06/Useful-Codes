
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_restful import Resource, Api
from flask_socketio import send, emit
import threading
import time
import ClientTwoSocket
import socketio
import time
check = 0
sio1 = socketio.Client()
sio2 = socketio.Client()

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'secret!'
socketio_z = SocketIO(app, cors_allowed_origins="*")


def magnum():
    sio1.connect('http://192.168.43.92:5000',  namespaces=['/ansible'])
    emit("message", "hello world", namespace='/ansible')


@socketio_z.on('message', namespace='/chat')
def handle_message(message):
    global check
    print(message)
    if message["message"] == "magnum":
        if(check == 0):
            check = 1
            t1 = threading.Thread(name="magnum", target=magnum)
            t1.start()
            # time.sleep(5)

    else:
        emit("message", "hello world", namespace='/chat')


@socketio_z.on('message', namespace='/ansible')
def on_message(message):
    print("meessgae recieved")
    emit("message", "hello world2", namespace='/chat')


@sio1.on('connect', namespace='/ansible')
def get_message():
    print("connected")


@sio1.event
def message(message):
    print('I received a message!', message)


# Checking Event Stop 2
if __name__ == '__main__':
    socketio_z.run(app, host='0.0.0.0')
