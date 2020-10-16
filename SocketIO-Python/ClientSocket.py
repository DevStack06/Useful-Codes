import socketio
import time

sio = socketio.Client()


@sio.event
def message(message):
    print('React Got Msg: ', message)


@sio.event
def connect():
    print("I'm connected!")
    sio.emit('message', "magnum")


@sio.event
def connect_error():
    print("The connection failed!")


@sio.event
def disconnect():
    print("I'm disconnected!")


if __name__ == '__main__':
    sio.connect('http://192.168.43.92:5000')
