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
    if message == "magnum":
        Sendmsg()


def Sendmsg():
    print("hello")
    socketio.emit('message', "1st ho gya")
    time.sleep(30)
    socketio.emit('message', "2rd ho gya")
    time.sleep(30)
    socketio.emit('message', "3rd ho gya")
    time.sleep(30)
    socketio.emit('message', "4th ho gya")


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)
