from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_restful import Resource, Api
from flask_socketio import send, emit
import threading
import time
import ClientTwoSocket
import socketio
import time

sio1 = socketio.Client()
sio2 = socketio.Client()

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'secret!'
socketio_z = SocketIO(app, cors_allowed_origins="*")


def magnum():
    sio1.connect('http://192.168.43.92:5000')
    sio2.connect('http://192.168.43.92:5001')


@socketio_z.on('message')
def handle_message(message):
    print(message)
    if message == "magnum":
        t1 = threading.Thread(name="magnum", target=magnum)
        t1.start()
        time.sleep(5)
        emit("message", "magnum", broadcast=True)


@socketio_z.on('response')
def handle_response(response):
    print(response)
    emit('message', response,  broadcast=True)


@socketio_z.on('json')
def handle_json(json):
    print('received json: ' + str(json))


@socketio_z.on('my event')
def handle_my_custom_event(msg):
    emit('message', msg)


def send_Message():
    handle_my_custom_event("hi")


# client code
@sio1.event
def message(message):
    print('I received a message!', message)
    sio2.emit('response2', message)

# Checking Event Start


@sio2.event
@sio1.event
def connect():
    print("I'm connected!")


@sio2.event
@sio1.event
def connect_error():
    print("The connection failed!")


@sio2.event
@sio1.event
def disconnect():
    print("I'm disconnected!")

# Checking Event Stop

# Checking Event Start 2


@sio2.event
def response2(response2):
    print('I received a message!', response2)
    sio1.emit('response', response2)

# Checking Event Stop 2


if __name__ == '__main__':
    socketio_z.run(app, host='0.0.0.0')
