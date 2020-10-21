from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_restful import Resource, Api
from flask_socketio import send, emit
import threading
import time
import socketio
import redis
check = 0

sio1 = socketio.Client()

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'secret!'
socketio_z = SocketIO(app, message_queue='redis://', cors_allowed_origins="*")


def magnum():
    sio1.connect('http://192.168.43.92:5001')
    sio1.emit("message", "magnum")


def callMsg():
    sio1.emit("message", "magnum")


@socketio_z.on('message')
def handle_message(message):
    global check
    print(message)
    if message["message"] == "magnum":
        if(check == 0):
            check = 1
            t1 = threading.Thread(name="magnum", target=magnum)
            t1.start()
        else:
            callMsg()
        # else:

    else:
        emit("message", "hello world")


# client code
@sio1.event
def message(message):
    print('I received a message!', message)


@sio1.event
def connect():
    print("I'm connected!")


@sio1.event
def connect_error():
    print("The connection failed!")


@sio1.event
def disconnect():
    print("I'm disconnected!")

# Checking Event Stop

# Checking Event Start 2


if __name__ == '__main__':
    socketio_z.run(app, host='0.0.0.0')
    r = redis.Redis()
