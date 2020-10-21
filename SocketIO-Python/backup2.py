from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_restful import Resource, Api
from flask_socketio import send, emit
import time
app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handle_message(message):
    print(message)
    Sendmsg()


@socketio.on('response2')
def handle_response(response2):
    print(response2)
    if response2 == "magnum":
        Sendmsg()
        # emit('response2', "magnum Got Help you")


@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))


@socketio.on('my event')
def handle_my_custom_event(msg):
    emit('message', msg)


def Sendmsg():
    print("hello")
    socketio.emit('response', "1st ho gya")
    time.sleep(30)
    socketio.emit('response', "2rd ho gya")
    time.sleep(30)
    socketio.emit('response', "3rd ho gya")
    time.sleep(30)
    socketio.emit('response', "4th ho gya")


def send_Message():
    handle_my_custom_event("hi")


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8090)
